#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility to stage updated translation files in git, ignoring files that only have minor changes
to the headers and do not contain changes to the translation strings.
"""

import os
import re
import subprocess
import sys


SHOW_COMPARISONS = 1    # 0 = none, 1 = differences only, 2 = all comparisons

COMMAND_TIMEOUT = 300
LOCALE_DIR = '_locale'


def get_stdout_from_command(command: str):
    """Run the specified command in a shell and return the stdout response as a string.

    Args:
        command (str): Command to run

    Returns:
        str: stdout response for the command output
    """
    print(f"Running command: {command}")
    response = subprocess.run(command, shell=True, check=True, capture_output=True, encoding='utf8', timeout=COMMAND_TIMEOUT)
    return response.stdout


def parse_git_status(git_stat: list, files_to_stage: dict, files_to_ignore: set):
    """Parse the git status response to add new or deleted files.

    Args:
        git_stat (list): List of lines in the git status response
        files_to_stage (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files to not add to git staging
    """
    for line in git_stat:
        matches = re.match(r"\s*(\S+)\s+(.*)$", line)
        if not matches:
            continue
        status = matches.group(1)
        fullfilename = matches.group(2)
        filename = os.path.split(fullfilename)[1]
        _root, ext = os.path.splitext(filename)
        if '_video_thumbnail' in fullfilename:
            files_to_ignore.add(fullfilename)
        elif status == "??" and fullfilename not in files_to_ignore and fullfilename.startswith(LOCALE_DIR) and fullfilename.endswith('/'):
            files_to_stage[fullfilename] = 'Added'
        elif ext not in {'.pot', '.po'}:
            files_to_ignore.add(fullfilename)
        elif status == "D":
            files_to_stage[fullfilename] = 'Deleted'
        elif status == "??" and '_video_thumbnail' not in fullfilename and fullfilename not in files_to_ignore:
            files_to_stage[fullfilename] = 'Added'


def parse_git_diff(git_diff: list, files_to_stage: dict, files_to_ignore: set):
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    """Parse the git diff response.  Do not add translation files that only have changed
    comment lines or minor changes to headers.

    Args:
        git_diff (list): List of lines in the git diff response
        files_to_stage (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files to not add to git staging
    """
    header_keys = '|'.join([
        "Project-Id-Version:",
        "Report-Msgid-Bugs-To:",
        "POT-Creation-Date:",
        "PO-Revision-Date:",
        "Last-Translator:",
        "Language-Team:",
        "Language:",
        "MIME-Version:",
        "Content-Type:",
        "Content-Transfer-Encoding:",
        "Plural-Forms:",
        "Generated-By:",
    ])
    fullfilename = ''
    filename = ''
    ext = ''
    minus = ''
    plus = ''
    last = ''

    def process_change(files_to_stage: dict, fullfilename: str, minus: str, plus: str):
        if (minus or plus) and (SHOW_COMPARISONS > 1 or (SHOW_COMPARISONS == 1 and minus != plus)):
            print(f"\nCompare: {fullfilename}")
            print(f"--- {len(minus):,} characters\n\"{minus}\"\n+++ {len(plus):,} characters\n\"{plus}\"")
        if minus != plus:
            files_to_stage[fullfilename] = 'Modified'
        return '', '', ''

    for line in git_diff:
        # Ignore nearby lines and unchanged ranges
        if line and line[0] in {' ', '@'}:
            continue

        line = line.strip()

        # Ignore selected information lines
        if not line or line.startswith("+++ ") or line.startswith("diff") or line.startswith("index"):
            continue

        # Start a new file filename for processing
        if line.startswith("--- "):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            fullfilename = line[6:].strip()
            filename = os.path.split(fullfilename)[-1]
            _root, ext = os.path.splitext(filename)

        # Ignore non-translation files
        if ext not in {'.pot', '.po'} or not fullfilename.startswith(LOCALE_DIR):
            continue

        # Ignore files already processed
        if fullfilename in files_to_stage or fullfilename in files_to_ignore:
            continue

        # Add changed fuzzy comment lines
        if re.match(r'[+-]#, fuzzy', line, re.IGNORECASE):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            files_to_stage[fullfilename] = 'Modified'
            continue

        # Add changed location comment lines
        if re.match(r'[+-]#: \.\./', line):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            files_to_stage[fullfilename] = 'Modified'
            continue

        # Ignore changed comment lines
        if re.match(r'[+-]#', line):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            continue

        # Ignore changed header lines
        if re.match(r'[+-].*\\n"$', line) or re.match(r'[+-]"(' + header_keys + r')', line, re.IGNORECASE):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            continue

        # Add files with changed translation text lines
        if re.match(r'[+-](msgid|msgstr)', line):
            minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)
            files_to_stage[fullfilename] = 'Modified'
            continue

        # Combine changed translation text lines within a 'msgid' or 'msgstr' section to
        # accommodate lines wrapped at different lengths but the overall content is the same
        if re.match(r'[+-]"', line):
            action = line[0]
            text = line[2:-1]

            # All related changes in the diff show the removed lines before the added lines
            # so a minus following a plus should signify a new change.
            if last == '+' and action == '-':
                minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)

            if action == '+':
                plus += text
            else:
                minus += text
            last = action
            continue

        minus, plus, last = process_change(files_to_stage, fullfilename, minus, plus)

    # Handle any outstanding changes at the end of the git diff output
    process_change(files_to_stage, fullfilename, minus, plus)


def main():
    """Main processing method.
    """
    files_to_ignore = set()
    files_to_stage = {}

    try:
        command = 'git status --porcelain'
        git_stat = get_stdout_from_command(command).splitlines()

        command = 'git diff --ignore-cr-at-eol'
        git_diff = get_stdout_from_command(command).splitlines()

    except subprocess.SubprocessError as ex:
        print(f"Error running:{command}\nException: {ex}")

    print("Getting the list of translation files.")
    print(" - Parsing the git status output")
    parse_git_status(git_stat, files_to_stage, files_to_ignore)

    print(" - Parsing the git diff output.")
    parse_git_diff(git_diff, files_to_stage, files_to_ignore)

    if files_to_stage:
        print("\nFiles to add to git staging:")
        for filename, action in files_to_stage.items():
            print(f" + {filename} [{action}]")
            command = "git add " + filename
            if subprocess.run(
                    command,
                    shell=True,
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=COMMAND_TIMEOUT
                    ).returncode:
                print("\nThere was a problem adding the file to the commit.\n")
                sys.exit(1)
        print()
    else:
        print("\nNo files to stage for git.\n")

##############################################################################


if __name__ == '__main__':
    main()

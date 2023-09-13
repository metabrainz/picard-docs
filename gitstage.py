#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility to stage updated translation files in git, ignoring files that only have minor changes
to the headers and do not contain changes to the translation strings.
"""

# Copyright (C) 2023 Bob Swift


import argparse
import os
import re
import subprocess
import sys

import conf
from setup import PACKAGE_TITLE


SCRIPT_NAME = 'Picard Docs Git File Stager'
SCRIPT_VERS = '0.4'
SCRIPT_INITIAL_COPYRIGHT = '2023'
SCRIPT_INITIAL_AUTHOR = 'Bob Swift'

DEFAULT_COMPARISON_DISPLAY_LEVEL = 'changed'

COMMAND_TIMEOUT = 300
LOCALE_DIRS = conf.locale_dirs if 'locale_dirs' in conf.__dict__ else ['_locale']

STATUS_FILE = 'git_status.txt'
DIFF_FILE = 'git_diff.txt'

HEADER_KEYS_TO_IGNORE = '|'.join([
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

##################################################
#   Text to display when the script is started   #
##################################################

DESCRIPTION = f"{SCRIPT_NAME} (v{SCRIPT_VERS})"

COPYRIGHT_TEXT = f"""\

{DESCRIPTION}  Copyright (C) {SCRIPT_INITIAL_COPYRIGHT}, {SCRIPT_INITIAL_AUTHOR}
"""

ABOUT_TEXT = f"""\
{COPYRIGHT_TEXT}
This script stages files in git for the {PACKAGE_TITLE} package.

For usage instructions, please use the '--help' option.

This program comes with ABSOLUTELY NO WARRANTY; use the '--warranty'
option for more information.  This is free software, and you are
welcome to redistribute it under certain conditions.  Please see the
GPLv3 license for details.
"""

WARRANTY_TEXT = f"""\
{COPYRIGHT_TEXT}
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT
WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF
THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES
SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE
WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN
ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

If the disclaimer of warranty and limitation of liability provided above
cannot be given local legal effect according to their terms, reviewing
courts shall apply local law that most closely approximates an absolute
waiver of all civil liability in connection with the Program, unless a
warranty or assumption of liability accompanies a copy of the Program in
return for a fee.
"""


class Printer():
    """Custom print helper"""
    silent = False

    @classmethod
    def stdout(cls, text: str = ''):
        """Print the text to stdout if the silent flag has not been set.

        Args:
            text (str, optional): Text to print. Defaults to ''.
        """
        if not cls.silent:
            print(text)

    @staticmethod
    def stderr(text: str = ''):
        """Print the text to stderr, regardless of the silent flag setting.

        Args:
            text (str, optional): Text to print. Defaults to ''.
        """
        sys.stderr.write(f"{text}\n")


def parse_command_line():
    """Parse the command line arguments.
    """
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        '-r', '--rst',
        action='store_true',
        dest='rst',
        help="also stage rst files"
    )

    arg_parser.add_argument(
        '-c', '--comparison-display',
        action='store',
        dest='display',
        nargs='?',
        type=str,
        choices=['none', 'changed', 'all'],
        default='changed',
        help="none = don't show any diffs, "
             "changed = show only changed diffs (default), "
             "all = show all diffs"
    )

    arg_parser.add_argument(
        '-s', '--silent',
        action='store_true',
        dest='silent',
        help="supress all program output"
    )

    arg_parser.add_argument(
        '-d', '--dry-run',
        action='store_true',
        dest='dryrun',
        help="don't stage the files (report only)"
    )

    arg_parser.add_argument(
        '-f', '--files-save',
        action='store_true',
        dest='save_files',
        help="save the git output to files"
    )

    arg_parser.add_argument(
        '-a', '--about',
        action='store_true',
        dest='about',
        help="display information about the script"
    )

    arg_parser.add_argument(
        '-w', '--warranty',
        action='store_true',
        dest='warranty',
        help="display warranty information"
    )

    return arg_parser.parse_args()


def get_stdout_from_command(command: str):
    """Run the specified command in a shell and return the stdout response as a string.

    Args:
        command (str): Command to run

    Returns:
        str: stdout response for the command output
    """
    Printer.stdout(f"Running command: {command}")
    response = subprocess.run(command, shell=True, check=True, capture_output=True, encoding='utf8', timeout=COMMAND_TIMEOUT)
    return response.stdout


def is_in_locale_dir(fullpath: str):
    """Checks if the specified filepath is in a locale directory.

    Args:
        fullpath (str): Full path and name of file to check

    Returns:
        bool: True if the file is in a locale directory otherwise false.
    """
    for locale_dir in LOCALE_DIRS:
        if fullpath.startswith(locale_dir):
            return True
    return False


def parse_git_status(git_stat: list, files_to_stage: dict, files_to_ignore: set, stage_rst: bool = False):
    """Parse the git status response to add new or deleted files.

    Args:
        git_stat (list): List of lines in the git status response
        files_to_stage (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files to not add to git staging
    """
    stage_types = {'.pot', '.po'}
    if stage_rst:
        stage_types.add('.rst')
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
        elif status == "??" and fullfilename not in files_to_ignore and is_in_locale_dir(fullfilename) and fullfilename.endswith('/'):
            files_to_stage[fullfilename] = 'Added'
        elif ext not in stage_types:
            files_to_ignore.add(fullfilename)
        elif status == "D":
            files_to_stage[fullfilename] = 'Deleted'
        elif status == "??" and fullfilename not in files_to_ignore:
            files_to_stage[fullfilename] = 'Added'
        elif status == "M" and fullfilename not in files_to_ignore and stage_rst and ext == '.rst':
            files_to_stage[fullfilename] = 'Modified'


def parse_git_diff(git_diff: list, files_to_stage: dict, files_to_ignore: set, level: str = DEFAULT_COMPARISON_DISPLAY_LEVEL):
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-locals
    """Parse the git diff response.  Do not add translation files that only have changed
    comment lines or minor changes to headers.

    Args:
        git_diff (list): List of lines in the git diff response
        files_to_stage (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files to not add to git staging
        level (str): Comparison display level (none|changed|all)
    """
    fullfilename = ''
    filename = ''
    ext = ''
    minus = ''
    plus = ''
    last = ''
    match_type = ''
    last_type = ''

    def process_change(files_to_stage: dict, fullfilename: str, minus: str, plus: str):
        """Compare the 'plus' and 'minus' strings and mark the file for staging if
        they are different.  Print the diff if the appropriate display level is set.

        Args:
            files_to_stage (dict): Dictionary of files to add to git staging
            fullfilename (str): Full path and name of file being examined
            minus (str): Combined lines being removed
            plus (str): Combined lines being added
        """
        if not minus and not plus:
            return
        if level == 'all' or (minus != plus and level == 'changed'):
            Printer.stdout(f"\nCompare: {fullfilename}")
            Printer.stdout(f"--- {len(minus):,} characters\n\"{minus}\"\n+++ {len(plus):,} characters\n\"{plus}\"")
        if minus != plus:
            files_to_stage[fullfilename] = 'Modified'

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
            process_change(files_to_stage, fullfilename, minus, plus)
            minus = plus = last = ''
            fullfilename = line[6:].strip()
            filename = os.path.split(fullfilename)[-1]
            _root, ext = os.path.splitext(filename)

        # Ignore non-translation files
        if ext not in {'.pot', '.po'} or not is_in_locale_dir(fullfilename):
            continue

        # Ignore files already processed unless printing differences
        if (fullfilename in files_to_stage or fullfilename in files_to_ignore) and level == 'none':
            continue

        # Add changed fuzzy comment lines
        if re.match(r'[+-]#, fuzzy', line, re.IGNORECASE):
            process_change(files_to_stage, fullfilename, minus, plus)
            minus = plus = last = ''
            files_to_stage[fullfilename] = 'Modified'
            continue

        # Add changed location comment lines
        if re.match(r'[+-]#: \.\./', line):
            process_change(files_to_stage, fullfilename, minus, plus)
            minus = plus = last = ''
            files_to_stage[fullfilename] = 'Modified'
            continue

        # Ignore changed comment lines
        if re.match(r'[+-]#', line):
            process_change(files_to_stage, fullfilename, minus, plus)
            minus = plus = last = ''
            continue

        # Ignore changed header lines
        if re.match(r'[+-].*\\n"$', line) or re.match(r'[+-]"(' + HEADER_KEYS_TO_IGNORE + r')', line, re.IGNORECASE):
            process_change(files_to_stage, fullfilename, minus, plus)
            minus = plus = last = ''
            continue

        # Add files with changed translation text lines
        match = re.match(r'[+-](msgid|msgstr)?\s?"', line)
        if match:
            action = line[0]
            match_type = match.group(1)
            text = line[len(match.group(0)):-1]

            # All related changes in the diff show the removed lines before the added lines
            # so a minus following a plus should signify a new change.
            if (last == '+' and action == '-') or (match_type and match_type != last_type):
                process_change(files_to_stage, fullfilename, minus, plus)
                minus = plus = last = last_type = ''

            # Combine changed translation text lines within a 'msgid' or 'msgstr' section to
            # accommodate lines wrapped at different lengths but the overall content is the same
            if action == '+':
                plus += text
            else:
                minus += text

            last = action
            if match_type:
                last_type = match_type
            continue

        process_change(files_to_stage, fullfilename, minus, plus)
        minus = plus = last = match_type = last_type = ''

    # Handle any outstanding changes at the end of the git diff output
    process_change(files_to_stage, fullfilename, minus, plus)


def main():     # pylint: disable=too-many-statements
    """Main processing method.
    """
    args = parse_command_line()

    dry_run = args.dryrun if 'dryrun' in vars(args) else False
    stage_rst = args.rst if 'rst' in vars(args) else False
    silent = args.silent if 'silent' in vars(args) else False
    save_files = args.save_files if 'save_files' in vars(args) else False
    display_comparison_level = args.display if 'display' in vars(args) else DEFAULT_COMPARISON_DISPLAY_LEVEL
    Printer.silent = silent

    if 'about' in vars(args) and args.about:
        Printer.stdout(ABOUT_TEXT)
        sys.exit(0)

    if 'warranty' in vars(args) and args.warranty:
        Printer.stdout(WARRANTY_TEXT)
        sys.exit(0)

    Printer.stdout(f"\n{DESCRIPTION}\n")

    files_to_ignore = set()
    files_to_stage = {}

    try:
        command = 'git status --porcelain'
        git_stat = get_stdout_from_command(command)
        if save_files:
            with open(STATUS_FILE, 'w', encoding='utf-8') as f:
                f.write(git_stat)
        git_stat = git_stat.splitlines()

        command = 'git diff --ignore-cr-at-eol'
        git_diff = get_stdout_from_command(command)
        if save_files:
            with open(DIFF_FILE, 'w', encoding='utf-8') as f:
                f.write(git_diff)
        git_diff = git_diff.splitlines()

    except subprocess.SubprocessError as ex:
        Printer.stderr(f"\nError running:{command}\nException: {ex}")
        sys.exit(1)

    Printer.stdout("Getting the list of translation files.")
    Printer.stdout(" - Parsing the git status output")
    parse_git_status(git_stat, files_to_stage, files_to_ignore, stage_rst)

    Printer.stdout(" - Parsing the git diff output.")
    parse_git_diff(git_diff, files_to_stage, files_to_ignore, display_comparison_level)

    if files_to_stage:
        Printer.stdout("\nFiles to add to git staging:")
        for filename, action in files_to_stage.items():
            Printer.stdout(f' + "{filename}" [{action}]')
            if not dry_run:
                if subprocess.run(
                        f'git add "{filename}"',
                        shell=True,
                        check=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=COMMAND_TIMEOUT
                        ).returncode:
                    Printer.stderr(f"\nThere was a problem adding {filename if silent else 'the file'} to the commit.\n")
                    sys.exit(1)
        if dry_run:
            Printer.stdout("\nNo files staged due to dry run option enabled.")
        Printer.stdout()
    else:
        Printer.stdout("\nNo files to stage for git.\n")

    sys.exit(0)

##############################################################################


if __name__ == '__main__':
    main()

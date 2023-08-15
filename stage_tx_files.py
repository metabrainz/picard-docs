#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility to stage updated translation files in git, ignoring files that only have minor changes
to the headers and do not contain changes to the translation strings.
"""

import os
import re
import subprocess
import sys


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


def parse_git_status(git_stat: list, files_to_add: dict, files_to_ignore: set, rst_files: set, pot_files: set):
    """Parse the git status response.

    Args:
        git_stat (list): List of lines in the git status response
        files_to_add (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files not to add to the git staging
        rst_files (set): Set of *.rst files found
        pot_files (set): Set of *.pot files found
    """
    for line in git_stat:
        matches = re.match(r"\s*(\S+)\s+(.*)$", line)
        if not matches:
            continue
        status = matches.group(1)
        fullfilename = matches.group(2)
        filename = fullfilename.split('/')[-1]
        root, ext = os.path.splitext(filename)
        if status == "D":
            files_to_add[fullfilename] = 'Deleted'
            if ext == '.rst':
                files_to_ignore.add(root + '.pot')
                files_to_ignore.add(root + '.po')
            if ext == '.pot':
                files_to_ignore.add(root + '.po')
            continue
        if status == "??" and "/" in fullfilename:
            if '_video_thumbnail' in fullfilename:  # do not add video thumbnail files
                continue
            if ext not in {'.po', '.pot'}:
                files_to_add[fullfilename] = 'Added'
                continue
            if ext == '.pot' and filename in rst_files and filename not in files_to_ignore:
                files_to_add[fullfilename] = 'Added'
                continue
            if ext == '.po' and filename in rst_files and filename in pot_files and filename not in files_to_ignore:
                files_to_add[fullfilename] = 'Added'
                continue

def parse_git_diff(git_diff: list, files_to_add: dict):
    """Parse the git diff response.  Do not add translation files that only have changed
    comment lines or minor changes to headers.

    Args:
        git_diff (list): List of lines in the git diff response
        files_to_add (dict): Dictionary of files to add to git staging
    """
    for line in git_diff:
        filename = ''
        line = line.strip()
        if line.startswith("--- "):
            filename = line[6:].strip()

            # Add files not in the locale directory (not translation files)
            if not filename.startswith(LOCALE_DIR) and filename not in files_to_add:
                files_to_add[filename] = 'Modified'
            continue

        # Ignore files not identified or already added
        if not filename or filename in files_to_add:
            continue

        # Ignore changed comment lines
        if re.match(r'[+-]#', line):
            continue

        # Ignore changed header lines
        if re.match(r'[+-]"(POT-Creation|PO-Revision|Language-Team|Plural-Forms|X-Generator|Content-Type|Generated-By|Project-Id-Version)', line):
            continue

        # Add files with changed translation text lines
        if re.match(r'[+-](msgid|msgstr|")', line):
            files_to_add[filename] = 'Modified'


def initialize_file_sets(rst_files: set, pot_files: set, files_to_ignore: set):
    """Initialize the file sets.

    Args:
        rst_files (set): Set of *.rst files found
        pot_files (set): Set of *.pot files found
        files_to_ignore (set): Set of files not to add to the git staging
    """
    for _dirname, _dirlist, filelist in os.walk("."):
        for filename in filelist:
            root, ext = os.path.splitext(filename)
            if ext == '.rst':
                rst_files.add(root + '.pot')
            elif ext == '.pot':
                if filename in rst_files:
                    pot_files.add(root + '.po')
                else:
                    files_to_ignore.add(filename)
            elif ext == '.po':
                if filename not in pot_files:
                    files_to_ignore.add(filename)


def main():
    """Main processing method.
    """
    rst_files = set()
    pot_files = set()
    files_to_ignore = set()

    # Add standard files not captured by directory walk
    rst_files.add('sphinx.pot')
    rst_files.add('sphinx.po')

    print("Getting the list of translation files.")
    initialize_file_sets(rst_files, pot_files, files_to_ignore)

    try:
        command = 'git status --porcelain'
        git_stat = get_stdout_from_command(command).splitlines()

        command = 'git diff --ignore-cr-at-eol'
        git_diff = get_stdout_from_command(command).splitlines()

    except subprocess.SubprocessError as ex:
        print(f"Error running:{command}\nException: {ex}")

    files_to_add = {}
    print("Reviewing the changes to identify files to add.")

    print(" - Parsing the git status output.")
    parse_git_status(git_stat, files_to_add, files_to_ignore, rst_files, pot_files)

    print(" - Parsing the git diff output.")
    parse_git_diff(git_diff, files_to_add)

    if files_to_add:
        print("\nFiles to add to git staging:")
        for filename, action in files_to_add.items():
            print(f" + {filename} [{action}]")
            command = "git add " + filename
            exit_code = subprocess.run(command, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=COMMAND_TIMEOUT).returncode
            if exit_code:
                print("\nThere was a problem adding the file to the commit.\n")
                sys.exit(1)
    else:
        print("\nNo files to stage for git.")

    print()

##############################################################################

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Utility to stage updated translation files in git, ignoring files that only have
minor changes to the headers and do not contain changes to the translation strings.
"""

# Copyright (C) 2023-2025 Bob Swift


import argparse
import os
import re
import subprocess
import sys

import conf
from setup import PACKAGE_TITLE


SCRIPT_NAME = 'Picard Docs Git File Stager'
SCRIPT_VERS = '0.7'
SCRIPT_INITIAL_COPYRIGHT = '2023'
SCRIPT_INITIAL_AUTHOR = 'Bob Swift'

COMMAND_TIMEOUT = 300
LOCALE_DIRS = conf.locale_dirs if 'locale_dirs' in conf.__dict__ else ['_locale']

FILE_TYPES = {'.pot', '.po'}

STATUS_FILE = 'git_status.txt'
DIFF_FILE = 'git_diff.txt'

TRANSLATION_KEY_GROUPS = {'msgid', 'msgstr', 'location'}

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

################################
#   Regular expressions used   #
################################

RE_GIT_STAT_LINE = re.compile(r"\s*(\S+)\s+(.*)$")

RE_IGNORE_COMMENT_LINE = re.compile(r'[+-]#')
RE_IGNORE_LINE_STARTS = re.compile(r'^( |@|--- |diff|index)')
RE_IGNORE_HEADER_LINES_1 = re.compile(r'[+-].*\\n"$')
RE_IGNORE_HEADER_LINES_2 = re.compile(r'[+-]"(' + HEADER_KEYS_TO_IGNORE + r')', re.IGNORECASE)

RE_CHANGED_TRANSLATION_LINE = re.compile(r'[+-](msgid|msgstr)\s?"')
RE_CHANGED_STRINGS_LINE = re.compile(r'[+-]"')
RE_CHANGED_LOCATION_LINE = re.compile(r'[+-]#: \.\./')
RE_CHANGED_FUZZY_LINE = re.compile(r'[+-]#, fuzzy', re.IGNORECASE)

##################################################
#   Text to display when the script is started   #
##################################################

DESCRIPTION = f"{SCRIPT_NAME} (v{SCRIPT_VERS})"

COPYRIGHT_TEXT = f"""\

{DESCRIPTION}  Copyright (C) {SCRIPT_INITIAL_COPYRIGHT}, {SCRIPT_INITIAL_AUTHOR}
See comments in the script for additional copyright information.
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


################################################################################

class Printer():
    """Custom print helper"""
    silent = False

    @classmethod
    def stdout(cls, text: str = '') -> None:
        """Print the text to stdout if the silent flag has not been set.

        Args:
            text (str, optional): Text to print. Defaults to ''.
        """
        if not cls.silent:
            print(text)

    @staticmethod
    def stderr(text: str = '') -> None:
        """Print the text to stderr, regardless of the silent flag setting.

        Args:
            text (str, optional): Text to print. Defaults to ''.
        """
        sys.stderr.write(f"{text}\n")


################################################################################

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


################################################################################

def get_stdout_from_command(command: str) -> str:
    """Run the specified command in a shell and return the stdout response as a string.

    Args:
        command (str): Command to run

    Returns:
        str: stdout response for the command output
    """
    Printer.stdout(f"Running command: {command}")
    response = subprocess.run(command, shell=True, check=True, capture_output=True,
                              encoding='utf8', timeout=COMMAND_TIMEOUT)
    return response.stdout


################################################################################

def is_in_locale_dir(fullpath: str) -> bool:
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


################################################################################

def parse_git_status(git_stat: list, files_to_stage: dict, files_to_ignore: set,
                     stage_rst: bool = False) -> None:
    """Parse the git status response to add new or deleted files.

    Args:
        git_stat (list): List of lines in the git status response
        files_to_stage (dict): Dictionary of files to add to git staging
        files_to_ignore (set): Set of files to not add to git staging
        stage_rst: (bool): Whether or not RST files should be staged (default False)
    """
    stage_types = FILE_TYPES
    if stage_rst:
        stage_types.add('.rst')
    for line in git_stat:
        matches = RE_GIT_STAT_LINE.match(line)
        if not matches:
            continue
        status = matches.group(1)
        fullfilename = matches.group(2)
        filename = os.path.split(fullfilename)[1]
        ext = os.path.splitext(filename)[1]
        if '_video_thumbnail' in fullfilename:
            files_to_ignore.add(fullfilename)
        elif status == "??" and fullfilename not in files_to_ignore and \
                is_in_locale_dir(fullfilename) and fullfilename.endswith('/'):
            files_to_stage[fullfilename] = 'Added'
        elif ext not in stage_types:
            files_to_ignore.add(fullfilename)
        elif status == "D":
            files_to_stage[fullfilename] = 'Deleted'
        elif status == "??" and fullfilename not in files_to_ignore:
            files_to_stage[fullfilename] = 'Added'
        elif status == "M" and fullfilename not in files_to_ignore and \
                stage_rst and ext == '.rst':
            files_to_stage[fullfilename] = 'Modified'


################################################################################

def check_tx_strings_differences(tx_strings: dict) -> bool:
    """Checks for mismatches between translation 'msgid' and 'msgstr'
    values added and removed from a file.

    Args:
        tx_strings (dict): Dictionary of sets of translation strings.

    Returns:
        bool: Ture if there is a mismatch, otherwise False.
    """
    for key in TRANSLATION_KEY_GROUPS:
        s_p: set = tx_strings[f"+{key}"]
        s_m: set = tx_strings[f"-{key}"]
        if s_p.difference(s_m) or s_m.difference(s_p):
            return True
    return False


################################################################################

def reset_tx_strings(tx_strings: dict) -> None:
    """Reset the translation strings dictionary.

    Args:
        tx_strings (dict): Translations dictionary to reset.
    """
    for key in tx_strings.keys():
        tx_strings[key] = set()


################################################################################

def do_process(tx_strings: dict, filename: str, fullfilename: str, files_to_stage: dict, files_to_ignore: set) -> None:
    """Process the translation strings for the file and add the file to the
    proper group (stage or ignore).

    Args:
        tx_strings (dict): Translation strings dictionary.
        filename (str): Name of the file.
        fullfilename (str): Full path and name of the file.
        files_to_stage (dict): Dictionary of files to stage.
        files_to_ignore (set): Set of files to ignore.
    """
    if filename and fullfilename not in files_to_stage.keys() and fullfilename not in files_to_ignore:

        if check_tx_strings_differences(tx_strings):
            files_to_stage[fullfilename] = 'Modified'
        else:
            files_to_ignore.add(fullfilename)

    reset_tx_strings(tx_strings)
    filename = fullfilename = ''


################################################################################

def parse_git_diff(git_diff: list, files_to_stage: dict, files_to_ignore: set) -> None:
    """Parse the git diff response.  Do not add translation files that only have changed
    comment lines or minor changes to headers.

    Args:
        git_diff (list): List of lines in the git diff response.
        files_to_stage (dict): Dictionary of files to add to git staging.
        files_to_ignore (set): Set of files to not add to git staging.
    """
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements

    fullfilename = ''
    filename = ''
    tx_strings = {}
    for text in TRANSLATION_KEY_GROUPS:
        tx_strings[f"+{text}"] = set()
        tx_strings[f"-{text}"] = set()

    line_count = len(git_diff)
    line_num = 0
    while line_num < line_count:
        line: str = git_diff[line_num]
        line_num += 1

        # Ignore selected line starts
        if not line or RE_IGNORE_LINE_STARTS.match(line):
            continue

        line = line.strip()

        # Ignore blank lines
        if not line:
            continue

        # Ignore changed comment lines
        if RE_IGNORE_COMMENT_LINE.match(line):
            continue

        # Ignore changed header lines
        if RE_IGNORE_HEADER_LINES_1.match(line) or RE_IGNORE_HEADER_LINES_2.match(line):
            # Keep skipping lines until header line ends with '\n"'
            while line_num < line_count and not RE_IGNORE_HEADER_LINES_1.match(line.strip()):
                line = git_diff[line_num]
                line_num += 1
            continue

        # Start a new file filename for processing
        if line.startswith("+++ "):
            if filename:
                do_process(tx_strings, filename, fullfilename, files_to_stage, files_to_ignore)
            fullfilename = line[6:].strip()
            filename = os.path.split(fullfilename)[-1]

            # Ignore non-translation files
            if os.path.splitext(filename)[1] not in FILE_TYPES or not is_in_locale_dir(fullfilename):
                fullfilename = filename = ''
                continue

            # Ignore files already processed
            if fullfilename in files_to_stage or fullfilename in files_to_ignore:
                fullfilename = filename = ''
                continue

        if not filename:
            continue

        # Check for changed translation 'msgid' or 'msgstr' strings.
        match = RE_CHANGED_TRANSLATION_LINE.match(line)
        if match:
            action = line[0]
            key = f"{action}{match.group(1)}"
            text = line[len(match.group(0)):-1]

            # Append to text from continuation lines.
            while line_num < line_count and str(git_diff[line_num]).strip() and str(git_diff[line_num]).startswith(f'{action}"'):
                text += str(git_diff[line_num]).strip()[2:-1]
                line_num += 1

            tx_strings[key].add(text)

            continue

        # Check for changed translation strings not starting with 'msgid' or 'msgstr'.
        # Note that changed sections of lines show removals before additions.
        match = RE_CHANGED_STRINGS_LINE.match(line)
        if match:
            minus = plus = ''
            action = line[0]
            text = line[len(match.group(0)):-1]

            # Append to text from continuation lines.
            while line_num < line_count and str(git_diff[line_num]).strip() and str(git_diff[line_num]).startswith(f'{action}"'):
                text += str(git_diff[line_num]).strip()[2:-1]
                line_num += 1

            if action == '-':
                minus = text
                text = ''
                action = '+'
                while line_num < line_count and str(git_diff[line_num]).strip() and str(git_diff[line_num]).startswith(f'{action}"'):
                    text += str(git_diff[line_num]).strip()[2:-1]
                    line_num += 1
                plus = text

            if plus != minus:
                files_to_stage[fullfilename] = 'Modified'
                reset_tx_strings(tx_strings)
                filename = fullfilename = ''

            minus = plus = ''

            continue

        # Check for changed location comment lines
        if RE_CHANGED_LOCATION_LINE.match(line):
            action = line[0]
            text = line.rsplit(':', maxsplit=1)[-1].strip()

            key = f"{action}location"
            tx_strings[key].add(text)

            continue

        # Add changed fuzzy comment lines
        if RE_CHANGED_FUZZY_LINE.match(line):
            files_to_stage[fullfilename] = 'Modified'
            reset_tx_strings(tx_strings)
            filename = fullfilename = ''

    # Handle any outstanding changes at the end of the git diff output
    do_process(tx_strings, filename, fullfilename, files_to_stage, files_to_ignore)


################################################################################

def main():
    """Main processing method.
    """
    args = parse_command_line()

    Printer.silent = args.silent

    if args.about:
        Printer.stdout(ABOUT_TEXT)
        sys.exit(0)

    if args.warranty:
        Printer.stdout(WARRANTY_TEXT)
        sys.exit(0)

    Printer.stdout(f"\n{DESCRIPTION}\n")

    files_to_ignore = set()
    files_to_stage = {}

    try:
        command = 'git status --porcelain'
        git_stat = get_stdout_from_command(command)
        if 'save_files' in vars(args):
            with open(STATUS_FILE, 'w', encoding='utf-8') as f:
                f.write(git_stat)
        git_stat = git_stat.splitlines()

        command = 'git diff --ignore-cr-at-eol'
        git_diff = get_stdout_from_command(command)
        if 'save_files' in vars(args):
            with open(DIFF_FILE, 'w', encoding='utf-8') as f:
                f.write(git_diff)
        git_diff = git_diff.splitlines()

    except subprocess.SubprocessError as ex:
        Printer.stderr(f"\nError running:{command}\nException: {ex}")
        sys.exit(1)

    Printer.stdout("Getting the list of translation files.")
    Printer.stdout(" - Parsing the git status output")
    parse_git_status(git_stat, files_to_stage, files_to_ignore, args.rst)

    Printer.stdout(" - Parsing the git diff output.")
    parse_git_diff(git_diff, files_to_stage, files_to_ignore)

    if files_to_stage:
        Printer.stdout("\nFiles to add to git staging:")
        for filename, action in files_to_stage.items():
            Printer.stdout(f' + "{filename}" [{action}]')
            if not args.dryrun:
                if subprocess.run(
                        f'git add "{filename}"',
                        shell=True,
                        check=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=COMMAND_TIMEOUT
                        ).returncode:
                    Printer.stderr(f"\nThere was a problem adding {filename} to the commit.\n")
                    sys.exit(1)
        Printer.stdout("\nNo files staged due to dry run option enabled.\n" if args.dryrun else '')
    else:
        Printer.stdout("\nNo files to stage for git.\n")

    sys.exit(0)


################################################################################

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Python script used to provide development support functions.
"""
# Copyright (C) 2020-2023 Bob Swift
# Copyright (C) 2021 Philipp Wolfer

# pylint: disable=too-many-lines
# pylint: disable=wrong-import-order

import argparse
import glob
import os
import re
import shutil
import subprocess
from subprocess import SubprocessError
import sys
import time
import zipfile

import conf
import tag_mapping

import restructuredtext_lint


SCRIPT_NAME = 'Picard Docs Builder'
SCRIPT_VERS = '0.18'
SCRIPT_COPYRIGHT = '2021-2023'
SCRIPT_AUTHOR = 'Bob Swift'

PACKAGE_NAME = 'picard-docs'
PACKAGE_TITLE = 'Picard Docs'

OUTPUT_DIR = 'docs'
BASE_FILE_NAME = conf.base_filename if hasattr(conf, 'base_filename') and conf.base_filename else 'musicbrainzpicard'
FILE_NAME_ROOT = 'MusicBrainz_Picard'
TAG_MAP_NAME = FILE_NAME_ROOT + '_Tag_Map'
CURRENT_VERSION = conf.version

######################
#   Linter Options   #
######################

IGNORE_INFO_MESSAGES = False
FAIL_ON_WARNINGS = True

PYTHON_FILES_TO_CHECK = [
    'setup.py',
    'conf.py',
    'tag_mapping.py',
    '_extensions/*.py',
    'gitstage.py',
]

#################################################################
#   Sphinx Directives and Roles to ignore while lint checking   #
#################################################################

IGNORE_DIRECTIVES = [
    # Table of Contents
    'toctree',

    # Paragraph Level Markup
    'note', 'warning', 'versionadded', 'versionchanged', 'deprecated',
    'seealso', 'rubic', 'centered', 'hlist',

    # Showing Code Examples
    'highlight', 'code-block', 'literalinclude',

    # Glossary
    'glossary',

    # Meta-information Markup
    'sectionauthor', 'codeauthor',

    # Index-generating Markup
    'index',

    # Including content based on tags
    'only',

    # Tables
    'tabularcolumns',

    # Math
    'math',

    # Grammar production displays
    'productionlist',

    # Command line parameter docs
    'option', 'describe',

    # Specialty directives
    'youtube',
]

IGNORE_ROLES = [
    # Cross-referencing
    'any', 'ref', 'doc', 'download', 'numref', 'envar', 'token',
    'keyword', 'option', 'term', 'index',

    # Math
    'math', 'eq',

    # Semantic Markup
    'abbr', 'command', 'dfn', 'file', 'guilabel', 'kbd', 'mailheader',
    'makevar', 'manpage', 'menuselection', 'mimetype', 'newsgroup',
    'program', 'regexp', 'samp', 'pep', 'rfc',
]

IGNORE_LEXERS = [
    'taggerscript',
]

################################################
#   RE Tests for Sphinx Roles and Directives   #
################################################

RE_TEST_DIRECTIVE_1 = re.compile(r'^No directive entry for "([^"]+)')
RE_TEST_DIRECTIVE_2 = re.compile(r'^.*directive type "([^"]+)".*$')
RE_TEST_DIRECTIVE_3 = re.compile(r'^.*No Pygments lexer found for "([^"]+)".*$')

RE_TEST_ROLE_1 = re.compile(r'^No role entry for "([^"]+)')
RE_TEST_ROLE_2 = re.compile(r'^.*role "([^"]+)".*$')

RE_TEST_LANGUAGE = re.compile(r'^[a-z]{2}(_[A-Z]([A-Z]{1}|[a-z]{3}){1})?$')

##################################################
#   Text to display when the script is started   #
##################################################

COPYRIGHT_TEXT = f"""\

{SCRIPT_NAME} (v{SCRIPT_VERS})  Copyright (C) {SCRIPT_COPYRIGHT}, {SCRIPT_AUTHOR}
"""

ABOUT_TEXT = f"""\
{COPYRIGHT_TEXT}
This program provides some utility functions to aid in the development
of the {PACKAGE_TITLE} package.

For usage instructions, please use the '--help' option.

This program comes with ABSOLUTELY NO WARRANTY; for details use command
'info warranty'.  This is free software, and you are welcome to redistribute
it under certain conditions.  Please see the GPLv3 license for details.
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

DESCRIPTION = f"{SCRIPT_NAME} (v{SCRIPT_VERS})"

HELP = f"""\
Usage: {os.path.basename(os.path.realpath(__file__))} [optional arguments] command [command args]

Commands:
   clean            Clean the specified target directory
   build            Build the specified target files
   test             Run the specified tests

   info about       Information about the script
   info warranty    Warranty information about the script
   info languages   Display list of supported languages

Optional Arguments:
  -l LANGUAGE       Specify language for processing
  -h, --help        Show this help message and exit
"""

########################################
#   Documentation Languages to Build   #
########################################

LANGUAGE_NAMES = {
    'bg': 'Bulgarian',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fi': 'Finnish',
    'fr': 'French',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'it': 'Italian',
    'ja': 'Japanese',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'nb': 'Norwegian (Bokmål)',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sv': 'Swedish',
    'tr': 'Turkish',
    'zh': 'Chinese',
}

LANGUAGE_LIST = {
    'en': 'English',
}
if conf.supported_languages:
    for code, title in conf.supported_languages:
        LANGUAGE_LIST[code] = LANGUAGE_NAMES[code[:2]] if code[:2] in LANGUAGE_NAMES else title

DEFAULT_LANGUAGE = conf.default_language if conf.default_language else 'en'
LANGUAGES = list(LANGUAGE_LIST.keys())


################################################
#   Custom exceptions used within the script   #
################################################

class CustomError(Exception):
    """Custom base exception for the script.
    """
    def __init__(self, message='Setup Script Error'):
        self.message = message
        super().__init__(self.message)


class CreateDirectoryError(CustomError):
    """Exception when creating a directory.
    """
    def __init__(self, message='Create Directory Error'):
        self.message = message
        super().__init__(self.message)


class CleanDirectoryError(CustomError):
    """Exception when cleaning a directory.
    """
    def __init__(self, message='Clean Directory Error'):
        self.message = message
        super().__init__(self.message)


class RemoveDirectoryError(CustomError):
    """Exception when removing a directory.
    """
    def __init__(self, message='Remove Directory Error'):
        self.message = message
        super().__init__(self.message)


class RemoveFileError(CustomError):
    """Exception when removing a file.
    """
    def __init__(self, message='Remove File Error'):
        self.message = message
        super().__init__(self.message)


class ErrorLintRST():   # pylint: disable=too-few-public-methods
    """Special LintRST error for unhandled exceptions.
    """
    def __init__(self, err_type='INFO', err_line=0, err_message=''):
        self.type = err_type
        self.line = err_line
        self.message = err_message


class SPHINX_():        # pylint: disable=too-few-public-methods
    """Sphinx constants used when building the documentation.
    """
    OPTS = ''
    BUILD = 'sphinx-build'
    INTL = 'sphinx-intl'
    BUILD_DIR = '_build'
    SOURCE_DIR = '.'
    LOCALE_DIR = conf.locale_dirs[0] if conf.locale_dirs else '_locale'
    GETTEXT_DIR = os.path.join(LOCALE_DIR, 'gettext')
    BUILD_TIMEOUT = 300
    BUILD_TARGETS = {
        'html': {'dir': 'html', 'cmd': 'html', 'extra': ''},
        'epub': {'dir': 'epub', 'cmd': 'epub', 'extra': '-D master_doc=epub'},
        'pdf': {'dir': 'latex', 'cmd': 'latex', 'extra': ''},
    }


def exit_with_code(exit_code=0):
    """Print and exit with the specified exit code.

    Keyword Arguments:
        exit_code {int} -- Exit code to use (default: 0)
    """
    print(f'\nExit Code: {exit_code}\n')
    sys.exit(exit_code)


def python_files_to_check():
    """Provide expanded list of python files to check.

    Yields:
        str: Path and name of file.
    """
    for filepath in PYTHON_FILES_TO_CHECK:
        for filename in glob.glob(filepath, recursive=True):
            yield filename


class LintRST():
    """Lint the restructured text (RST) files.
    """
    def __init__(self):
        """Provides an instance of the "restructuredtext-lint" linter.
        """
        self.checked_count = 0
        self.warning_count = 0
        self.error_count = 0
        self.info_count = 0
        self.untested = 0
        self.linter = restructuredtext_lint

    def process_error(self, err):
        """Print the error information and increment the appropriate error counter.

        Args:
            err (restructuredtext_lint error): Restructured text linter error object.
        """
        print(f'\n   [{err.type}] Line {err.line}: {err.message}', end='', flush=True)
        if err.type == 'WARNING':
            self.warning_count += 1
        elif err.type == 'INFO':
            self.info_count += 1
        elif err.type == 'UNTESTED':
            self.untested += 1
        else:
            # Includes 'ERROR' and 'SEVERE'
            self.error_count += 1

    def check_file(self, file_name, ignore_info=True):  # pylint: disable=too-many-branches
        """Lint check the specified file, printing the findings to the console.

        Arguments:
            file_name {str} -- Path and name of the file to check

        Keyword Arguments:
            ignore_info {bool} -- Determines whether INFO notices should be ignored (default: {True})
        """
        print(f"{' ' * 79}\r{file_name}", end='', flush=True)
        self.checked_count += 1
        if not os.path.isfile(file_name):
            self.process_error(ErrorLintRST('ERROR', 0, 'File not found'))
            return

        try:
            err_processed = False
            errs = self.linter.lint_file(file_name)
            if not errs:
                errs = []
            for err in errs:
                err_process = True
                if err.type == 'INFO':
                    if ignore_info:
                        # Ignore this error message and continue testing
                        continue
                    m = RE_TEST_DIRECTIVE_1.match(err.message)
                    if m and m.group(1) in IGNORE_DIRECTIVES:
                        continue
                    m = RE_TEST_ROLE_1.match(err.message)
                    if m and m.group(1) in IGNORE_ROLES:
                        continue
                elif err.type == 'WARNING':
                    m = RE_TEST_DIRECTIVE_3.match(err.message)
                    if m and m.group(1) in IGNORE_LEXERS:
                        continue
                elif err.type in {'ERROR', 'SEVERE'}:
                    m = RE_TEST_DIRECTIVE_2.match(err.message)
                    if m and m.group(1) in IGNORE_DIRECTIVES:
                        continue
                    m = RE_TEST_ROLE_2.match(err.message)
                    if m and m.group(1) in IGNORE_ROLES:
                        continue
                if err_process:
                    err_processed = True
                    self.process_error(err)
            print('\n\n' if err_processed else f"\r{' ' * 79}\r", end='', flush=True)
        except UnicodeDecodeError:
            err = ErrorLintRST('UNTESTED', 0, 'Unable to check because of unmapped unicode characters.\n')
            self.process_error(err)
        except IOError as ex:
            self.process_error(ErrorLintRST('ERROR', 0, f'Error reading file. ({ex})'))

    def check(self, root_dir, ignore_info=False, fail_on_warnings=False):
        """Check all files in the specified directory, including files in subdirectories.

        Arguments:
            root_dir {str} -- Path to the root directory to check

        Keyword Arguments:
            ignore_info {bool} -- Determines whether INFO notices should be ignored (default: {False})
            fail_on_warnings {bool} -- Determines whether warnings will cause the check to return a failed status (default: {False})

        Returns:
            {int} -- Error code 1 if check failed, otherwise 0.
        """
        for dir_name, subdir_list, file_list in os.walk(root_dir):  # pylint: disable=unused-variable
            for fname in file_list:
                if str(fname).lower().endswith('.rst'):
                    self.check_file(os.path.join(dir_name, fname), ignore_info)

        text = (
            f'Checked {self.checked_count:,} files.  '
            f'Errors: {self.error_count:,}  '
            f'Warnings: {self.warning_count:,}  '
            f'Untested: {self.untested:,}  '
        ) + ('' if ignore_info else f'Info: {self.info_count:,}')
        print(f"{text.strip()}")

        err = self.error_count + (self.warning_count if fail_on_warnings else 0)
        return 1 if err > 0 else 0


##############################################################################

class POCheck():
    """Check for restructured text errors in the translation *.po files.
    """
    def __init__(self):
        """Provides an instance of the "POCheck" class.
        """
        self.warning_count = 0
        self.file_count = 0
        self.line_count = 0
        self.bad_files = []
        self.filename = ''
        self.filename_written = False

    def get_lines(self, file_lines):
        """Assemble the content into full lines for testing.

        Args:
            file_lines (list): List of the lines read from the *.po file

        Returns:
            dict: Dictionary of assembled lines by starting line number in the file.
        """
        tx_lines = {}
        line_number = 0
        build_line = False
        temp_line_text = ''
        temp_line_number = 0
        for file_line in file_lines:
            line_number += 1
            if build_line:
                if re.match(r'^".*"$', file_line):
                    temp_line_text += file_line[1:-2]
                else:
                    tx_lines[temp_line_number] = temp_line_text
                    build_line = False
            if file_line and not build_line:
                if re.match(r'^(msgid|msgstr)', file_line):
                    temp_line_number = line_number
                    temp_line_text = ''
                    build_line = True
        if build_line:  # Catch case where line ends on the last line of a msgstr entry
            tx_lines[temp_line_number] = temp_line_text
        self.line_count += len(tx_lines)
        return tx_lines

    def write_warning(self, message):
        """Add message to file processing output.

        Args:
            message (str): Message to add
        """
        if not self.filename_written:
            self.bad_files.append('')
            self.bad_files.append(f'File: {self.filename}')
            self.filename_written = True
        self.warning_count += 1
        self.bad_files.append('  ' + message)

    def check_line(self, line_number, content):     # pylint: disable=too-many-branches
        """Check the line for restructured-text errors.

        Args:
            filename (str): Full path of the file being checked
            line_number (int): Line number of the start of the assembled line
            content (str): The assembled line to check
        """
        if re.search(r"`[^`_]+`\s+_", content) or re.search(r"`[^`']*'\s*_", content):
            self.write_warning(f'[L{line_number}]: Link')
        for item in IGNORE_DIRECTIVES:
            if re.search(r"\.\.\s+" + item + r"\s+::", content):
                self.write_warning(f'[L{line_number}]: Directive "{item}"')
        for item in IGNORE_ROLES:
            if re.search(r":\s+" + item + r":", content) \
               or re.search(r":" + item + r"\s+:", content) \
               or re.search(r":" + item + r":\s+`", content) \
               or re.search(r"[^\:]+" + item + r":`", content):
                self.write_warning(f'[L{line_number}]: Role "{item}"')
        links = re.findall(r"`([^`]*)`_", content)
        for item in ['doc', 'download', 'numref', 'ref']:
            links.extend(re.findall(r":" + item + r":`([^`]*)`", content))
        for item in links:
            if (
                item.count('<') != item.count('>')
                or '<>' in item
                or re.search(r"\S<", ' ' + item)
                or re.search(r"<\S*\s+.*>", item)
            ):
                self.write_warning(f'[L{line_number}]: Link "{item}"')
        indices = re.findall(r":index:`[^<]*<([^>]*)>", content)
        for item in indices:
            if re.search(r"\s+(,|;)", item):
                self.write_warning(f'[L{line_number}]: Index "{item}"')
        backticks = content.count('`') % 2
        if backticks:
            self.write_warning(f'[L{line_number}]: Backtick Mismatch')
            return
        backticks_open = False
        lastchar = ''
        nextchar = ''
        ccount = 0
        for char in content:
            ccount += 1
            if char == '`':
                backticks_open = not backticks_open
                nextchar = content[ccount] if len(content) > ccount else ''
                if backticks_open:
                    # if lastchar and lastchar not in ' :"\'' and nextchar and nextchar != '`':
                    if lastchar and nextchar and nextchar != '`' and re.search(r"[a-zA-Z0-9]+", lastchar):
                        self.write_warning(f'[L{line_number},C{ccount}]: Backtick Open "{lastchar + char + nextchar}"')
                        break
                else:
                    if lastchar != '`' and nextchar and re.search(r"[a-zA-Z0-9]+", nextchar):
                        self.write_warning(f' [L{line_number},C{ccount}]: Backtick Close "{lastchar + char + nextchar}"')
                        break
            lastchar = char

    def check(self, locale_dir, filetype='po'):
        """Check all translation *.po files in the specified directory and subdirectories.
        """
        if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
            return
        print(f"\nTesting restructured-text in *.po files.\nStarting root directory: {locale_dir}\n")
        if os.path.isdir(locale_dir):
            for dir_name, _subdir_list, file_list in os.walk(locale_dir):
                for file_name in file_list:
                    if re.match(r'.*\.' + filetype + '$', file_name, re.IGNORECASE):
                        self.file_count += 1
                        filename = os.path.join(dir_name, file_name)
                        self.filename_written = False
                        print(f"{(filename + ' ' * 80)[:79]}\r", end='', flush=True)
                        self.filename = filename
                        content = {}
                        with open(filename, 'r', encoding='utf8') as f:
                            content = self.get_lines(f.readlines())
                        for key in sorted(content):
                            self.check_line(key, content[key])
            print(' ' * 79 + '\r', end='', flush=True)
        print(f"Checked {self.line_count:,} lines in {self.file_count:,} files.  Found {self.warning_count:,} issues to check.")
        if self.bad_files:
            print("\nCheck the following for errors:")
            for item in self.bad_files:
                print(item)
        # print()
        if self.warning_count:
            exit_with_code(1 if self.warning_count else 0)


def show_help():
    """Print the help screen.
    """
    print(f"\n{HELP}")


def parse_command_line():
    """Parse the command line arguments.
    """
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)

    arg_parser.add_argument(
        '-l', '--language',
        action='store',
        nargs='?',
        default='en',
        const='en',
        metavar='LANGUAGE',
        dest='language',
        help="specify language for processing"
    )

    subparsers = arg_parser.add_subparsers()

    parser01 = subparsers.add_parser(
        'test',
        help='Test the files'
    )

    parser01.add_argument(
        'test_targets',
        action='store',
        nargs='+',
        type=str,
        choices=['rst', 'sphinx', 'po', 'flake8', 'pylint', 'isort', 'python'],
        help="rst = lint check the rst files, "
             "sphinx = test build of the *.rst files "
             "po = rudimentary test of RST in *.po files "
             "flake8 = test python files with flake8, "
             "pylint = test python files with pylint, "
             "isort = check python files import sorting, "
             "python = all python tests (isort, flake8 and pylint)"
    )

    parser02 = subparsers.add_parser(
        'build',
        help='Build the files'
    )

    parser02.add_argument(
        'build_targets',
        action='store',
        nargs='+',
        choices=['map', 'pot', 'po', 'html', 'pdf', 'epub', 'all'],
        help="map = build tag map files, "
             "pot = build translation template files, "
             "po = build translation files, "
             "html = build html files, "
             "pdf = build pdf file, "
             "epub = build epub file, "
             "all = build all files"
    )

    parser03 = subparsers.add_parser(
        'clean',
        help='Reset the build directories'
    )

    parser03.add_argument(
        'clean_targets',
        action='store',
        nargs='+',
        choices=['mo', 'html', 'pdf', 'epub', 'all'],
        help="mo = remove all compiled MO files, "
             "html = clean html build directory, "
             "pdf = clean pdf build directory, "
             "epub = clean epub build directory, "
             "all = clean all build targets"
    )

    parser04 = subparsers.add_parser(
        'info',
        help='Display project information'
    )

    parser04.add_argument(
        'info_type',
        action='store',
        choices=['about', 'languages', 'warranty'],
        help="about = info about the script, "
             "languages = list of supported languages, "
             "warranty = warranty of the script"
    )

    args = arg_parser.parse_args()
    return args


def run_sphinx_test(language=''):
    """Perform a trial build using Sphinx with all warnings enabled.
    """
    print('\nSphinx test build.\n')
    if not (language and language in LANGUAGES):
        language = DEFAULT_LANGUAGE
    if language == DEFAULT_LANGUAGE:
        language_option = ''
    else:
        language_option = '-D language=' + language
        # update_po_files_for_language(language)
    junk_dir = '_junk'
    command = f"{SPHINX_.BUILD} -b dummy -W --keep-going {SPHINX_.SOURCE_DIR} {junk_dir} {language_option}".strip().replace('  ', ' ')
    exit_code = subprocess.run(command, shell=True, check=False, capture_output=False, timeout=SPHINX_.BUILD_TIMEOUT).returncode
    remove_dir(junk_dir)
    if exit_code:
        exit_with_code(exit_code)
    print()


def run_lint(root_dir, ignore_info=False, fail_on_warnings=False):
    """Check the RST files in the specified directory and subdirectories.

    Arguments:
        root_dir {str} -- Path to the root directory to check

    Keyword Arguments:
        ignore_info {bool} -- Determines whether INFO notices should be ignored (default: {False})
        fail_on_warnings {bool} -- Determines whether warnings will cause the check to return a failed status (default: {False})
    """
    # # ---------------------------------------------------------------------
    # # Example code from https://pypi.org/project/restructuredtext-lint/
    # # Load in our dependencies
    # from docutils.parsers.rst.directives import register_directive
    # from sphinx.directives.code import Highlight
    # import restructuredtext_lint
    #
    # # Load our new directive
    # register_directive('highlight', Highlight)
    #
    # # Lint our README
    # errors = restructuredtext_lint.lint_file('docs/sphinx/README.rst')
    # print errors[0].message # Error in "highlight" directive: no content permitted.
    # # ---------------------------------------------------------------------

    print(f'\nLint checking all RST files starting in the "{root_dir}" directory.\n')
    linter = LintRST()
    err = linter.check(root_dir, ignore_info, fail_on_warnings)
    exit_code = 1 if err > 0 else 0
    if exit_code:
        exit_with_code(exit_code)


def run_pylint():
    """Check the Python code using pylint.
    """
    print("\nChecking the python files with pylint.\n")
    exit_code = 0
    for filename in python_files_to_check():
        print(f'pylint: {filename}', end='', flush=True)
        command = f'pylint {filename}'
        result = subprocess.run(command, shell=True, check=False, capture_output=True, timeout=SPHINX_.BUILD_TIMEOUT)
        exit_code = max(exit_code, result.returncode)
        text = ['[Error]']
        text.extend(result.stdout.decode('utf-8').splitlines()[:-4])
        text = ('\n'.join(text) + '\n') if result.returncode else '[Okay]'
        print(f"  {text}")
    if exit_code:
        exit_with_code(exit_code)


def run_flake8():
    """Check the Python code using flake8.
    """
    print("\nChecking the python files with flake8.\n")
    exit_code = 0
    for filename in python_files_to_check():
        print(f'flake8: {filename}', end='', flush=True)
        command = f'flake8 {filename}'
        result = subprocess.run(command, shell=True, check=False, capture_output=True, timeout=SPHINX_.BUILD_TIMEOUT)
        exit_code = max(exit_code, result.returncode)
        text = ['[Error]']
        text.extend(result.stdout.decode('utf-8').splitlines()[:-1])
        text = ('\n'.join(text) + '\n') if result.returncode else '[Okay]'
        print(f"  {text}")
    if exit_code:
        exit_with_code(exit_code)


def run_isort():
    """Check the Python code using isort.
    """
    print("\nChecking the python files with isort.\n")
    exit_code = 0
    for filename in python_files_to_check():
        print(f'isort: {filename}', end='', flush=True)
        command = f'isort -c {filename}'
        result = subprocess.run(command, shell=True, check=False, capture_output=True, timeout=SPHINX_.BUILD_TIMEOUT)
        print(('\n' + result.stderr.decode('utf-8').strip() + '\n') if result.returncode else '  [Okay]')
        exit_code = max(exit_code, result.returncode)
    if exit_code:
        exit_with_code(exit_code)


def get_major_minor(version):
    """Extract the major.minor portion of the supplied version string.

    Args:
        version (str): Version string to process

    Returns:
        str: Major.minor portion of the version string, or '' if invalid version
    """
    if re.match(r'^(v?[0-9][0-9\.]*)', version):
        parts = re.match(r'^v?([0-9][0-9\.]*)', version).group(1).split('.')
        parts.append('')
        return f"{int('0' + parts[0])}.{int('0' + parts[1])}"
    return ''


def create_directory(dir_path, dir_name):
    """If the specified directory does not exist, it will be created.  Includes multiple
    checks for success to accommodate race condition in Windows.

    Arguments:
        dir_path {str} -- Path to the directory to create
        dir_name {str} -- Name of the directory type (e.g.: 'html')
    """
    if not os.path.exists(dir_path):
        try:
            print(f'Creating the {dir_name} directory: {dir_path}')
            os.makedirs(dir_path)
            counter = 50
            # Multiple checks for success to accommodate race condition in Windows
            while counter and not os.path.exists(dir_path):
                counter -= 1
                time.sleep(.2)
            if not counter:
                raise CreateDirectoryError
        except (CustomError, OSError) as ex:
            print(f"\nError creating the {dir_name} directory: {dir_path}")
            print(f"Error message: {ex}\n")
            exit_with_code(1)


def clean_directory(dir_path, dir_name, create_dir=True):
    """Removes all files and subdirectories for the specified directory.  If the specified
    directory does not exist, it will be created.  Includes multiple checks for success to
    accommodate race condition in Windows.

    Arguments:
        dir_path {str} -- Path to the directory to clean
        dir_name {str} -- Name of the directory type (e.g.: 'html')
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            print(f'Emptying the {dir_name} directory: {dir_path}')
            if not os.listdir(dir_path):
                return
            err = None
            tries = 5
            while tries > 0:
                tries -= 1
                err = None
                if os.path.exists(dir_path):
                    try:
                        shutil.rmtree(dir_path)
                    except (shutil.Error, PermissionError, OSError) as ex:
                        err = ex
                        time.sleep(.2)
                        continue
                    # Multiple checks for success to accommodate race condition in Windows
                    counter = 50
                    while counter and os.path.exists(dir_path):
                        counter -= 1
                        time.sleep(.2)
                    if not counter:
                        err = CleanDirectoryError()
                        continue
                tries = 0
            if err:
                print(f"\nError removing the {dir_name} directory: {dir_path}")
                print(f"Error message: {err}\n")
                exit_with_code(1)
        else:
            print(f"\nThe {dir_name} directory is not a directory: {dir_path}\n")
            exit_with_code(1)
    if create_dir and not os.path.exists(dir_path):
        create_directory(dir_path=dir_path, dir_name=dir_name)


def remove_dir(dir_path):
    """Remove the specified directory.  Includes multiple checks for success to accommodate race
    condition in Windows.

    Arguments:
        dir_path {str} -- Path of directory to remove
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            clean_directory(dir_path, 'temporary build', create_dir=False)
            err = None
            tries = 5
            while tries > 0:
                tries -= 1
                err = None
                if os.path.exists(dir_path):
                    try:
                        os.rmdir(dir_path)
                    except (shutil.Error, PermissionError) as ex:
                        err = ex
                        time.sleep(.2)
                        continue
                    counter = 50
                    # Multiple checks for success to accommodate race condition in Windows
                    while counter and os.path.exists(dir_path):
                        counter -= 1
                        time.sleep(.2)
                    if not counter:
                        err = RemoveDirectoryError()
                        continue
                tries = 0
            if err:
                print(f"\nError removing the directory: {dir_path}")
                print(f"Error message: {err}\n")
                exit_with_code(1)
        else:
            print(f'\nUnable to remove (not a directory): {dir_path}\n')
            exit_with_code(1)


def remove_file(file_path):
    """Removes the specified file.  Includes multiple checks for success to accommodate race
    condition in Windows.

    Arguments:
        file_path {str} -- File to remove.
    """
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            err = None
            tries = 5
            while tries > 0:
                tries -= 1
                err = None
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                    except (shutil.Error, PermissionError) as ex:
                        err = ex
                        time.sleep(.2)
                        continue
                    counter = 50
                    # Multiple checks for success to accommodate race condition in Windows
                    while counter and os.path.exists(file_path):
                        counter -= 1
                        time.sleep(.2)
                    if not counter:
                        err = RemoveFileError()
                        continue
                tries = 0
            if err:
                print(f"\nError removing the file: {file_path}")
                print(f"Error message: {err}\n")
                exit_with_code(1)
        else:
            print(f'\nUnable to remove (not a file): {file_path}\n')
            exit_with_code(1)


def save_version_info():
    """Save version and language information to a __init__.py file in the docs directory
    so that it can be imported and used in the publish.py script.  This is used to create
    index.html files for use in the top and version directories, as well as the
    version_links.js file to provide the list of selectable versions in the options section
    of each web page.
    """
    create_directory(OUTPUT_DIR, 'Output')
    file_name = os.path.join(OUTPUT_DIR, '__init__.py')
    remove_file(file_name)
    print(f"Saving: {file_name}")
    with open(file_name, 'w', encoding='utf8') as ofile:
        ofile.write(
            "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n"
            '"""Version and Language information used for publishing the documentation.\n"""\n\n'
            "# This file is automatically generated.\n\n"
            f"VERSION = {repr(conf.version)}\n"
            f"DEFAULT_LANGUAGE = {repr(DEFAULT_LANGUAGE)}\n"
            f"LANGUAGES = {repr(LANGUAGES)}\n\n"
            f"FILE_NAME_ROOT = {repr(FILE_NAME_ROOT)}\n"
            f"TAG_MAP_NAME = {repr(TAG_MAP_NAME)}\n"
        )


def run_command(command):
    """Executes a command in a subprocess.

    Args:
        command (str): Command to execute, including all command line parameters.
    """
    print(f'\nExecuting command: {command}\n')
    try:
        exit_code = subprocess.run(command, shell=True, check=True, capture_output=False, timeout=SPHINX_.BUILD_TIMEOUT).returncode
    except (SubprocessError, FileNotFoundError, OSError) as ex:
        print(f"ERROR executing process: {ex}")
        exit_code = 1
    if exit_code:
        exit_with_code(exit_code)


def do_build(target=None, language='', clean=False):
    """Perform the specified build operation.

    Args:
        target (str, optional): Type of build target to use. Defaults to None.
        language (str, optional): Language code to use for the build. If not specified, the default language is used.
        clean (bool, optional): Signals whether the build directory should be emptied before starting the build. Defaults to False.
    """
    if not (target and target in SPHINX_.BUILD_TARGETS):
        print(f"\nUnknown build target: {target}")
        exit_with_code(1)
    print(f"\nBuilding target: {target}")
    if not (language and language in LANGUAGES):
        language = DEFAULT_LANGUAGE
    if language == DEFAULT_LANGUAGE:
        language_option = ''
    else:
        language_option = '-D language=' + language
        # update_po_files_for_language(language)

    if clean:
        clean_dir = os.path.join(SPHINX_.BUILD_DIR, SPHINX_.BUILD_TARGETS[target]['dir'])
        print(f'\nCleaning build directory: {clean_dir}')
        clean_directory(clean_dir, target)

    command = (
        f"{SPHINX_.BUILD} -M {SPHINX_.BUILD_TARGETS[target]['cmd']} "
        f"{SPHINX_.SOURCE_DIR} {SPHINX_.BUILD_DIR} -c . "
        f"{SPHINX_.BUILD_TARGETS[target]['extra']} {language_option}"
    ).strip().replace('  ', ' ')
    run_command(command)

    if target == 'html':
        # Additional HTML processing
        build_html(language=language)

    elif target == 'pdf':
        # Additional PDF processing
        build_pdf(language=language)

    elif target == 'epub':
        # Additional EPUB processing
        build_epub(language=language)


def build_html(language=''):
    """Build post processing specific to HTML files.

    Keyword Arguments:
        language {str} -- Language to use for the build (default: {''})

    Raises:
        Exception: Files not copied
    """
    output_dir = os.path.join(OUTPUT_DIR, language)
    html_dir = os.path.join(SPHINX_.BUILD_DIR, SPHINX_.BUILD_TARGETS['html']['dir'])
    clean_directory(output_dir, 'html')
    print(f'Copying HTML files to document directory: {output_dir}')
    try:
        remove_dir(output_dir)
        shutil.copytree(html_dir, output_dir)
        counter = 50
        # Multiple checks for success to accommodate race condition in Windows
        while counter and not os.path.exists(output_dir):
            counter -= 1
            time.sleep(.2)
        if not counter:
            raise CreateDirectoryError
    except (CreateDirectoryError, shutil.Error) as ex:
        print(f'Files not copied.  Error: {ex}')
        exit_with_code(1)

    zip_file = os.path.join(OUTPUT_DIR, f'{FILE_NAME_ROOT}_v{get_major_minor(CURRENT_VERSION)}_HTML_[{language}].zip')
    print(f'Removing old ZIP file: {zip_file}')
    remove_file(zip_file)
    print(f'Copying HTML to ZIP file: {zip_file}')
    current_dir = os.getcwd()

    try:
        with zipfile.ZipFile(zip_file, 'w') as myzip:
            os.chdir(output_dir)
            for dir_name, _subdir_list, file_list in os.walk('.'):
                for fname in file_list:
                    f_name = os.path.join(dir_name, fname)
                    myzip.write(f_name)
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as ex:
        print(f'Error creating ZIP file.  Error: {ex}')
        os.chdir(current_dir)
        exit_with_code(1)
    os.chdir(current_dir)


def build_pdf(language=''):
    """Build post processing specific to PDF files.

    Keyword Arguments:
        language {str} -- Language to use for the build (default: {''})
    """
    save_dir = os.getcwd()
    os.chdir(os.path.join(SPHINX_.BUILD_DIR, 'latex'))
    build_pdf_command = f'lualatex {BASE_FILE_NAME}'
    print('\nBuilding PDF output - First Pass')
    run_command(build_pdf_command)
    make_index_command = f"makeindex -s python.ist {BASE_FILE_NAME}"
    print('\nBuilding PDF output - Building Index')
    run_command(make_index_command)
    print('\nBuilding PDF output - Second Pass')
    run_command(build_pdf_command)
    os.chdir(save_dir)

    try:
        pdf_file = os.path.join(SPHINX_.BUILD_DIR, 'latex', BASE_FILE_NAME + '.pdf')
        target_file = os.path.join(OUTPUT_DIR, f'{FILE_NAME_ROOT}_v{get_major_minor(CURRENT_VERSION)}_[{language}].pdf')
        # Multiple checks if file exists to accommodate race condition in Windows
        counter = 50
        while counter and not os.path.exists(pdf_file):
            counter -= 1
            time.sleep(.2)
        if not counter:
            raise FileNotFoundError
    except (FileNotFoundError, OSError) as ex:
        print(f'Error building PDF file.  Error: {ex}')
        exit_with_code(1)
    print(f'Copying output to: {target_file}\n')
    try:
        shutil.copyfile(pdf_file, target_file)
    except (shutil.Error, OSError) as ex:
        print(f'Error copying PDF file.  Error: {ex}')
        exit_with_code(1)


def build_epub(language=''):
    """Build post processing specific to ePub files.

    Keyword Arguments:
        language {str} -- Language to use for the build (default: {''})
    """
    epub_file = os.path.join(SPHINX_.BUILD_DIR, SPHINX_.BUILD_TARGETS['epub']['dir'], BASE_FILE_NAME + '.epub')
    target_file = os.path.join(OUTPUT_DIR, f'{FILE_NAME_ROOT}_v{get_major_minor(CURRENT_VERSION)}_[{language}].epub')
    print(f'Copying output to: {target_file}\n')
    try:
        shutil.copyfile(epub_file, target_file)
    except (shutil.Error, OSError) as ex:
        print(f'Error copying epub file.  Error: {ex}')
        exit_with_code(1)


def build_pot():
    """Build the current 'gettext' language translation files and updates the *.po files for
    the supported languages.
    """
    command = ' '.join([SPHINX_.BUILD, '-b', 'gettext', SPHINX_.SOURCE_DIR, SPHINX_.LOCALE_DIR + '/gettext', '-c .'])
    print(f'Extracting POT files with command: {command}\n')
    exit_code = subprocess.run(command, shell=True, check=True, capture_output=False, timeout=SPHINX_.BUILD_TIMEOUT).returncode
    if exit_code:
        exit_with_code(exit_code)


def build_map():
    """Build the tag mapping files.
    """
    create_directory(OUTPUT_DIR, 'Output Documents')

    filename = os.path.join(OUTPUT_DIR, TAG_MAP_NAME + '.html')
    print(f'\nWriting HTML mapping file: {filename}')
    tag_mapping.write_html(filename)

    filename = os.path.join(OUTPUT_DIR, TAG_MAP_NAME + '.xlsx')
    print(f'Writing mapping spreadsheet file: {filename}')
    tag_mapping.write_spreadsheet(filename)

    filename = os.path.join(SPHINX_.SOURCE_DIR, 'appendices', 'tag_mapping.rst')
    print(f'Writing RST mapping file: {filename}')
    tag_mapping.write_rst(filename)


def clean_mo():
    """Delete all compiled translation files (*.mo) from the gettext directory and subdirectories.
    """
    print('Deleting compiled translation *.mo files.')
    count = 0
    # get a recursive list of file paths including sub directories that matches pattern
    gettext_path = os.path.join(SPHINX_.LOCALE_DIR, '**', '*.mo')
    filelist = glob.glob(gettext_path, recursive=True)

    # Iterate over the list of filepaths and remove each file.
    for filepath in filelist:
        try:
            os.remove(filepath)
            count += 1
        except OSError as ex:
            print(f"Error deleting file: {filepath}\nException: {ex}")
            exit_with_code(1)
    print(f'Removed {count} files.')


def check_language(language, supported_only=False):
    """Checks that the specified language is a valid language code.

    Args:
        language (str): Language code to check.
        supported_only (bool, optional): Validates the specified language against the list of supported language codes only. Defaults to False.

    Returns:
        bool: True if the language code is valid, otherwise False.
    """
    if language and isinstance(language, str):
        if RE_TEST_LANGUAGE.match(language):
            if (not supported_only) or language in LANGUAGE_LIST:
                return True
    return False


def get_languages():
    """Helper function to get list of po languages from directories.
    """
    dirlist = []
    for lang_dir in next(os.walk(SPHINX_.LOCALE_DIR))[1]:
        testdir = os.path.join(SPHINX_.LOCALE_DIR, lang_dir, 'LC_MESSAGES')
        if os.path.exists(testdir) and os.path.isdir(testdir):
            dirlist.append(lang_dir)
    return dirlist


def list_languages():
    """List the supported language options.
    """
    for lang_id, lang_name in LANGUAGE_LIST.items():
        print(f'   {lang_id} - {lang_name}')
    print("or 'all' to process all supported languages.\n")


def update_po(language, filegroup, filename):
    """Updates the specified po file.

    Args:
        language (str): Language to update
        filegroup (str): Topic group directory
        filename (str): File name (without extension) to update
    """
    print(f'{language}: {os.path.join(filegroup, filename)}', end='', flush=True)

    pot_file = os.path.join(SPHINX_.GETTEXT_DIR, filegroup, filename) + '.pot'
    po_file = os.path.join(SPHINX_.LOCALE_DIR, language, 'LC_MESSAGES', filegroup, filename) + '.po'
    if not os.path.exists(po_file):
        po_dir = os.path.split(po_file)[0]
        if not os.path.exists(po_dir):
            os.makedirs(po_dir)
        shutil.copyfile(pot_file, po_file)

    command = f"msgmerge --update --backup=none --lang={language} {po_file} {pot_file}"
    try:
        results = subprocess.run(command, shell=True, check=True, capture_output=True, timeout=SPHINX_.BUILD_TIMEOUT)
        exit_code = results.returncode
        if results.stdout.strip():
            print(f"{results.stdout.decode('utf-8').strip()}")
        if results.stderr.strip():
            print(f"{results.stderr.decode('utf-8').strip()}")
    except (SubprocessError, FileNotFoundError, OSError) as ex:
        print(f"\nERROR executing process: {ex}")
        exit_code = 1
    if exit_code:
        exit_with_code(exit_code)


def update_po_files_for_language(language):
    """Update the po files for the specified language.

    Args:
        language (str): Language code to update
    """
    short_lang = language[:2]
    lang_title = LANGUAGE_NAMES[short_lang] if short_lang in LANGUAGE_NAMES else 'Unknown Language'
    print(f"\n\nUpdating the {lang_title} ({language}) files.\n")

    # Check if `msgmerge` is available
    command = "msgmerge --version"
    try:
        use_msgmerge = not subprocess.run(command, shell=True, check=True, capture_output=True, timeout=SPHINX_.BUILD_TIMEOUT).returncode
    except (SubprocessError, FileNotFoundError, OSError):
        use_msgmerge = False

    if use_msgmerge:
        # `msgmerge` is available so use it as the preferred po file updater
        for dirpath, _dirnames, filenames in os.walk(SPHINX_.GETTEXT_DIR):
            filegroup = '' if dirpath == SPHINX_.GETTEXT_DIR else dirpath.split(os.path.sep)[-1]
            for filename in filenames:
                if not filename.endswith('.pot'):
                    continue
                fileroot = filename[:-4]
                update_po(language, filegroup, fileroot)

    else:
        # `msgmerge` is not available so use the fallback `sphinx-intl` po file updater
        command = ' '.join([SPHINX_.INTL, 'update', '-p', SPHINX_.GETTEXT_DIR, '-l', language])
        exit_code = subprocess.run(command, shell=True, timeout=SPHINX_.BUILD_TIMEOUT, check=True).returncode
        if exit_code:
            exit_with_code(exit_code)


def build_all_po_files():
    """Helper function to build all language po files.
    """
    print('\nUpdating PO files for other languages.')
    for language in sorted(get_languages()):
        update_po_files_for_language(language)


def main():
    """Main part of script to execute.
    """
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements

    args = parse_command_line()

    if 'language' in vars(args):
        if args.language == 'all':
            process_languages = LANGUAGES
        elif check_language(args.language):
            process_languages = [args.language]
        else:
            print(f'\nInvalid language selected: {args.language}')
            if not ('build_target' in vars(args) and (args.build_target == 'po')):
                print('\nPlease select from:')
                list_languages()
            exit_with_code(1)
    else:
        process_languages = [DEFAULT_LANGUAGE]

    if 'info_type' in vars(args):
        if args.info_type == 'about':
            print(ABOUT_TEXT)
            sys.exit(0)

        elif args.info_type == 'warranty':
            print(WARRANTY_TEXT)
            sys.exit(0)

        elif args.info_type == 'languages':
            print('\nSupported languages are:')
            list_languages()
            sys.exit(0)

        else:
            print(f"\nUnknown info type: '{args.info_type}'\n")
            exit_with_code(1)

    elif 'build_targets' in vars(args):
        for target in args.build_targets:
            if target in SPHINX_.BUILD_TARGETS:
                save_version_info()
                for lang in process_languages:
                    do_build(target=target, language=lang, clean=True)

            elif target == 'map':
                build_map()
                # build_all_po_files()

            elif target == 'po':
                build_all_po_files()

            elif target == 'pot':
                build_pot()
                build_all_po_files()
                # checker = POCheck()
                # checker.check(SPHINX_.LOCALE_DIR)

            elif target == 'all':
                save_version_info()
                build_map()
                build_pot()
                clean_mo()
                build_all_po_files()
                for build_target in SPHINX_.BUILD_TARGETS:
                    for lang in process_languages:
                        do_build(target=build_target, language=lang, clean=True)

            else:
                print(f"\nUnknown build target: '{args.build_target}'\n")
                exit_with_code(1)

    elif 'clean_targets' in vars(args):
        for target in args.clean_targets:
            if target in SPHINX_.BUILD_TARGETS:
                clean_dir = os.path.join(SPHINX_.BUILD_DIR, SPHINX_.BUILD_TARGETS[target]['dir'])
                clean_directory(clean_dir, target)

            elif target == 'mo':
                clean_mo()

            elif target == 'all':
                clean_mo()
                for clean_target, clean_target_value in SPHINX_.BUILD_TARGETS.items():
                    clean_dir = os.path.join(SPHINX_.BUILD_DIR, clean_target_value['dir'])
                    clean_directory(clean_dir, clean_target)

            else:
                print(f"\nUnknown clean target: '{target}'\n")
                exit_with_code(1)

    elif 'test_targets' in vars(args):
        for target in args.test_targets:
            if target == 'rst':
                run_lint(SPHINX_.SOURCE_DIR, ignore_info=IGNORE_INFO_MESSAGES, fail_on_warnings=FAIL_ON_WARNINGS)

            elif target == 'sphinx':
                for lang in process_languages:
                    run_sphinx_test(language=lang)

            elif target == 'po':
                checker = POCheck()
                if process_languages == [DEFAULT_LANGUAGE]:
                    checker.check(SPHINX_.LOCALE_DIR)
                else:
                    for lang in process_languages:
                        test_target = os.path.join(SPHINX_.LOCALE_DIR, lang)
                        checker.check(test_target)

            elif target == 'python':
                run_isort()
                run_flake8()
                run_pylint()

            elif target == 'isort':
                run_isort()

            elif target == 'flake8':
                run_flake8()

            elif target == 'pylint':
                run_pylint()

            elif target == 'html':
                print('\nThat function is still under development.\n')
                exit_with_code(1)

            elif target == 'pdf':
                print('\nThat function is still under development.\n')
                exit_with_code(1)

            else:
                print(f"\nUnknown test target: '{target}'\n")
                exit_with_code(1)

    else:
        # show help information
        show_help()

    exit_with_code(0)


##############################################################################


if __name__ == '__main__':
    main()

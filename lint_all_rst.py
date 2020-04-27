#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

import os
import restructuredtext_lint

IGNORE_INFO_MESSAGES = False
DIRECTIVES = ['toctree']
ROLES = ['doc', 'ref']

checked_count = 0
warning_count = 0
error_count = 0
info_count = 0


def check_file(file_name, ignore_info=True):
    global checked_count, warning_count, error_count, info_count
    print('Checking {0}'.format(file_name), end='', flush=True)
    checked_count += 1
    if os.path.isfile(file_name):
        try:
            err_processed = False
            errs = restructuredtext_lint.lint_file(file_name)
            if errs:
                for err in errs:
                    err_process = True
                    if err.type == 'INFO':
                        if ignore_info:
                            err_process = False
                        else:
                            for temp in DIRECTIVES:
                                if err.message.startswith('No directive entry for "{0}"'.format(temp,)):
                                    err_process = False
                            for temp in ROLES:
                                if err.message.startswith('No role entry for "{0}"'.format(temp,)):
                                    err_process = False
                    if (err.type == 'ERROR' or err.type == 'SEVERE') and err.message.startswith('Unknown'):
                        for temp in DIRECTIVES:
                            if err.message.endswith('directive type "{0}".'.format(temp,)):
                                err_process = False
                        for temp in ROLES:
                            if err.message.endswith('role "{0}".'.format(temp,)):
                                err_process = False
                    if err_process:
                        err_processed = True
                        # print('\n   [{0}] {1} Line {2}: {3}'.format(err.type, err.source, err.line, err.message), end='', flush=True)
                        print('\n   [{0}] Line {1}: {2}'.format(err.type, err.line, err.message), end='', flush=True)
                        if err.type == 'WARNING':
                            warning_count += 1
                        elif err.type == 'INFO':
                            info_count += 1
                        else:
                            # Includes 'ERROR' and 'SEVERE'
                            error_count += 1
            print('' if err_processed else ' [OK]')
        except Exception as ex:
            print('\n   [ERROR] Line 0: Error reading file.')
            error_count += 1
    else:
        print('\n   [ERROR] Line 0: File not found.')
        error_count += 1


print('\n\n')
check_file('index.rst', IGNORE_INFO_MESSAGES)

root_dir = 'source'
for dir_name, subdir_list, file_list in os.walk(root_dir):
    # print('Found directory: %s' % dir_name)
    for fname in file_list:
        # print('\t%s' % fname)
        if str(fname).lower().endswith('.rst'):
            check_file(os.path.join(dir_name, fname), IGNORE_INFO_MESSAGES)

if IGNORE_INFO_MESSAGES:
    print('\nChecked {0} files.  Errors: {1}.  Warnings: {2}.\n'.format(checked_count, error_count, warning_count))
else:
    print('\nChecked {0} files.  Errors: {1}.  Warnings: {2}.  Info: {3}\n'.format(checked_count, error_count, warning_count, info_count))

exit(1 if error_count > 0 else 0)

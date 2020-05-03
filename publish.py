#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Python script used to prepare documents for publishing.
"""

import glob
import os
import re
import shutil
import sys
import time

DEFAULT_LANGUAGE = 'en'
DOCUMENT_DIRECTORY = 'docs'
INDEX_TEMPLATE = 'index.html.template'
DEFAULT_LANGUAGE = 'en'

LANGUAGE_TEST_1 = re.compile(r'^[a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?$')
LANGUAGE_TEST_2 = re.compile(r'^.*MusicBrainz_Picard_\[([a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?)\].pdf$')

def exit_with_code(exit_code=0):
    """Print and exit with the specified exit code.

    Keyword Arguments:
        exit_code {int} -- Exit code to use (default: 0)
    """
    print('Exit Code: {0}\n'.format(exit_code))
    sys.exit(exit_code)

def clean_directory(dir_path, dir_name):
    """Removes all files and subdirectories for the specified directory.  If the specified
    directory does not exist, it will be created.  Includes multiple checks for success to
    accommodate race condition in Windows.

    Arguments:
        dir_path {str} -- Path to the directory to clean
        dir_name {str} -- Name of the directory type (e.g.: 'html')

    Raises:
        Exception: Unable to clean directory
        Exception: Unable to create directory
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            try:
                print('Emptying the {0} directory: {1}'.format(dir_name, dir_path))
                if not os.listdir(dir_path):
                    return
                shutil.rmtree(dir_path)
                counter = 10
                # Multiple checks for success to accommodate race condition in Windows
                while counter and os.path.exists(dir_path):
                    counter -= 1
                    time.sleep(1)
                if not counter:
                    raise Exception('Unable to clean directory.')
            except Exception:
                print("\nError removing the {0} directory: {1}\n".format(dir_name, dir_path))
                exit_with_code(1)
        else:
            print("\nThe {0} directory is not a directory: {1}\n".format(dir_name, dir_path))
            exit_with_code(1)
    else:
        try:
            print('Creating the {0} directory: {1}'.format(dir_name, dir_path))
            os.makedirs(dir_path)
            counter = 10
            # Multiple checks for success to accommodate race condition in Windows
            while counter and not os.path.exists(dir_path):
                counter -= 1
                time.sleep(1)
            if not counter:
                raise Exception('Unable to create directory.')
        except Exception:
            print("\nError creating the {0} directory: {1}\n".format(dir_name, dir_path))
            exit_with_code(1)

def remove_dir(dir_path):
    """Remove the specified directory.  Includes multiple checks for success to accommodate race
    condition in Windows.

    Arguments:
        dir_path {str} -- Path of directory to remove

    Raises:
        Exception: Directory not removed
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            try:
                os.rmdir(dir_path)
                counter = 10
                # Multiple checks for success to accommodate race condition in Windows
                while counter and os.path.exists(dir_path):
                    counter -= 1
                    time.sleep(1)
                if not counter:
                    raise Exception('Directory not removed.')
            except Exception:
                print("\nError removing the directory: {0}\n".format(dir_path))
                exit_with_code(1)
        else:
            print('\nUnable to remove (not a directory): {0}\n'.format(dir_path))
            exit_with_code(1)

def remove_file(file_path):
    """Removes the specified file.  Includes multiple checks for success to accommodate race
    condition in Windows.

    Arguments:
        file_path {str} -- File to remove.

    Raises:
        Exception: File not removed
    """
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                counter = 10
                # Multiple checks for success to accommodate race condition in Windows
                while counter and os.path.exists(file_path):
                    counter -= 1
                    time.sleep(1)
                if not counter:
                    raise Exception('File not removed.')
            except Exception:
                print("\nError removing the file: {0}\n".format(file_path))
                exit_with_code(1)
        else:
            print('\nUnable to remove (not a file): {0}\n'.format(file_path))
            exit_with_code(1)

def get_subdir_list(root_dir):
    """Get list of subdirectories in the specified directory.

    Arguments:
        root_dir {str} -- Path to directory to check

    Returns:
        {list} -- List of subdirectories
    """
    try:
        for dir_name, subdir_list, file_list in os.walk(root_dir):
            return subdir_list
    except Exception:
        return []

def get_file_list(root_dir):
    """Get list of files in the specified directory.

    Arguments:
        root_dir {str} -- Path to directory to check

    Returns:
        {list} -- List of files
    """
    try:
        for dir_name, subdir_list, file_list in os.walk(root_dir):
            return file_list
    except Exception:
        return []

def languages_from_dir_list(dir_list):
    """Extract a list of valid language codes from a directory list.

    Arguments:
        dir_list {list} -- List of directories

    Returns:
        {list} -- List of language codes
    """
    languages = [DEFAULT_LANGUAGE]
    for item in dir_list:
        temp = os.path.basename(item)
        if LANGUAGE_TEST_1.match(temp) and temp not in languages:
            languages.append(temp)
    return languages

def copy_files(mask, target):
    """Copy files using wildcards.

    Arguments:
        mask {str} -- Source files mask
        target {str} -- Target directory
    """
    for file in glob.glob(mask):
        print(" - {0}".format(file))
        shutil.copy(file, target)

def delete_files(mask):
    """Delete files using wildcards.

    Arguments:
        mask {str} -- Source files mask
    """
    for file in glob.glob(mask):
        print(" - {0}".format(file))
        os.remove(file)

def copy_directories(source, target):
    """Copy directory to target recursively.

    Arguments:
        source {str} -- Source directory to copy
        target {str} -- Target directory, which cannot exist for Python < 3.8
    """
    if os.path.exists(source) and os.path.exists(target) and os.path.isdir(target):
        try:
            subdirs = get_subdir_list(source)
            for subdir in subdirs:
                print(" - {0}".format(os.path.join(source, subdir)))
                shutil.copytree(os.path.join(source, subdir), os.path.join(target, subdir))
        except OSError as e:
            print('Copy unsuccessful. Error: {0}'.format(e))
            exit_with_code(1)

def main():
    """Main body of the script.
    """
    old_languages = languages_from_dir_list(get_subdir_list('.'))
    new_languages = languages_from_dir_list(get_subdir_list(DOCUMENT_DIRECTORY))
    print("\nOld languages = {0}\nNew languages = {1}".format(old_languages, new_languages))

    print('\nDeleting current files:')
    delete_files('*.pdf')
    delete_files('*.zip')

    print('\nDeleting current directories:')
    for item in old_languages:
        clean_directory(item, 'language')
        print("Removing directory: {0}".format(item))
        remove_dir(item)

    print('\nCopying new files and directories.')
    copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.pdf'), '.')
    copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.zip'), '.')
    copy_directories(DOCUMENT_DIRECTORY, '.')

    print('\nUpdating the master index.html file.\n')
    try:
        with open(INDEX_TEMPLATE, 'r', encoding='utf8') as f:
            temp = f.read()
    except Exception as e:
        print('Error reading template: {0}\n'.format(e))
        exit_with_code(1)
    temp = temp.replace(r'{{DEFAULT_LANGUAGE}}', DEFAULT_LANGUAGE).replace(r'{{SUPPORTED_LANGUAGES}}', str(new_languages))
    try:
        with open('index.html', 'w', encoding='utf8') as f:
            f.write(temp)
    except Exception as e:
        print('Error writing index.html file.\n')
        exit_with_code(1)

    exit_with_code(0)


##############################################################################


if __name__ == '__main__':
    RC = 1
    main()
    # try:
    #     main()
    #     RC = 0
    # except Exception as err:
    #     print('Error: {0}'.format(err), file=sys.stderr)
    sys.exit(RC)

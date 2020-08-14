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

import _build

DOCUMENT_DIRECTORY = 'docs'
BUILD_DIRECTORY = '_build'
DEFAULT_LANGUAGE = _build.default_language if _build.default_language else 'en'
CURRENT_VERSION = _build.current_version if _build.current_version else 'latest'
FILE_NAME_ROOT = _build.file_name_root if _build.file_name_root else 'MusicBrainz_Picard'

LANGUAGE_TEST_1 = re.compile(r'^[a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?$')
LANGUAGE_TEST_2 = re.compile(r'^.*MusicBrainz_Picard_\[([a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?)\].pdf$')


def exit_with_code(exit_code=0):
    """Print and exit with the specified exit code.
    Keyword Arguments:
        exit_code {int} -- Exit code to use (default: 0)
    """
    print('Exit Code: {0}\n'.format(exit_code))
    sys.exit(exit_code)


def make_directory(dir_path, dir_name):
    print('Creating the {0} directory: {1}'.format(dir_name, dir_path))
    os.makedirs(dir_path)
    counter = 10
    # Multiple checks for success to accommodate race condition in Windows
    while counter and not os.path.exists(dir_path):
        counter -= 1
        time.sleep(1)
    if not counter:
        raise Exception('Unable to reate the {0} directory: {1}'.format(dir_name, dir_path))


def clean_directory(dir_path, dir_name):
    """Removes the specified directory including all files and subdirectories.Includes
    multiple checks for success to accommodate race condition in Windows.
    Arguments:
        dir_path {str} -- Path to the directory to clean
        dir_name {str} -- Name of the directory type (e.g.: 'html')
    Raises:
        Exception: Unable to clean directory
        Exception: Not a directory
    """
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
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
        else:
            raise Exception("The {0} directory is not a directory: {1}\n".format(dir_name, dir_path))


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
            os.rmdir(dir_path)
            counter = 10
            # Multiple checks for success to accommodate race condition in Windows
            while counter and os.path.exists(dir_path):
                counter -= 1
                time.sleep(1)
            if not counter:
                raise Exception('Directory not removed.')
        else:
            raise Exception('\nUnable to remove (not a directory): {0}\n'.format(dir_path))


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
            os.remove(file_path)
            counter = 10
            # Multiple checks for success to accommodate race condition in Windows
            while counter and os.path.exists(file_path):
                counter -= 1
                time.sleep(1)
            if not counter:
                raise Exception('File not removed.')
        else:
            raise Exception('Unable to remove (not a file): {0}\n'.format(file_path))


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
        subdirs = get_subdir_list(source)
        for subdir in subdirs:
            print(" - {0}".format(os.path.join(source, subdir)))
            shutil.copytree(os.path.join(source, subdir), os.path.join(target, subdir))


def main():
    """Main body of the script.
    """
    old_languages = languages_from_dir_list(get_subdir_list('.'))
    new_languages = languages_from_dir_list(get_subdir_list(DOCUMENT_DIRECTORY))
    print("\nOld languages = {0}\nNew languages = {1}".format(old_languages, new_languages))

    print('\nDeleting current files:')
    delete_files('{0}_{1}_HTML_[*.zip'.format(FILE_NAME_ROOT, CURRENT_VERSION,))
    delete_files('{0}_{1}_[*.epub'.format(FILE_NAME_ROOT, CURRENT_VERSION,))
    delete_files('{0}_{1}_[*.pdf'.format(FILE_NAME_ROOT, CURRENT_VERSION,))
    delete_files('index.html')
    delete_files('version_links.js')

    print('\nDeleting current directories:')
    for item in old_languages:
        clean_directory(item, 'language')
        print("Removing directory: {0}".format(item))
        remove_dir(item)
    clean_directory(CURRENT_VERSION, 'version')
    make_directory(CURRENT_VERSION, 'version')

    print('\nCopying new files and directories.')
    copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.pdf'), '.')
    copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.epub'), '.')
    copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.zip'), '.')
    time.sleep(1)

    print('\nCopying html files to version directory.')
    copy_directories(DOCUMENT_DIRECTORY, CURRENT_VERSION)
    time.sleep(1)

    print('\nCopying html files to root directory.')
    copy_directories(DOCUMENT_DIRECTORY, '.')
    time.sleep(1)

    print('\nUpdating the master index.html file.')
    source = os.path.join(BUILD_DIRECTORY, 'top_index.html')
    target = 'index.html'
    # Ensure file exists so copy does not fail.
    with open(target, 'a', encoding='utf8') as ofile:
        ofile.write('')
    time.sleep(1)
    shutil.copy(source, target)

    print('Updating the version level index.html file.')
    source = os.path.join(BUILD_DIRECTORY, 'version_index.html')
    target = os.path.join(CURRENT_VERSION, 'index.html')
    # Ensure file exists so copy does not fail.
    with open(target, 'a', encoding='utf8') as ofile:
        ofile.write('')
    time.sleep(1)
    shutil.copy(source, target)

    print('Updating the version_links.js file.\n')
    source = os.path.join(BUILD_DIRECTORY, 'version_links.js')
    target = 'version_links.js'
    # Ensure file exists so copy does not fail.
    with open(target, 'a', encoding='utf8') as ofile:
        ofile.write('')
    time.sleep(1)
    shutil.copy(source, target)
    time.sleep(1)

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

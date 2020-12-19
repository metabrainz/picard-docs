#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Python script used to prepare documents for publishing.
"""

import glob
import importlib
import os
import re
import shutil
import sys
import time

PERSISTENT_FILE = 'persistent_settings'
persistent = importlib.import_module(PERSISTENT_FILE)

DOCUMENT_DIRECTORY = 'docs'
config = importlib.import_module(DOCUMENT_DIRECTORY)

DOWNLOADS_DIRECTORY = 'downloads'
BUILD_DIRECTORY = '_build'
DEFAULT_LANGUAGE = config.DEFAULT_LANGUAGE if config.DEFAULT_LANGUAGE else 'en'
LANGUAGE_LIST = config.LANGUAGES if config.LANGUAGES else [DEFAULT_LANGUAGE]
CURRENT_VERSION = config.VERSION if config.VERSION else ''
FILE_NAME_ROOT = config.FILE_NAME_ROOT if config.FILE_NAME_ROOT else 'MusicBrainz_Picard'
TAG_MAP_NAME = config.TAG_MAP_NAME if config.TAG_MAP_NAME else 'MusicBrainz_Picard_Tag_Map'

LANGUAGE_TEST_1 = re.compile(r'^[a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?$')
LANGUAGE_TEST_2 = re.compile(r'^.*' + FILE_NAME_ROOT + r'_\[([a-z]{2}(-[A-Z]([A-Z]{1}|[a-z]{3}){1})?)\].pdf$')

RE_VERSION = re.compile(r'^[0-9]+(\.[0-9]+){,2}$')


def make_sort_key(version):
    """Create a three-level sortable string key for the version string provided.
    The version string must consist of only digits and decimal points, and must
    begin with a digit.

    Args:
        version (str): The version string used to generate a key

    Returns:
        str: The sortable key for the version
    """
    parts = version.split(".")
    parts += ['0', '0', '0']
    key = '{0:0>5}.{1:0>5}.{2:0>5}'.format(parts[0], parts[1], parts[2],)
    return key


def get_latest_version(versions_dict):
    """Get the latest version number string from the versions dictionary.

    Args:
        versions_dict (dict): Dictionary of the version numbers by sort key

    Returns:
        str: Version number
    """
    version_keys = list(versions_dict.keys())
    version_keys.sort()
    return versions_dict[version_keys[-1]] if version_keys else ''


def get_reference_branch():
    """Get the GitHub target reference branch for the action.
    Returns:
        str: The target branch, or '' on error
    """
    try:
        GITHUB_REF = config.GITHUB_REF if config.GITHUB_REF else ''
        GITHUB_HEAD_REF = config.GITHUB_HEAD_REF if config.GITHUB_HEAD_REF else ''
        ref = GITHUB_HEAD_REF if GITHUB_HEAD_REF else GITHUB_REF
        parts = ref.split('/')
        return parts[-1]
    except AttributeError:
        return ''


def update_persistent_settings(module_name, stable_version, versions_dict, language, languages):
    """Overwrite the persistent settings module file with the updated information.

    Args:
        module_name (str): Name of the module containing the persistent settings
        stable_version (str): The latest version number
        versions_dict (dict): Dictionary of the version numbers by sort key
        language (str): Default language
        languages (list): Languages supported
    """
    versions = ''
    version_keys = list(versions_dict.keys())
    version_keys.sort()
    for key in version_keys:
        versions += "    '{0}',\n".format(versions_dict[key],)

    with open(module_name + '.py', 'w', encoding='utf8') as outfile:
        outfile.write(
            "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\n" +
            "# This file is automatically generated.\n\n" +
            "VERSIONS = [\n" + versions + "]\n" +
            "STABLE_VERSION = '" + stable_version + "'\n\n" +
            "DEFAULT_LANGUAGE = '" + language + "'\n" +
            "LANGUAGES = " + str(languages) + "\n"
        )


def exit_with_code(exit_code=0):
    """Print and exit with the specified exit code.
    Keyword Arguments:
        exit_code {int} -- Exit code to use (default: 0)
    """
    print('Exit Code: {0}\n'.format(exit_code))
    sys.exit(exit_code)


def make_directory(dir_path, dir_name):
    """If the specified directory does not exist, it will be created.  Includes multiple
    checks for success to accommodate race condition in Windows.

    Arguments:
        dir_path {str} -- Path to the directory to create
        dir_name {str} -- Name of the directory type (e.g.: 'html')

    Raises:
        Exception: Unable to create directory
    """
    if not os.path.exists(dir_path):
        print('Creating the {0} directory: {1}'.format(dir_name, dir_path))
        os.makedirs(dir_path)
        counter = 50
        # Multiple checks for success to accommodate race condition in Windows
        while counter and not os.path.exists(dir_path):
            counter -= 1
            time.sleep(.2)
        if not counter:
            raise Exception('Unable to create the {0} directory: {1}'.format(dir_name, dir_path))


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
            counter = 2
            while counter:
                # Retry to accommodate race condition in Windows
                try:
                    shutil.rmtree(dir_path)
                    counter = 0
                except OSError:
                    time.sleep(.2)
                    counter -= 1
            time.sleep(1)
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
        for dir_name, subdir_list, file_list in os.walk(root_dir):  # pylint: disable=unused-variable
            return subdir_list
    except OSError:
        return []


def get_file_list(root_dir):
    """Get list of files in the specified directory.
    Arguments:
        root_dir {str} -- Path to directory to check
    Returns:
        {list} -- List of files
    """
    try:
        for dir_name, subdir_list, file_list in os.walk(root_dir):  # pylint: disable=unused-variable
            return file_list
    except OSError:
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
            if subdir != '__pycache__':
                print(" - {0}".format(os.path.join(source, subdir)))
                shutil.copytree(os.path.join(source, subdir), os.path.join(target, subdir))


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
        return '{0}.{1}'.format(int('0' + parts[0]), int('0' + parts[1]))
    return ''


def make_versions_dict(version_list):
    """Create a dictionary of the version list provided.

    Args:
        version_list (list): List of versions

    Returns:
        dict: Dictionary of versions
    """
    versions_dict = {}
    for item in version_list:
        item = get_major_minor(item)
        if item:
            versions_dict[make_sort_key(item)] = item
    return versions_dict


def main():
    """Main body of the script.
    """

    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements

    # Initialize variables
    publish_targets = []
    P_VERSIONS = persistent.VERSIONS.copy()
    P_STABLE_VERSION = str(persistent.STABLE_VERSION)
    P_LANGUAGES = persistent.LANGUAGES.copy()
    P_DEFAULT_LANGUAGE = str(persistent.DEFAULT_LANGUAGE) if persistent.DEFAULT_LANGUAGE else 'en'
    MAJOR_MINOR = get_major_minor(CURRENT_VERSION)

    # print('\nCURRENT_VERSION = {0}'.format(CURRENT_VERSION,))
    # print('MAJOR_MINOR = {0}'.format(MAJOR_MINOR,))
    # exit_with_code(0)

    # print('\nP_VERSIONS = {0}'.format(P_VERSIONS,))
    # print('P_STABLE_VERSION = {0}'.format(P_STABLE_VERSION,))
    # print('P_LANGUAGES = {0}'.format(P_LANGUAGES,))
    # print('P_DEFAULT_LANGUAGE = {0}'.format(P_DEFAULT_LANGUAGE,))

    # Get the current reference branch for the GitHub action.
    branch = get_reference_branch()
    # branch = 'master'
    # branch = '2.5'

    if branch == 'master':
        publish_targets.append('.')
        P_DEFAULT_LANGUAGE = DEFAULT_LANGUAGE
        for lang in LANGUAGE_LIST:
            if lang not in P_LANGUAGES:
                P_LANGUAGES.append(lang)
        # if MAJOR_MINOR and 'v{0}'.format(MAJOR_MINOR,) in VERSIONS:
        if MAJOR_MINOR:
            if MAJOR_MINOR not in P_VERSIONS:
                P_VERSIONS.append(MAJOR_MINOR)
            publish_targets.append('v{0}'.format(MAJOR_MINOR,))
    elif branch == MAJOR_MINOR and branch in P_VERSIONS:
        publish_targets.append('v{0}'.format(MAJOR_MINOR,))

    if re.match(r'^v?([0-9\.]+)$', CURRENT_VERSION):
        P_STABLE_VERSION = get_latest_version(make_versions_dict([P_STABLE_VERSION, MAJOR_MINOR]))

    # print('\nP_VERSIONS = {0}'.format(P_VERSIONS,))
    # print('P_STABLE_VERSION = {0}'.format(P_STABLE_VERSION,))
    # print('P_LANGUAGES = {0}'.format(P_LANGUAGES,))
    # print('P_DEFAULT_LANGUAGE = {0}'.format(P_DEFAULT_LANGUAGE,))

    print('\nPublish_targets: {0}\n'.format(publish_targets,))

    # exit_with_code(0)

    if publish_targets:

        # print('\nDeleting current files:')
        # delete_files(os.path.join(DOWNLOADS_DIRECTORY, '{0}_{1}_HTML_[*.zip'.format(FILE_NAME_ROOT, CURRENT_VERSION,)))
        # delete_files(os.path.join(DOWNLOADS_DIRECTORY, '{0}_{1}_[*.epub'.format(FILE_NAME_ROOT, CURRENT_VERSION,)))
        # delete_files(os.path.join(DOWNLOADS_DIRECTORY, '{0}_{1}_[*.pdf'.format(FILE_NAME_ROOT, CURRENT_VERSION,)))
        # delete_files('index.html')
        # delete_files('version_links.js')

        print('\nDeleting current directories:')
        for target in publish_targets:
            if target == '.':
                for item in LANGUAGE_LIST:
                    clean_directory(item, 'language')
                    print("  - Removing directory: {0}".format(item))
                    remove_dir(item)
            else:
                clean_directory(target, 'version')
                make_directory(target, 'version')

        print('\n')
        make_directory(DOWNLOADS_DIRECTORY, 'Downloads')
        print('Copying new files to Downloads directory.')
        copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.pdf'), DOWNLOADS_DIRECTORY)
        copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.epub'), DOWNLOADS_DIRECTORY)
        copy_files(os.path.join(DOCUMENT_DIRECTORY, '*.zip'), DOWNLOADS_DIRECTORY)
        if branch == 'master':
            copy_files(os.path.join(DOCUMENT_DIRECTORY, '{0}.*'.format(TAG_MAP_NAME)), DOWNLOADS_DIRECTORY)
        time.sleep(1)

        for target in publish_targets:
            print('\nCopying html files to \'{0}\' directory.'.format(target,))
            copy_directories(DOCUMENT_DIRECTORY, target)
            time.sleep(1)

        print('\nUpdating the master index.html file(s).')
        with open('index_template.html', 'r', encoding='utf8') as f:
            template = f.read()
        for target in publish_targets:
            ver = '' if target == '.' else 'v{0}'.format(MAJOR_MINOR,)
            html = template
            html = html.replace('{{supported_languages}}', str(P_LANGUAGES))
            html = html.replace('{{default_language}}', P_DEFAULT_LANGUAGE)
            html = html.replace('{{current_version}}', ver)
            filename = os.path.join(ver, 'index.html') if ver else 'index.html'
            print('  - Writing: {0}'.format(filename,))
            with open(filename, 'w', encoding='utf8') as f:
                f.write(html)
        time.sleep(1)

        print('\nUpdating the master 404.html file.')
        with open('404_template.html', 'r', encoding='utf8') as f:
            html = f.read()
        html = html.replace('{{supported_languages}}', str(P_LANGUAGES))
        html = html.replace('{{default_language}}', P_DEFAULT_LANGUAGE)
        html = html.replace('{{version_list}}', str(P_VERSIONS))
        html = html.replace('{{stable_version}}', str(P_STABLE_VERSION))
        with open('404.html', 'w', encoding='utf8') as f:
            f.write(html)
        time.sleep(1)

        print('Updating the version_links.js file.')
        with open('version_links_template.js', 'r', encoding='utf8') as f:
            template = f.read()
        template = template.replace('{{default_language}}', P_DEFAULT_LANGUAGE)
        template = template.replace('{{stable_version}}', P_STABLE_VERSION)
        template = template.replace('{{version_list}}', str(P_VERSIONS))
        with open('version_links.js', 'w', encoding='utf8') as f:
            f.write(template)
        time.sleep(1)

        print('Updating the persistent settings file: {0}.py\n'.format(PERSISTENT_FILE,))
        update_persistent_settings(PERSISTENT_FILE, P_STABLE_VERSION, make_versions_dict(P_VERSIONS), P_DEFAULT_LANGUAGE, P_LANGUAGES)

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
    # sys.exit(RC)
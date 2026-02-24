#!/usr/bin/env python3
"""Python script used to provide a list of translation contributors and
translation completion information for each locale (language).
"""
# Version 1.0
# Copyright (C) 2025 Bob Swift

import os
import re
import subprocess

from conf import locale_dirs


# Set to True to print the lines from the gitlog output and the list
# of authors for each file checked.  This is a very lengthy output
# and is best redirected to a log file for review.
DEBUG = False

# Aliases to match to avoid duplicate credits under different names.
ALIASES = {
    'bob': 'Bob Swift',
    'phw': 'Philipp Wolfer',
    'rdswift': 'Bob Swift',
    'mfmeulenbelt': 'Maurits Meulenbelt',
}

# Contributor names to ignore (lower case)
IGNORE = {
    'anonymous',
    'hosted weblate',
    'languages add-on',
    'weblate',
}

# Used to restrict the applicable languages for selected authors.  This is
# necessary because some authors appear on commits for all translation files,
# even if they did not contribute a translation for a locale (language).
OK_LANGUAGES = {
    'Bob Swift': {'en', 'fr'},
    'Philipp Wolfer': {'de'},
}

# Domains to omit from the translator credits.
BAD_DOMAINS = set(['hostux.ninja'])

# Regular expressions used
RE_LANGUAGE = re.compile(r'^.*/(?P<language>[^/]+)/LC_MESSAGES')
RE_GITLOG = re.compile(r'^(?P<email>[^¤]*)¤(?P<name>.*)$')
RE_TEAM = re.compile(r'^"Language-Team: (?P<team>[^<\\]*)')


######################################################################################

def get_domain(email: str) -> str:
    """Extract the domain portion of an email address.

    Args:
        email (str): Email address to process.

    Returns:
        str: Domain portion of the address if it exists, otherwise an empty string.
    """
    return email.split('@', maxsplit=1)[1].strip() if '@' in email else ''


######################################################################################

def extract_authors_from_gitlog(path: str, debug: bool = False) -> set:
    """Read the git commit log and extract the list of authors for a file.

    Args:
        path (str): Path of the file to check.
        debug (bool, optional): Print debug information while processing. Defaults to False.

    Returns:
        set: Set containing the authors for the file.
    """

    authors = set()
    cmd = ['git', 'log', r'--pretty=format:%aE¤%aN', r'--', path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, timeout=30, check=False)
    if result.returncode == 0:
        for line in result.stdout.decode('utf-8').split("\n"):
            if debug:
                print(f"Checking: {line}")
            matched = RE_GITLOG.search(line)
            if matched:
                author = matched.group('name')
                email = matched.group('email')
                # Get standard name for the author if there is an alias.
                for c in (f"{author} <{email}>", email, author):
                    if c in ALIASES:
                        author = ALIASES[c]
                        break
                # Only add author if name and email domain are not blocked.
                if author.lower() not in IGNORE and get_domain(email) not in BAD_DOMAINS:
                    authors.add(author)
    if debug:
        print(f"Authors: {', '.join(sorted(authors))}")
    return authors


######################################################################################

def get_translation_counts(file: str, translation_counts: tuple, language: str, language_titles: dict) -> tuple:
    """Update the counts of total strings to translate and translated strings
    with counts from the specified file.  Also updates the language title dictionary.

    Args:
        file (str): Translation file to process.
        translation_counts (tuple): Starting value of (total translation stings, number of translated strings) for the language.
        language (str): Localization (language) code for the file.
        language_titles (dict): Language titles dictionary to update.

    Returns:
        tuple: Updated tuple of (total translation stings, number of translated strings) for the language.
    """
    total, translated = translation_counts
    processing = False
    # Read the translation file into an array to allow accessing a line multiple times.
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()

    line_count = len(lines)
    line_num = 0
    while line_num < line_count:
        line = str(lines[line_num]).strip()
        line_num += 1

        # Ignore blank lines
        if not line:
            continue

        # Get the locale (language) title if it isn't already set.
        if line.startswith('"Language-Team:') and not language_titles[language]:
            matches = RE_TEAM.match(line)
            text = matches.group('team').strip()
            if text and text.lower() != 'none':
                language_titles[language] = text

        # Get the translation key.
        if line.startswith('msgid "'):
            processing = False
            text = line.strip()[7:-1]
            # Append to text from continuation lines.
            while line_num < line_count and str(lines[line_num]).strip() and str(lines[line_num]).startswith('"'):
                text += str(lines[line_num]).strip()[1:-1]
                line_num += 1
            # Only update count if the translation key is not empty.
            if text.strip():
                total += 1
                processing = True

        # Get the translation value.
        if processing and line.startswith('msgstr "'):
            text = line.strip()[8:-1]
            # Append to text from continuation lines.
            while line_num < line_count and str(lines[line_num]).strip() and str(lines[line_num]).startswith('"'):
                text += str(lines[line_num]).strip()[1:-1]
                line_num += 1
            # Only update count if the translation value is not empty.
            if text.strip():
                translated += 1
            processing = False

    return total, translated


######################################################################################

def get_po_files():
    """Gets the translation files to process.

    Yields:
        Iterable: Iterable of tuples: (locale, file path).
    """
    for base_path in locale_dirs:
        for _path, _dirs, _files in os.walk(base_path):
            matches = RE_LANGUAGE.search(_path)
            if not matches:
                continue
            language = matches.group('language')
            for _file in _files:
                # Only include translation *.po files.
                if not _file.endswith('.po'):
                    continue
                filepath = os.path.join(_path, _file)

                yield language, filepath


######################################################################################

def main() -> None:
    """Main processing method.  Reviews the git history for all translation files and
    prints:

    1) A list of all translators and the locales they translated; and
    2) A list of the locales that have translations, and the translators contributing
    to that locale.
    """
    translators = {}
    languages = {}
    completion = {}
    language_titles = {}

    for item in get_po_files():
        language, filepath = item

        text = f"Processing: {filepath}{' ' * 79}"[:79]
        print(f"{text}", end='\r', flush=True)

        if language not in language_titles:
            language_titles[language] = ''

        # Tuple of (total translation stings, number of translated strings)
        completion[language] = get_translation_counts(
            filepath, completion[language] if language in completion else (0, 0),
            language, language_titles)

        # Example of only displaying debug output for a single locale.
        # authors = extract_authors_from_gitlog(filepath, debug=language == 'pt_BR')
        authors = extract_authors_from_gitlog(filepath, debug=DEBUG)
        for author in authors:
            # Don't add authors that have language restrictions
            if author in OK_LANGUAGES and not any(language.startswith(i) for i in OK_LANGUAGES[author]):
                continue

            if author not in translators:
                translators[author] = set()
            translators[author].add(language)

            if language not in languages:
                languages[language] = set()
            languages[language].add(author)

    print(' ' * 79, end='\r', flush=True)

    def _name_sorter(key: str) -> str:
        """Parses the name to return a sort key based on last name.

        Args:
            key (str): Name to parse.

        Returns:
            str: Lower case name in the format "last name, first name".
        """
        parts = str(key).lower().split()
        return f"{parts[-1]}{(', ' + ' '.join(parts[:-1])) if len(parts) > 1 else ''}"

    print("\nTranslators:")
    for author in sorted(translators.keys(), key=_name_sorter):
        print(f" - {author} ({', '.join(sorted(translators[author]))})")

    print(f"\n{'-' * 79}")

    for language in sorted(languages.keys()):
        total, translated = completion[language]
        completed = round(100 * translated / total, 1)
        print(
            f"\nLanguage: [{language}] "
            f"{language_titles[language] if language in language_titles and language_titles[language] else 'Unknown Language'}\n"
            f"Progress: Translated {translated:,} of {total:,} strings ({completed}%)"
        )
        for author in sorted(languages[language], key=_name_sorter):
            print(f" - {author}")


######################################################################################

if __name__ == '__main__':
    main()

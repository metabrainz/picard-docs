# Developer Utilities

A set of utilities to aid developers is available as `dev_utils.py` in the root directory of the repository. It is called as `python dev_utils.py {command} [arguments]`. Brief help is available by entering `python dev_utils.py --help` for general help identifying the commands available, or `python dev_utils.py {command} --help` for help regarding the specified command. The commands currently supported are `test`, `clean`, `build`, `stage` and `info`, and these are covered in more detail below.

Some of the functions allow you to specify a specific language to which the processing should be applied. This is enabled by including `-l {language}` or `--language {language}` on the command line following the processing command, such as `python dev_utils.py test po --language fr` to check just the French language `*.po` files. If no language is specified, the language processed defaults to English (en). Use the language `-all` to repeat the processing for all supported languages.

In addition, the repository contains a pre-commit configuration file (`.pre-commit-config.yaml`) that will perform some basic checks on the files. This can be configured to run automatically when commiting changes to the git repository. See the [pre-commit documentation](https://pre-commit.com) for more information regarding the installation and use of the pre-commit hooks.

## Checking Files (`test`)

Files are checked for consistency and integrity by using the `test` command. The type of files checked and the testing provided is specified as an argument to the command. Valid arguments and the functionality they provide are:

### Documentation and Translation Files

- `rst`: Lint checks the restructured text (*.rst) files. The optional argument `-v`/`--verbose` is used to include INFO level messages in the output, and `-i`/`--ignore-warnings` is used to not fail the test on WARNING level messages.
- `sphinx`: Performs a test build of the restructured text files using Sphinx.
- `po`: Performs a rudimentary check of the restructured text contained in the *.po translation files.
- `fuzzy`: Provides a list of all *.po translation files that contain a fuzzy translation that will need to be reviewed.

### Python Files

- `flake8`: Checks the files using flake8.
- `pylint`: Checks the files using pylint.
- `isort`: Checks the files using isort.
- `python`: Runs all of the checks (flake8, pylint and isort).

## Cleaning Files and Directories (`clean`)

The utility can clean (reset) the build directories to force a clean build using the `clean` command. The type of files removed is specified as an argument to the command. Valid arguments and the functionality they provide are:

- `mo`: Remove all compiled translation MO files.
- `html`: Resets the html build directory.
- `pdf`: Resets the pdf build directory.
- `all`: Remove all compiled translation MO files and resets all build targets.

## Build Output Files (`build`)

The output files can be built in the various formats using the `build` command to allow for local checking and testing. The type of output files produced is specified as an argument to the command. Valid arguments and the functionality they provide are:

### Documentation Source and Translation Files

- `map`: Build the tag map html and spreadsheet files from the master `tag_mapping.py` file. This will also update the `appendices/tag_mapping.rst` file so that the latest information is used for the document output builds.
- `pot`: Build the translation template POT files. This will update the translation template files based on the current restructured text (RST) files, and updates all of the language translation (PO) files with any changes to the source strings. This should be done when changes to the documentation are merged so that the translation files on Weblate are updated accordingly.
- `po`: Updates all of the language translation (PO) files with any changes to the source strings based on the current translation template (POT) files. This is performed automatically when the POT files are rebuilt.

### Documentation Output Files

- `html`: Builds the html output files for the documentation site. Defaults to English unless another language is specified.
- `pdf`: Builds the pdf output file for the documentation. Defaults to English unless another language is specified.
- `all`: Builds all output files for the documentation. Defaults to English unless another language is specified.

## Stage Files for Git (`stage`)

Translation POT and PO files are checked for changes and staged for Git. The actual translation keys and translation strings are combined into complete strings for comparison because different line lengths in the file can cause git to identify the file as modified even if there are no changes to the translation keys or actual translations. In addition, translation files are not staged if the only change is in the header information. Valid options to the `stage` command and the functionality they provide include:

- `-r` or `--rst`: Also stage any modified restructured text (RST) files.
- `-d` or `--dry-run`: Do not actually stage the changed files, but only report the files to be staged.
- `-f` or `--files-save`: Saves the output of the `git status` and `git diff` commands to `git_status.txt` and `git_diff.txt` respectively. This option is generally used for debugging purposes.

## General Information (`info`)

The script can provide some general information about itself using the `info` command. The type of information output is specified as an argument to the command. Valid arguments and the output they provide are:

- `about`: General information about the script.
- `languages`: A list of the supported languages. These are the languages that have translations that are substantially complete and are being published on the website.
- `warranty`: Warranty covering the use of the script.

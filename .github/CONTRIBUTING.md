# Contributing to Documentation for MusicBrainz Picard

This documentation project only exists because of the volunteer effort that goes into its development, from the initial documentation on the Picard website, the information posted in the [Community Discussion Forum](https://community.metabrainz.org/), documentation from scripts, plugins and program source code, proofreaders, editors, translators, and feedback from the user community.

Further high quality contributions are welcomed from all Picard users wanting to be part of the open source community that creates and maintains this valuable music tool. Even if you cannot write code, based on your experience of using Picard any help you can give to improve this documentation further will be most appreciated. If you cannot improve the existing help, but would be willing to assist in creating or maintaining translations into other languages, that would be of great benefit.

Please refer to the [Style Guidelines](https://github.com/metabrainz/picard-docs/blob/main/_project_documentation/DOCUMENTATION_STYLE_GUIDE.md) for more information about the stylistic and RestructuredText coding preferences for the documentation project.

If you want to contribute corrections or new material to this documentation project, there are a few different ways to submit your contributions.

- If you are comfortable developing ReStructuredText format files, and are familiar with [Pull Requests](https://github.com/metabrainz/picard-docs/pulls) on GitHub, you can submit a pull request with the changes to the documentation source files. This is the preferred method, because it provides a clear way for the changes to be reviewed and discussed. To setup the development environment for documentation see the [Technical Setup](#technical-setup) section below.

- If you are not so comfortable developing ReStructuredText format files or preparing GitHub pull requests, you can create a [ticket](https://tickets.metabrainz.org/issues/?jql=project+%3D+PICARD+AND+component+%3D+Documentation+AND+resolution+%3D+Unresolved) under the Picard project (Documentation component) requesting the change (if the issue does not already exist) and attach your suggestions to it, either as an attached text file or within the discussion comments on the Issue. This way, someone can convert your suggestions into the appropriate (\*.rst) file changes and submit a pull request with the changes on your behalf.

- You can also provide your suggestions on the [Community Discussion Forum](https://community.metabrainz.org/), or via email to the editor of the MusicBrainz Picard documentation project through their [account profile page](https://musicbrainz.org/user/rdswift) on [MusicBrainz](https://musicbrainz.org/).

If you are submitting your changes via a pull request, please make the request against the `main` branch for review and implementation, unless it is specific to a previous version of the documentation. All documentation is included in the form of restructured text files (\*.rst) found in the appropriate *"source"* directory such as `config`, `tutorials` and `usage`. These directories also contains some subdirectories to help organize the information into logical groups.The *"index.rst"* file contains the top level document index for the HTML output, and the *"pdf.rst"* file contains the document index for the PDF output. [Sphinx](https://www.sphinx-doc.org/) is used to produce the final output documents. Please check your submission for things like spelling and punctuation, don't add unnecessary newlines (long lines are actually preferred), and please remove any trailing whitespace from the lines. When you submit the pull request, the system will perform some automated testing of the \*.rst files, and will attempt to build the documentation.

The source documentation has been developed in the English language. Translation into other languages is being managed through a [Weblate server](https://translations.metabrainz.org/) under the project name "Picard Docs". This provides a number of benefits including translation tools and automated checking and processing. Any help in providing or reviewing translations is greatly appreciated. That helps to make the information available to a greater number of Picard users. Please contact us if you are interested in helping to work on translating the documentation to other languages, or would like to contribute in some other manner.

Thank-you for considering contributing to this documentation project.


## Technical Setup

### 1. Install uv (Recommended)

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package manager:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Set Up Development Environment

```bash
# Clone and enter the repository
git clone https://github.com/metabrainz/picard-docs.git
cd picard-docs

# Create virtual environment
uv venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate.bat  # Windows

# Install the documentation dependencies
uv sync
```

### 3. Launch the sphinx server for previewing documentation

```bash
# Builds the sphinx documentation and starts a server at http://127.0.0.1:8000 for previewing
uv run sphinx-autobuild ./ ./build/
```


## Development workflow

### Dependency Management

Dependencies are defined in `pyproject.toml` using modern Python packaging standards:

- **Main dependencies**: Runtime requirements for the picard-docs repo
- **dev**: Development tools (pre-commit, pylint, restructuredtext-lint, etc.)

### Documentation Quality

Install pre-commit hooks for automatic documentation checks on submit:

```bash
pre-commit install
```

This will run `rstcheck` validation checks on the `*.rst` files with the repo as well as sphinx-lint against the ReStructuredText format files when commit changes using `git`.


### Alternative Setup (Traditional pip)

```bash
If you prefer not to use uv:

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements_dev.txt

sphinx-autobuild ./ ./build/
```

### Previewing Documentation

Updates to documentation can be verified by running a local sphinx server using the command `sphinx-autobuild`.
Before running `sphinx-autobuild`, make sure your virtual environment is active by sourcing the `activate` script first.
```bash
source .venv/bin/activate
```

`sphinx-autobuild` supports hot reloading in the browser, so any updates to `*.rst` files will be seen live as the files are saved.<br/>
If for reason the page does not update, a hard-refresh can be performed in the browser by pressing `CTRL+SHIFT+R` (Linux/Windows) or `CMD+OPTION+R` (MacOS).

The sphinx server preview will be available at http://127.0.0.1:8000.

![Sphinx Preview server](./static/sphinx-preview-server.png)

For more in-depth instructions on how to translate, build, test and validate documentation changes, the [DEV_UTILS.md](../_project_documentation/DEV_UTILS.md) provides detailed explanations on the `dev_utils.py` script used to run file checks.

# Repository Structure

The Picard Documentation Project repository is partially structured both in terms of branches as well as directories and files. If you are submitting changes to the documentation then it is beneficial to understand the existing structure. In addition, it helps make it easier to locate a particular file when adding or correcting information.

-----

## Branch Structure

There are four types of branches within the repository:

1. ***Primary Branch***: This is the `main` branch which holds the most up-to-date documentation (including pre-release versions in testing) and is published as the "latest" version on the [documentation website](https://picard-docs.musicbrainz.org). It is also used to connect to the [Weblate translation server](https://translations.metabrainz.org/projects/picard-docs/) to exchange translation `\*.pot` and `\*.po` files. When the ***Primary Branch*** is updated, the changes are automatically published. A pull request entered against the branch will initiate a check of the restructured text (RST) files as well as a basic build of the publication files in the default language (English) only.

2. ***Publication Branches***: These are the branches that contain the versions of the documentation published, and will initiate a publish action on the documentation server when they are updated. These branches include any version number branches named in the form `v{major}.{minor}` where `{major}` and `{minor}` are integers containing only digits (e.g.: `v2.5` or `v3.0`). A pull request entered against one of these branches will initiate a check of the restructured text (RST) files as well as a basic build of the publication files in the default language (English) only. More information about how information is published can be found in [Publishing the Documentation](https://github.com/metabrainz/picard-docs/blob/main/_project_documentation/PUBLISHING_DOCUMENTATION.md). Once created, ***Publication Branches*** should not be removed.

3. ***Next Version Branch***: This is the `next_version` branch. This is used to collect documentation changes prior to a `v{major}.{minor}` pre-release version of Picard being issued, and would be merged into the ***Primary Branch*** once the pre-release version of Picard has been made publicly available for testing. A pull request entered against the branch will initiate a check of the restructured text (RST) files as well as a basic build of the publication files in the default language (English) only.

4. ***Working Branches***: This includes all other branches. These will typically be used for development and staging of changes that will eventually be applied to the ***Primary Branch***, the ***Next Release Branch***, or one of the ***Publication Branches***. There is no automatic checking performed when one of these ***Working Branches*** is updated. These ***Working Branches*** can be created as required and removed when no longer needed, and can have any valid GitHub branch name except for the names reserved for the ***Primary Branch***, ***Next Version Branch***, and ***Publication Branches***.

-----

## Directory and File Structure

There is generally one type of directory structures used for all of the source file branches.

The root directory of the ***Primary Branch***, ***Publication Branches***, ***Next Version Branch*** and ***Working Branches*** contains the files used to configure the build environment for compiling the source files into the files to be published, as well as the developer utilities script (`dev_utils.py`) and support files used to perform the builds and miscellaneous maintenance of the project files.

The `.github` directory contains the action scripts for testing and building the files for the website, as well as the templates used by GitHub for things like pull requests and issue reports.

The `_locale` directory contains the `gettext` catalog files for translating the documentation to other languages. The translation template (`*.pot`) files produced by `gettext` are included because they are used by Weblate. The language-specific translation files are included and can be found in subdirectories named by the applicable language code. The individual language translation files are named with the `.po` extension. The translation files with the `.mo` extension are not included because these are recreated automatically when the documentation is built.

The `_project_documentation` directory contains the documentation files describing and supporting the project. It does not contain the actual Picard documentation.

The `_static` directory contains the static files such as css and site icon that are used throughout all versions and languages of the documentation provided on the website.

The `_templates` directory contains the templates used by `Sphinx` when building the documentation files.

All remaining directories contain the source files for the documentation, with each directory holding a specific chapter or topic. Images used for that chapter or topic are stored in an `images` subdirectory of the topic directory. Note that images to be used for languages other than the default (English) base language must have the target language code identified just prior to the file extension. For example, if the English version of an image is named `image1.jpg`, the French version of the image would be `image1.fr.jpg`. If there is no language-specific image file, then the default (English) image file will be used. The image would still be specified using the default (English) name in the restructured-text files, and Sphinx would automatically use the French version if available for the French version of the documentation.

The documentation files are developed using restructured-text and are named with the extension `.rst`. The top-level index files are stored in the root directory for HTML (`index.rst`) and PDF (`pdf.rst`) output.

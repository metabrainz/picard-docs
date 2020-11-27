# Contributing to Documentation for MusicBrainz Picard

This documentation project only exists because of the volunteer effort that goes into its development, from the initial documentation on the Picard website, the information posted in the [Community Discussion Forum](https://community.metabrainz.org/), documentation from scripts, plugins and program source code, proofreaders, editors, translators, and feedback from the user community.

Further high quality contributions are welcomed from all Picard users wanting to be part of the open source community that creates and maintains this valuable music tool. Even if you cannot write code, based on your experience of using Picard any help you can give to improve this documentation further will be most appreciated. If you cannot improve the existing help, but would be willing to assist in creating or maintaining translations into other languages, that would be of great benefit.

If you want to contribute corrections or new material to this documentation project, there are a few different ways to submit your contributions.

- If you are comfortable developing ReStructuredText format files, and are familiar with [Pull Requests](https://github.com/rdswift/picard-docs/pulls) on GitHub, you can submit a pull request with the changes to the documentation source files. This is the preferred method, because it provides a clear way for the changes to be reviewed and discussed.

- If you are not so comfortable developing ReStructuredText format files or preparing GitHub pull requests, you can create an [Issue](https://github.com/rdswift/picard-docs/issues) requesting the change (if the issue does not already exist) and attach your suggestions to it, either as an attached text file or within the discussion comments on the Issue. This way, someone can convert your suggestions into the appropriate (\*.rst) file changes and submit a pull request with the changes on your behalf.

- You can also provide your suggestions on the Community Discussion Forum, or via email to the editor of the MusicBrainz Picard documentation project through their [account profile page](https://musicbrainz.org/user/rdswift) on [MusicBrainz](https://musicbrainz.org/).

If you are submitting your changes via a pull request, please make the request against the `master` branch for review and implementation.  All documentation is included in the form of restructured text files (\*.rst) found in the *"source"* directory.  This directory also contains some subdirectories to help organize the information into logical groups.  The *"index.rst"* file contains the top level document index for the HTML output, *"epub.rst"* contains the index for the ePub output, and the *"pdf.rst"* file contains the document index for the PDF output. [Sphinx](https://www.sphinx-doc.org/) is used to produce the final output documents.  Please check your submission for things like spelling and punctuation, and please remove any trailing whitespace from the lines.  When you submit the pull request, the system will perform some automated testing of the \*.rst files, and will attempt to build the documentation.

The source documentation has been developed in the English language.  Please contact us if you are interested in helping to work on translating the documentation to other languages, or would like to contribute in some other manner.

Thank-you for considering contributing to this documentation project.

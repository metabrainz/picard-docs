# Project Workflow

The typical (simplified) steps for making a change to the documentation is:

1. Change proposed
2. Proposed change reviewed
3. Change approved and applied
4. Updated documentation translated
5. Documentation translations published

Following, each of these typical steps is described in greater detail.

## 1. Change proposed

Source branch: various (specific to the change / pull request)<br />
Target branch: `main` (or `v{major}.{minor}` for changes to prior versions of the documentation)

Proposed changes are made to the English base language documentation source files in a branch created from the current `main` branch. A pull request is created by the content contributor to merge the changes into the target branch. If the change is to an earlier `v{major}.{minor}` version of the documentation, the working branch will be created from the associated `v{major}.{minor}` branch and the changes will be merged into the `v{major}.{minor}` branch rather than the `main` branch.

## 2. Proposed change reviewed

Source branch: various (specific to the change / pull request)<br />
Target branch: `main` (or `v{major}.{minor}` for changes to prior versions of the documentation)

The pull request with the proposed changes is reviewed by the editor for overall quality and consistency with the document structure and presentation, including restructured text encoding. The pull request is also reviewed to ensure that any technical content is correct. Any review comments applied should be addressed by the content contributor, making changes if required or explaining why the proposed content should not be changed.

## 3. Change approved and applied

Source branch: various (specific to the change / pull request)<br />
Target branch: `main` (or `v{major}.{minor}` for changes to prior versions of the documentation)

Once the pull request has received editorial and (if necessary) technical approval and all review comments have been addressed, it is merged into the `main` branch (or `v{major}.{minor}` branch for changes to prior versions of the documentation). In preparation for translation of the changes to other languages, the editor will generate updated translation template `*.pot` files which are are uploaded to the Weblate translation server used for the project. The translators are notified through their accounts on Weblate that there are changes requiring translation.

## 4. Updated documentation translated

Source branch: `main` (through Weblate)<br />
Target branch: `main` (or `v{major}.{minor}` branch for changes to prior versions of the documentation)

The translators provide updated translations to accommodate the changes to the documentation. Depending on the tools used for translating and producing the `*.po` files, the translators may submit pull requests directly for review or the translations can be updated through the Weblate server (preferred). Once a translation pull request has been revied and approved, the pull request will be merged. If the translation updates are being managed on the Weblate server, then they will be merged automatically into the `main` branch.

All translation updates to prior versions of the documentation must be submitted as pull requests to the appropriate `v{major}.{minor}` branch rather than the `main` branch.

## 5. Documentation published

Source branch: `main` (or `v{major}.{minor}` branch for changes to prior versions of the documentation)

Once the translations are complete and merged into the `main` branch, the revised documentation will be automatically generated and published as the `latest` version on the documentation website. Translations merged into a `v{major}.{minor}` branch will automatically trigger the generation and publication as the `v{major}.{minor}` version on the website.

-----

## Notes

Pushing / merging to the `main` or `v{major}.{minor}` branches will automatically trigger building the updated documentation files and update the documentation available of the website. This ensures that the latest approved changes are published promptly, although it also means that translations may lag behind the English base language version.

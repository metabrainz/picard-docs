# AGENTS.md - Picard Documentation Project

> This file condenses project documentation from the `_project_documentation/` directory.
> For full details, see the original files linked in each section.

## Project Overview

- MusicBrainz Picard user documentation
- Built with Sphinx using RestructuredText (.rst)
- Published via ReadTheDocs
- License: CC0 1.0
- **Source:** `README.md`

## Repository Structure

- Root: config files, index.rst, dev_utils.py
- Directories: documentation topics (about_picard/, config/, etc.)
- `_locale/`: translation POT/PO files
- `_project_documentation/`: this file's source docs
- **Source:** `_project_documentation/REPOSITORY_STRUCTURE.md`

## Branch Strategy

- `main`: current docs, published as "latest"
- `v{major}.{minor}`: version branches, auto-published
- `next_version`: collects changes for next major release
- Working branches: temporary, no auto-build
- **Source:** `_project_documentation/SETUP_AND_PROCESSING.md`

## Documentation Style

- Use .rst files (not Markdown)
- Heading hierarchy: `=` → `-` → `+` → `'`
- 3-space indentation, no tabs
- Single space between sentences
- Use list-tables over simple tables
- Code blocks: use `.. code-block::` directive
- Images: PNG format, in `images/` subdirectory
- **Source:** `_project_documentation/DOCUMENTATION_STYLE_GUIDE.md`

## Development Commands

- `python dev_utils.py test rst`: lint RST files
- `python dev_utils.py build html`: build HTML docs
- `python dev_utils.py build pot`: update translation templates
- `python dev_utils.py clean html`: reset HTML build
- `python dev_utils.py stage`: stage translation files for git
- **Source:** `_project_documentation/DEV_UTILS.md`

## PR Guidelines

- Target `main` for current version changes
- Target `v{major}.{minor}` for prior version fixes
- RST lint runs on PR to main/version branches
- Include alt text for images
- Use relative links for `:doc:` references
- **Source:** `_project_documentation/PROJECT_WORKFLOW.md`

## Translation Process

- Weblate connects to `main` branch
- Run `build pot` after merging to update templates
- Translations merge automatically from Weblate
- Prior version translations go to `v{major}.{minor}` branches
- **Source:** `_project_documentation/PROJECT_WORKFLOW.md`

## Publishing

- Pushes to `main` → "latest" version on website
- Pushes to `v{major}.{minor}` → versioned docs on website
- Use "nobuild" in commit message to skip build
- **Source:** `_project_documentation/PUBLISHING_DOCUMENTATION.md`

## Roles

- Editor: content, structure, translations, publishing
- Maintainers: assist editor
- Reviewers: technical/grammar quality
- Translators: language translations via Weblate
- Content Contributors: submit PRs
- **Source:** `_project_documentation/ROLES_AND_RESPONSIBILITIES.md`

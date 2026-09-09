# AGENTS.md - Picard Documentation Project

RST-only Sphinx manual for MusicBrainz Picard (HTML + PDF on ReadTheDocs, gettext translations via Weblate). Everything is authored in restructured text; Sphinx is configured to also accept `.md`, but the project is RST-only — write RST.

- License: CC0 1.0
- **Source:** `README.md`

## Repository Structure

- Root: config files, index.rst, dev_utils.py
- Directories: documentation topics (about_picard/, config/, etc.)
- `_locale/`: translation POT/PO files
- `_project_documentation/`: this file's source docs
- **Source:** `_project_documentation/REPOSITORY_STRUCTURE.md`

## Branches and Publishing

- `main` is published as "latest" on ReadTheDocs. Target for almost all PRs.
- `v{major}.{minor}` branches are published as versioned pages; target one only when a change applies to an older released version.
- `next_version` stages pre-release major-version content; not published.
- Use `nobuild` in a commit message to cancel the ReadTheDocs rebuild — don't use it in doc commits.
- **Source:** `_project_documentation/SETUP_AND_PROCESSING.md`, `_project_documentation/PUBLISHING_DOCUMENTATION.md`

## Commands (run from repo root)

- `python dev_utils.py test rst` — the RST lint gate (also CI + pre-commit). Use `-i` to not fail on warnings, `-v` for INFO.
- `python dev_utils.py test sphinx` — Sphinx test build.
- `python dev_utils.py build html` — build into `_build/html`; verify locally before pushing (`fail_on_warning: true` on RTD).
- `python dev_utils.py build map` — regenerate tag mapping (see gotchas).
- `python dev_utils.py build pot` — regenerate POT files and update PO files after doc merges (drives Weblate).
- `python dev_utils.py clean html` — reset HTML build.
- `python dev_utils.py stage --rst` — stage translation files (and RST) in a sensible way.
- `pre-commit run --all-files` — run the full local hook set (rstcheck, sphinx-lint, rst-backticks, `test rst`).
- **Source:** `_project_documentation/DEV_UTILS.md`

## Gotchas

- NEVER hand-edit `appendices/tag_mapping.rst` or `_static/MusicBrainz_Picard_Tag_Map.{html,xlsx}` — all generated from `tag_mapping.py` via `build map`.
- NEVER hand-edit `.po`/`.pot` files; regenerate with `build pot`. `.mo` files are gitignored build artifacts.
- Local HTML build must be warning-free — ReadTheDocs fails builds on any warning (broken refs, headers, etc.).
- Images live in a topic-local `images/` dir as PNG with no spaces. Translations use `name.{lang}.ext` (e.g. `image.fr.jpg`) but keep referencing the English name in RST.
- `conf.py:35` holds the documented Picard release line (currently `version = 'v3.0'`); bump it with each new documented version.
- **Source:** `_project_documentation/SETUP_AND_PROCESSING.md`

## RST Style (enforced by tooling/CI)

- One top-level title per file; heading adornments strictly `=` → `-` → `+` → `'`, never skip a level, underline must be >= title length.
- 3-space indentation, no tabs.
- Prefer long unwrapped lines and a single space between sentences.
- Internal links: `:doc:` (pages) and `:ref:` (sections/labels) with relative paths, never hardcoded paths. Use `:kbd:`, `:guilabel:`, `:menuselection:` roles.
- Code blocks via `.. code-block:: <lang>` with an explicit language (custom `taggerscript` available; `none` if nothing fits), never bare indented blocks.
- Prefer `list-table::` over grid tables; every image needs an `:alt:`; images use `.. only:: not latex` / `.. only:: latex` variants for scaling.
- **Source:** `_project_documentation/DOCUMENTATION_STYLE_GUIDE.md`

## Translation Process

- Weblate connects to `main` branch.
- Run `build pot` after merging to update templates.
- Translations merge automatically from Weblate.
- Prior version translations go to `v{major}.{minor}` branches.
- **Source:** `_project_documentation/PROJECT_WORKFLOW.md`

## PR Guidelines

- Target `main` for current version changes.
- Target `v{major}.{minor}` for prior version fixes.
- RST lint runs on PR to main/version branches.
- Include alt text for images.
- Use relative links for `:doc:` references.
- **Source:** `_project_documentation/PROJECT_WORKFLOW.md`

## Roles

- Editor: content, structure, translations, publishing.
- Maintainers: assist editor.
- Reviewers: technical/grammar quality.
- Translators: language translations via Weblate.
- Content Contributors: submit PRs.
- **Source:** `_project_documentation/ROLES_AND_RESPONSIBILITIES.md`

## Canonical References (read before big edits)

- `_project_documentation/DOCUMENTATION_STYLE_GUIDE.md` — full style/formatting rules
- `_project_documentation/DEV_UTILS.md` — all dev_utils.py commands and options
- `_project_documentation/REPOSITORY_STRUCTURE.md` — repository layout
- `_project_documentation/SETUP_AND_PROCESSING.md` — branch model, version workflow, translations
- `_project_documentation/PROJECT_WORKFLOW.md` — PR and translation workflow
- `_project_documentation/PUBLISHING_DOCUMENTATION.md` — publishing details
- `_project_documentation/ROLES_AND_RESPONSIBILITIES.md` — contributor roles

.. MusicBrainz Picard Documentation Project

Options — Sessions
==================

Location: ``Options → Advanced → Sessions``

Settings
--------

- Sessions folder path (leave empty for default)

  - Sets the base folder for session files. Empty uses the default ``<config>/sessions``.

- Honor local edits and placement on load (no auto-matching)

  - Preserves your saved layout and manual edits during restore. Disables MBID-based auto-matching while restoring.

- Load last saved session on startup

  - If enabled, Picard will load the most recently used session at launch (if still available).

- Auto-save session every N minutes (0 disables)

  - Periodically saves the session to the last used path, or to an autosave path in the sessions folder.

- Attempt to keep a session backup on unexpected shutdown

  - On exit, Picard attempts a best-effort backup to ``autosave.mbps.gz`` in the sessions folder.

- Include MusicBrainz data in saved sessions (warm cache)

  - Embeds release data for loaded albums into the session so restore can be instant and work offline.

- Do not make MusicBrainz requests on restore (faster loads, risk of stale data)

  - When used with the embedded data option, restores are fast and fully offline. If a referenced album has no embedded data, it will not be loaded without network access.

Related UI
----------

- File → Load Session…
- File → Recent Sessions
- File → Save Session / Save Session As…
- File → New Session

Reference
---------

Feature PR: `Allow user to save/load current Picard session <https://github.com/metabrainz/picard/pull/2731>`_.

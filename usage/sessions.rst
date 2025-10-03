.. MusicBrainz Picard Documentation Project

Sessions
========

Picard can save and restore your current workspace state as a session file. Sessions preserve file placement (unclustered, clusters, albums, specific tracks, and standalone recordings), your manual metadata edits, and selected configuration options so you can resume work later.

.. note::
   Session files use the ``.mbps.gz`` extension and are gzip-compressed YAML. Only user-visible tags are stored; internal tags are excluded.

File menu actions
-----------------

- ``File → Load Session…``: Open a session file and restore its state. If there is an active session, Picard will prompt you to save before loading the new one.
- ``File → Recent Sessions``: Quickly reopen one of the most recent session files. Use "Clear Recent Sessions" to empty the list.
- ``File → Save Session``: Save the current session to the last used file. If none, Picard will prompt for a path.
- ``File → Save Session As…``: Always prompt for a path. When there is no prior session file, Picard suggests a sensible default filename based on the first detected artist or a timestamp.
- ``File → New Session``: Close the current session (clears files, clusters and albums). You will be prompted to save if there is content to preserve.

What gets saved
---------------

- **File placement**: Unclustered, in clusters, on albums, on specific tracks, and standalone recordings (NAT).
- **Manual edits (overrides)**: Only your changes versus Picard’s base/scripted metadata are stored, not the entire tag set.
- **Unmatched albums**: Albums loaded into Picard without matched files are preserved.
- **UI state**: Album expansion state in the album view.
- **Core options snapshot**: The current values of Rename Files, Move Files, and Don’t Write Tags.
- **Optional MusicBrainz cache**: If enabled in settings, Picard embeds release data for loaded albums so sessions can be restored without waiting for online lookups.

Offline and fast restores
-------------------------

- To enable fully offline restores, turn on both:

  - "Include MusicBrainz data in saved sessions (warm cache)"
  - "Do not make MusicBrainz requests on restore"

  Picard will reconstruct albums from the embedded cache and skip web requests. If an album referenced by the session has no embedded cache and network requests are disabled, that album cannot be loaded and its referenced files will not be auto-matched to it.

- With online access, Picard can still preload from the embedded cache and then refresh data from MusicBrainz for accuracy.

Safe restore of local work
--------------------------

If "Honor local edits and placement on load (no auto-matching)" is enabled, Picard will not auto-match files by existing MBIDs during restore. Files will be placed exactly as saved, and your unsaved edits are preserved and re-applied.

Session storage location
------------------------

By default, Picard stores sessions in the ``sessions`` folder under your configuration directory. You can set a custom folder in Options → Advanced → Sessions. Recent and last-used paths are remembered for convenience.

Tips and notes
--------------

- Recent Sessions lists up to five items. If a file in the list no longer exists and you select it, Picard will notify you and remove it from the list.
- New Session clears the last used session path. After this, Save Session will prompt for a file (use Save Session As… to choose a new path at any time).
- Autosave: When enabled, Picard periodically saves to the last session file or to an ``autosave.mbps.gz`` in the sessions folder if no file is known.
- Crash/exit backup: If enabled, Picard attempts a best-effort backup to ``autosave.mbps.gz`` on exit.
- Only a small set of core options (Rename/Move/Don’t Write Tags) are stored inside the session. All other settings remain global; use Option Profiles if you need different configurations.
- Privacy: Session files include absolute file paths and your manual tag edits. Avoid sharing session files unless you are comfortable exposing that information.

Reference
---------

This feature originates from PICARD-3118. See pull request `Allow user to save/load current Picard session <https://github.com/metabrainz/picard/pull/2731>`_.

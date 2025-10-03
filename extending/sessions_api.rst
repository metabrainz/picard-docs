.. MusicBrainz Picard Documentation Project

Sessions API (technical)
========================

This page describes Picard’s session API for developers and advanced users. It provides programmatic access to export the current workspace state, save it to disk, and load it later.

Overview
--------

- Module: ``picard.session.session_manager``

  - ``export_session(tagger) -> dict``
  - ``save_session_to_path(tagger, path) -> None``
  - ``load_session_from_path(tagger, path) -> None``

Session files
-------------

- Format: gzip-compressed UTF‑8 YAML
- Extension: ``.mbps.gz``
- Version: ``version: 1``
- Only user-visible tags are exported (internal tags starting with ``~`` are excluded).

Python usage
------------

Save to a known path:

.. code-block:: python

   from picard.session.session_manager import save_session_to_path

   # tagger is the running Picard application instance
   save_session_to_path(tagger, "/path/to/my_session.mbps.gz")

Load a session:

.. code-block:: python

   from picard.session.session_manager import load_session_from_path

   load_session_from_path(tagger, "/path/to/my_session.mbps.gz")

Export to a Python dict (without writing to disk):

.. code-block:: python

   from picard.session.session_manager import export_session

   data = export_session(tagger)
   # inspect or modify ``data`` before saving if needed

Top-level schema
----------------

Minimal example (YAML, before gzip):

.. code-block:: yaml

   version: 1
   options:
     rename_files: false
     move_files: false
     dont_write_tags: false
   items:
     - file_path: /absolute/path/to/file.flac
       location:
         type: track
         album_id: 01234567-89ab-cdef-0123-456789abcdef
         recording_id: 89abcdef-0123-4567-89ab-cdef01234567
       metadata:
         tags:
           title: [My Edited Title]
   album_track_overrides: {}
   album_overrides: {}
   unmatched_albums: []
   expanded_albums: []
   mb_cache: {}

Field reference
---------------

- ``version``: Session format version (``1``).
- ``options``: Snapshot of core file-processing flags: ``rename_files``, ``move_files``, ``dont_write_tags``.
- ``items``: List of file entries with:

  - ``file_path``: Absolute path string.
  - ``location``: Dict with one of the following ``type`` values:

    - ``unclustered``
    - ``cluster`` (plus ``cluster_title`` and ``cluster_artist``)
    - ``album_unmatched`` (plus ``album_id``)
    - ``track`` (plus ``album_id`` and ``recording_id``)
    - ``nat`` (standalone recording; plus ``recording_id``)
  - ``metadata.tags``: Per-file tag deltas (lists of values); internal/excluded tags are omitted.
- ``album_track_overrides``: ``{album_id: {track_id: {tag: [values]}}}`` for per-track manual edits.
- ``album_overrides``: ``{album_id: {tag: [values]}}`` for album-level manual edits.
- ``unmatched_albums``: List of album MBIDs that should be shown even without matched files.
- ``expanded_albums``: Album IDs whose UI nodes were expanded.
- ``mb_cache``: Optional embedded MusicBrainz release data keyed by album MBID (used for offline/fast restore).

Behavioral flags (settings)
---------------------------

The loader respects Picard settings that influence restore behavior:

- ``session_safe_restore``: When true, disables MBID-based auto-matching during restore to honor saved placement and edits.
- ``session_include_mb_data`` + ``session_no_mb_requests_on_load``: When both true, restore uses only embedded data and skips network requests (fully offline; albums without embedded cache are skipped).

Lower-level components (advanced)
---------------------------------

- ``picard.session.session_exporter.SessionExporter``
- ``picard.session.session_loader.SessionLoader`` (orchestrates reading, grouping, loading, overrides, and UI state)
- ``picard.session.constants.SessionConstants`` (``SESSION_FILE_EXTENSION``, location types, retry delays)
- ``picard.session.metadata_handler.MetadataHandler`` (helpers for tag deltas application)

End-to-end: custom persist with low-level components
------------------------------------------------------------

The following example shows how to export, write, and later restore a session using the lower-level components directly.

.. code-block:: python

   from __future__ import annotations

   import gzip
   import os
   import tempfile
   from pathlib import Path

   import yaml

   from picard.const.appdirs import sessions_folder
   from picard.session.constants import SessionConstants
   from picard.session.session_exporter import SessionExporter
   from picard.session.session_loader import SessionLoader

   def save_session_low_level(tagger, path: str | Path) -> Path:
       """Export current state and write a .mbps.gz file (atomic write).

       Returns the final path written.
       """
       target = Path(path)
       if not str(target).lower().endswith(SessionConstants.SESSION_FILE_EXTENSION):
           target = Path(str(target) + SessionConstants.SESSION_FILE_EXTENSION)

       # 1) Export to Python dict
       data = SessionExporter().export_session(tagger)

       # 2) Serialize to YAML (UTF-8) and gzip-compress
       yaml_text = yaml.dump(data, allow_unicode=True, sort_keys=False)
       compressed = gzip.compress(yaml_text.encode("utf-8"))

       # 3) Atomic write (temp file + replace)
       target.parent.mkdir(parents=True, exist_ok=True)
       temp_path = None
       try:
           with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.stem + "_", suffix=target.suffix, delete=False) as tf:
               temp_path = Path(tf.name)
               temp_path.write_bytes(compressed)
           temp_path.replace(target)
       finally:
           if temp_path and temp_path.exists() and temp_path != target:
               with contextlib.suppress(OSError):
                   temp_path.unlink()
       return target

   def load_session_low_level(tagger, path: str | Path) -> None:
       """Restore a session from file using the orchestrator directly."""
       loader = SessionLoader(tagger)
       loader.load_from_path(path)
       loader.finalize_loading()

   # Example roundtrip
   def roundtrip_example(tagger) -> None:
       base = Path(sessions_folder())
       path = base / "example_roundtrip"  # extension appended automatically
       final_path = save_session_low_level(tagger, path)
       # Later (or immediately) restore:
       load_session_low_level(tagger, final_path)

Notes
-----
- The exporter respects settings such as "Include MusicBrainz data in saved sessions" and will embed cached release data when enabled.
- The loader honors safe-restore and offline flags (see Behavioral flags below).

- Paths are stored as absolute file paths.
- The API aims to be stable but may evolve; consult release notes for changes.

Reference
---------

Feature PR: `Allow user to save/load current Picard session <https://github.com/metabrainz/picard/pull/2731>`_.

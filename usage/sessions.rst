.. MusicBrainz Picard Documentation Project

:index:`Sessions Management <sessions management>`
===================================================

As of version 3, Picard can save and restore your current workspace state as a session file. Sessions preserve file placement (unclustered, clusters, albums, specific tracks, and standalone recordings), your manual metadata edits, and selected configuration options so you can resume work later.

.. note::

   Session files use the ``.mbps.gz`` extension and are gzip-compressed YAML. Only user-visible tags are stored; internal tags are excluded.


File menu actions
-----------------

The following actions are available under the :menuselection:`File` menu:

- :menuselection:`Load Session…`: Open a session file and restore its state. If there is an active session, Picard will prompt you to save before loading the new one.
- :menuselection:`Recent Sessions`: Quickly reopen one of the most recent session files. Use "Clear Recent Sessions" to empty the list.
- :menuselection:`Save Session`: Save the current session to the last used file. If none, Picard will prompt for a path.
- :menuselection:`Save Session As…`: Always prompt for a path. When there is no prior session file, Picard suggests a default filename based on the first detected artist or a timestamp.
- :menuselection:`New Session`: Close the current session (clears files, clusters and albums). You will be prompted to save if there is content to preserve.


What gets saved
---------------

- **File placement**: Unclustered, in clusters, on albums, on specific tracks, and standalone recordings (NAT).
- **Manual edits (overrides)**: Only your changes versus Picard's base/scripted metadata are stored, not the entire tag set.
- **Unmatched albums**: Albums loaded into Picard without matched files are preserved.
- **UI state**: Album expansion state in the album view.
- **Core options snapshot**: The current values of Rename Files, Move Files, and Don't Write Tags.
- **Optional MusicBrainz cache**: If enabled in settings, Picard includes release data for loaded albums so sessions can be restored without waiting for online lookups.


Offline and fast restores
-------------------------

To enable fully offline restores, turn on both:
- "Include MusicBrainz data in saved sessions"
- "Do not make MusicBrainz requests on restore"

Picard will reconstruct albums from the embedded cache and skip web requests. If an album referenced by the session has no embedded cache and network requests are disabled, that album cannot be loaded and its referenced files will not be auto-matched.

With online access, Picard can still preload from the embedded cache and then refresh data from MusicBrainz for accuracy.


Safe restore of local work
--------------------------

If "No auto-matching on load" is enabled, Picard will not auto-match files by existing MBIDs during the restore. Files will be placed exactly as saved, and your unsaved edits are preserved and re-applied.


Session storage location
------------------------

By default, Picard stores sessions in the ``sessions`` subdirectory under your configuration directory. You can set a custom directory in the Advanced / Sessions option settings page. Recent and last-used paths are remembered for convenience.


.. note::

   "Recent Sessions" lists up to five items. If a file in the list no longer exists and you select it, Picard will notify you and remove it from the list.

   "New Session" clears the last used session path. After this, "Save Session" will prompt for a file (use "Save Session As…" to choose a new path at any time).

   Only a small set of core options (Rename/Move/Don't Write Tags) are stored inside the session. All other settings remain global; use ":doc:`Option Profiles <option_profiles>`" if you need different configurations.

.. warning::

   Session files include absolute file paths and your manual tag edits. Please avoid sharing session files unless you are comfortable exposing that information.

.. seealso::

   For additional information about sessions settings please see the ":doc:`../config/options_sessions`" section under Configuration.

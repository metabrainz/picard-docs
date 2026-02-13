.. MusicBrainz Picard Documentation Project

:index:`Sessions <configuration; sessions, sessions; configuration>`
=============================================================================

As of Picard v3 you can save and restore your current workspace state as a session file. Sessions preserve file placement (unclustered, clusters, albums, specific tracks, and standalone recordings), your manual metadata edits, and selected configuration options so you can resume work later.

.. only:: not latex

   .. image:: images/options-sessions.png
      :align: center

.. only:: latex

   .. image:: images/options-sessions.png
      :width: 75%
      :align: center

The following settings determine how the session files are managed:

**Sessions directory**

   The directory where the session files are stored.

**Auto-save every N minutes**

   The interval in minutes between the times the current session is saved. Sessions will not be automatically saved when the interval is set to 0.

   When enabled, Picard periodically saves to the last known session file, or to ``autosave.mbps.gz`` in the sessions folder if no file is known.

**Attempt session backup on unexpected shutdown**

   When enabled, the system will attempt to save the current session to ``autosave.mbps.gz`` in the sessions folder if Picard is unexpectedly shut down.

**Include MusicBrainz data in saved sessions**

   When enabled, the release data for loaded albums will be included in the session information. This will speed up the session restore, and also allows continuing the work offline.

**Do not make MusicBrainz requests on restore**

   When enabled, requests to MusicBrainz will not be made when restoring the session.

**Load last saved session on startup**

   When enabled, Picard will load the most recently used session at startup (if the session information file is still available).

**No auto-matching on load**

   When enabled, Picard will not perform any MBID-based auto-matching when restoring the session.

.. seealso::

   For additional information about sessions please see the ":doc:`../usage/sessions`" section under Usage.

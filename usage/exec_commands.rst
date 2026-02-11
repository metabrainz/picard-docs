.. MusicBrainz Picard Documentation Project

:index:`Executable Commands <commands; executable, executable commands>`
========================================================================

Picard can accept commands for processing by specifying them on the command line using the ``-e`` option or loading them from a text file. Commands are case-insensitive, and are processed sequentially in the order that they are received. The executable commands that Picard recognizes are:

:index:`CLEAR_LOGS <executable commands; CLEAR_LOGS>`
-----------------------------------------------------

| Usage: **CLEAR_LOGS**
| Implemented: Picard 2.9

Clear all entries from Picard's log. This is the equivalent of clicking the :guilabel:`Clear Log` button from the log viewing screen opened using the :menuselection:`"Help --> View Error/Debug Log"` command.

:index:`CLUSTER <executable commands; CLUSTER>`
-----------------------------------------------

| Usage: **CLUSTER**
| Implemented: Picard 2.9

Cluster all files in the cluster pane. This is the equivalent of using the :menuselection:`"Tools --> Cluster"` command.

:index:`FINGERPRINT <executable commands; FINGERPRINT>`
-------------------------------------------------------

| Usage: **FINGERPRINT**
| Implemented: Picard 2.9

Calculate acoustic fingerprints for all (matched) files in the album pane. This is the equivalent of using the :menuselection:`"Tools --> Generate AcoustID Fingerprints"` command.

:index:`FROM_FILE <executable commands; FROM_FILE>`
---------------------------------------------------

| Usage: **FROM_FILE <file path>**
| Implemented: Picard 2.9

Load commands from a file. The file path can be either an absolute or relative path to a text file containing the commands to be executed. Each command to be processed must be on a separate line along with its arguments (if applicable). Blank lines and lines beginning with an octothorpe (#) are ignored. Command files can include other command files by specifying them with another ``FROM_FILE`` command. Circular references (by including a command file that is currently being processed) are ignored and will be logged as a warning.

For example, you may have a file named ``commands.txt`` containing the standard commands that you want to use when processing each directory, such as:

.. code::

   # Try clustering and lookup the clusters first
   CLUSTER
   LOOKUP_CLUSTERED

   # Save matched clusters
   SAVE_MATCHED

   # Calculate and submit fingerprints for the matched files
   FINGERPRINT
   SUBMIT_FINGERPRINTS

   # Clean up and remove the saved files
   REMOVE_SAVED
   REMOVE_EMPTY

   # Try scanning the remaining files to find matches
   SCAN

   # Save matched files from the scans
   SAVE_MATCHED

   # Clean up and remove the saved files
   REMOVE_SAVED
   REMOVE_EMPTY

   # Any files remaining in the cluster pane could not be
   # matched automatically

You could then process a directory by starting Picard with the command:

.. code::

   picard -e LOAD path/to/directory/of/unprocessed/files -e FROM_FILE commands.txt


:index:`LOAD <executable commands; LOAD>`
-----------------------------------------

| Usage: **LOAD <supported MBID/URL or path to a file/directory>**
| Implemented: Picard 2.9

Load one or more files/directories/MBIDs/URLs to Picard. This is similar to including the file, directory path, URL or MBID on the command line.

Files and directories are specified including the path (either absolute or relative) to the file or directory, and may include drive specifiers. They can also be specified using the ``file://`` prefix. URLs are specified by using either the ``http://`` or ``https://`` prefix. MBIDs are specified in the format ``mbid://<entity_type>/<mbid>`` where ``<entity_type>`` is one of "release", "artist" or "track" and ``<mbid>`` is the MusicBrainz Identifier of the entity.

If a specified item contains a space, it must be enclosed in quotes such as ``"/home/user/music/my song.mp3"``.

:index:`LOOKUP <executable commands; LOOKUP>`
---------------------------------------------

| Usage: **LOOKUP [clustered|unclustered|all]**
| Implemented: Picard 2.9

Lookup files in the clustering pane. Options are clustered files, unclustered files or all files. If not specified, the command defaults to all files.

This is the equivalent of using the :menuselection:`"Tools --> Lookup"` command.

:index:`LOOKUP_CD <executable commands; LOOKUP_CD>`
---------------------------------------------------

| Usage: **LOOKUP_CD [device/log file]**
| Implemented: Picard 2.9

Read CD from the selected drive or ripper log file, and looks it up on MusicBrainz. If no argument is specified, it defaults to the first (alphabetically) available disc drive.

This is the equivalent of using the :menuselection:`"Tools --> Lookup CD..."` command.

:index:`PAUSE <executable commands; PAUSE>`
-------------------------------------------

| Usage: **PAUSE <number of seconds to pause>**
| Implemented: Picard 2.9

Pause executable command processing for the specified number of seconds.

:index:`QUIT <executable commands; QUIT>`
-----------------------------------------

| Usage: **QUIT \[force\]**
| Implemented: Picard 2.9

The ``QUIT`` command waits until all queued executable commands have completed, and then initiates a shutdown request the same as if the user closed Picard from the user interface. This allows Picard to perform the same checks for unsaved files and such. When 'force' is entered as an argument to the command, Picard will bypass the unsaved files check.

Once a ``QUIT`` command has been queued, Picard will not queue any further executable commands. If the user cancels the ``QUIT`` from the unsaved files check dialog, the system will allow more commands to be queued.

:index:`REMOVE <executable commands; REMOVE>`
---------------------------------------------

| Usage: **REMOVE <path to one or more files>**
| Implemented: Picard 2.9

Removes the specified file(s) from Picard. Does nothing if no arguments provided.

:index:`REMOVE_ALL <executable commands; REMOVE_ALL>`
-----------------------------------------------------

| Usage: **REMOVE_ALL**
| Implemented: Picard 2.9

Removes all files from Picard.

:index:`REMOVE_EMPTY <executable commands; REMOVE_EMPTY>`
---------------------------------------------------------

| Usage: **REMOVE_EMPTY**
| Implemented: Picard 2.9

Removes all empty clusters and albums.

:index:`REMOVE_SAVED <executable commands; REMOVE_SAVED>`
---------------------------------------------------------

| Usage: **REMOVE_SAVED**
| Implemented: Picard 2.9

Removes all saved files from the album pane.

:index:`REMOVE_UNCLUSTERED <executable commands; REMOVE_UNCLUSTERED>`
---------------------------------------------------------------------

| Usage: **REMOVE_UNCLUSTERED**
| Implemented: Picard 2.9

Removes all unclustered files from the cluster pane.

:index:`SAVE_MATCHED <executable commands; SAVE_MATCHED>`
---------------------------------------------------------

| Usage: **SAVE_MATCHED**
| Implemented: Picard 2.9

Saves all matched files from the album pane.

:index:`SAVE_MODIFIED <executable commands; SAVE_MODIFIED>`
-----------------------------------------------------------

| Usage: **SAVE_MATCHED**
| Implemented: Picard 2.9

Saves all modified files from the album pane.

:index:`SCAN <executable commands; SCAN>`
-----------------------------------------

| Usage: **SCAN**
| Implemented: Picard 2.9

Scans all files in the cluster pane. This is the equivalent of using the :menuselection:`"Tools --> Scan"` command.

:index:`SHOW <executable commands; SHOW>`
-----------------------------------------

| Usage: **SHOW**
| Implemented: Picard 2.9

Make the running instance of Picard the currently active window.

:index:`SUBMIT_FINGERPRINTS <executable commands; SUBMIT_FINGERPRINTS>`
-----------------------------------------------------------------------

| Usage: **SUBMIT_FINGERPRINTS**
| Implemented: Picard 2.9

Submits outstanding acoustic fingerprints for all (matched) files in the album pane. This is the equivalent of using the :menuselection:`"Tools --> Submit AcoustIDs"` command.

:index:`WRITE_LOGS <executable commands; WRITE_LOGS>`
-----------------------------------------------------

| Usage: **WRITE_LOGS <path to output file>**
| Implemented: Picard 2.9

Writes the Picard logs to the specified output file. This is the equivalent of using the :guilabel:`Save As...` button from the log viewing screen opened using the :menuselection:`"Help --> View Error/Debug Log"` command.

.. MusicBrainz Picard Documentation Project

:index:`Command and Batch Processing <command processing, batch processing, processing; batch>`
===============================================================================================

As of version 2.9, Picard will try to only run a single instance of the program at a time. When the program is started, it checks to see if there is another instance of that version, configuration file and plugin startup status ``-P`` already running. If the same version is already running, any files or directories specified on the command line of the new instance, along with any executable commands specified with the ``-e`` or ``-exec`` options will be passed to the already running instance for processing and the new duplicate instance will be shut down. This allows batch processing of files to be initiated automatically from other processes. If there is no instance of that version already running, Picard will start normally.

For example if there is an instance of Picard running and a second instance is started with the command line:

.. code::

   picard -e load mbid://release/dbd0ce67-cae6-33eb-8f5a-1143a30c2353

the load command will be passed to the running instance to load the specified release, and the second instance will be closed.

This allows the user to set up dynamic batch processing of commands to automate the tagging process, especially when used with the ``FROM_FILE`` command to load a standard processing command sequence such as:

.. code::

   CLUSTER
   LOOKUP_CLUSTERED
   SAVE_MATCHED
   REMOVE_SAVED
   REMOVE_EMPTY

or:

.. code::

   LOOKUP_CD path/to/ripper.log
   SAVE_MATCHED
   FINGERPRINT
   SUBMIT_FINGERPRINTS
   REMOVE_SAVED
   REMOVE_EMPTY

or even something like:

.. code::

   # Load a directory of files to process
   LOAD path/to/directory/of/unprocessed/files

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

Please see the :doc:`exec_commands` section for details regarding the commands available for execution.

.. toctree::
   :hidden:

   exec_commands

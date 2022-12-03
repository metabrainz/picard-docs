.. MusicBrainz Picard Documentation Project

Appendix C: :index:`Command Line Options <pair: command line; options>`
========================================================================

Picard can be started from the command line with the following arguments:

.. code::

   picard [-h] [-c CONFIG_FILE] [-d] [-N] [-P] [-s] [-v] [-V] [FILE_OR_URLs] [-e COMMANDs]

where the options are:

.. option:: -h, --help

   show a help message and exit

.. option:: -c CONFIG_FILE, --config-file CONFIG_FILE

   location of the configuration file to use (implies ``--stand-alone-instance``)

.. option:: -d, --debug

   enable debug-level logging

.. option:: -e COMMAND, --exec COMMAND

   execute one or more COMMANDs at start-up (see :doc:`/usage/exec_commands` for more information)

.. option:: -M, --no-player

   disable built-in media player

.. option:: -N, --no-restore

   do not restore window positions or sizes

.. option:: -P, --no-plugins

   do not load any plugins (starts a stand-alone instance)

.. option:: -s, --stand-alone-instance

   force Picard to create a new, stand-alone instance (see :doc:`/usage/command_processing` for more information)

.. option:: -v, --version

   display the version information and exit

.. option:: -V, --long-version

   display the long version information and exit

.. describe:: FILE_OR_URL

   one or more files, directories, URLs and MBIDs to load

   .. note::

      Files and directories are specified including the path (either absolute or relative) to the file or directory, and may include drive specifiers.
      They can also be specified using the ``file://`` prefix.
      URLs are specified by using either the ``http://`` or ``https://`` prefix.
      MBIDs are specified in the format ``mbid://<entity_type>/<mbid>`` where ``<entity_type>`` is one of "release", "artist"
      or "track" and ``<mbid>`` is the MusicBrainz Identifier of the entity.

      If a specified item contains a space, it must be enclosed in quotes such as ``"/home/user/music/my song.mp3"``.

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

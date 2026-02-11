.. MusicBrainz Picard Documentation Project

Appendix B: :index:`Command Line Options <pair: command line; options>`
=======================================================================

Picard can be started from the command line with the following arguments:

.. code-block:: bash

   run_picard.py [-h] [-a AUDIT] [-c CONFIG_FILE] [-d] [-e COMMAND [COMMAND ...]] [-M] [-N] [-P] [--no-crash-dialog] [-s] [-v] [-V] [FILE_OR_URL ...]

where the options are:

.. option:: -h, --help

   show a help message and exit

.. option:: -a AUDIT, --audit AUDIT

   audit events passed as a comma-separated list, prefixes supported, use "all" to match any event. See the `Python Documentation <https://docs.python.org/3/library/audit_events.html#audit-events>`_ for more information.

.. option:: -c CONFIG_FILE, --config-file CONFIG_FILE

   location of the configuration file to use

.. option:: -d, --debug

   enable debug-level logging

.. option:: -e COMMAND, --exec COMMAND

   execute one or more COMMANDs at start-up (see :doc:`../usage/exec_commands` for more information)

.. option:: -M, --no-player

   disable built-in media player

.. option:: -N, --no-restore

   do not restore window positions or sizes

.. option:: -P, --no-plugins

   do not load any plugins

.. option:: --no-crash-dialog

   disable the crash dialog

.. option:: -s, --stand-alone-instance

   force Picard to create a new, stand-alone instance

.. option:: -v, --version

   display the version information and exit

.. option:: -V, --long-version

   display the long version information and exit

.. describe:: FILE_OR_URL

   one or more files, directories, URLs and MBIDs to load

   .. note::

      Files and directories are specified including the path (either absolute or relative) to the file or directory, and may include drive specifiers. They can also be specified using the ``file://`` prefix. URLs are specified by using either the ``http://`` or ``https://`` prefix. MBIDs are specified in the format ``mbid://<entity_type>/<mbid>`` where ``<entity_type>`` is one of "release", "artist" or "track" and ``<mbid>`` is the MusicBrainz Identifier of the entity.

      If a specified item contains a space, it must be enclosed in quotes such as ``"/home/user/music/my song.mp3"``.

.. raw:: latex

   \clearpage

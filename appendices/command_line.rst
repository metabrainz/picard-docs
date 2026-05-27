.. MusicBrainz Picard Documentation Project

Appendix B: :index:`Command Line Options <pair: command line; options>`
=======================================================================

Picard can be started from the command line with the following arguments:

.. code-block:: bash

   run_picard.py [-h] [-a AUDIT] [-c CONFIG_FILE] [-d] [-e COMMAND [COMMAND ...]] [-M] [-N] [-P] [--no-crash-dialog] [--debug-opts] [-s] [-v] [-V] [FILE_OR_URL ...]

where the options are:

.. option:: -h, --help

   show a help message and exit

.. option:: -a AUDIT, --audit AUDIT

   audit events passed as a comma-separated list, prefixes supported, use "all" to match any event. See the `Python Documentation <https://docs.python.org/3/library/audit_events.html#audit-events>`_ for more information.

.. option:: -c CONFIG_FILE, --config-file CONFIG_FILE

   location of the configuration file to use

.. option:: -d, --debug

   enable debug-level logging

.. option:: --debug-opts [OPTIONS]

   comma-separated list of debug options. Use --debug-opts without value to list available options

   .. note::

      The ``plugin_development`` debug option has been specifically designed to assist plugin developers by allowing detailed logging of plugin-related events that would not normally be included in the debug log. This can help developers identify issues and understand the behavior of their plugins within Picard. Debug log entries are useful when a user is trying to understand which plugin is making changes to metadata and such, but extensive debug logging such as that required for troubleshooting a specific plugin can be overwhelming. If detailed debug logging is included, it should be used with the ``api.logger.debug_if()`` method so that it is only logged when the ``plugin_development`` debug option is specified on the command line. For example:

      .. code-block:: python

         # Single message
         self.api.logger.debug_if(DebugOpt.PLUGIN_DEVELOPMENT, "Detailed debug message with no parameters")
         self.api.logger.debug_if(DebugOpt.PLUGIN_DEVELOPMENT, "Resize: %d x %d", width, height)

         # Lazy formatting with msg_func
         self.api.logger.debug_if(DebugOpt.PLUGIN_DEVELOPMENT, msg_func=lambda: "Settings: %s" % expensive())

         # Block guard to skip expensive code entirely when disabled
         if dbg := self.api.logger.debug_if(DebugOpt.PLUGIN_DEVELOPMENT):
             for item in items:
                 dbg("item: %r", item)

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

.. MusicBrainz Picard Documentation Project

:index:`Starting Picard <starting>`
===================================

Once Picard has been installed on your system, most of the time you will be starting it by clicking an icon on your desktop or in a start menu. This will run the program using the default location for the configuration file and configured logging level. Picard can also be started from a command line prompt with some overrides available. From the command line, you can also specify files or directories to load into Picard for processing. Please see :doc:`../appendices/command_line` for more details about the available options.

As of version 2.9, Picard will try to only run a single instance of the program at a time. When the program is started, it checks to see if there is another instance of that version, configuration file and plugin startup status ``-P`` already running. If the same version is already running, any files or directories specified on the command line of the new instance, along with any executable commands specified with the ``-e`` or ``--exec`` options will be passed to the already running instance for processing and the new duplicate instance will be shut down. This allows batch processing of files to be initiated automatically from other processes. If there is no instance of that version already running, Picard will start normally.

Additionally, Picard can be started in "stand-alone" mode, in which case it neither sends information to an already running instance nor accepts information from another instance.

Instances started with command-line argument ``-s / --stand-alone`` always start as stand-alone.

If there is already an instance running when another instance is started that doesn't result in a stand-alone instance, any of the command-line overrides ``-d / --debug``, ``-M / --no-player`` or ``-N / --no-restore`` of the new duplicate instance will be ignored, and only the specified files or directories and executable commands (if any) will be passed to the running instance for processing. Similarly, if a primary instance has been started with any of these overrides specified on the command line, starting a subsequent instance of that version without the override will not modify the user interface settings of the currently running instance.

All instances started with the ``-h / --help``, ``-v / --version`` or ``-V / --long-version`` command line arguments will always output the requested product information and exit, regardless of whether or not another instance is running.

Please refer to the :doc:`../usage/command_processing` section for more information.

.. raw:: latex

   \clearpage

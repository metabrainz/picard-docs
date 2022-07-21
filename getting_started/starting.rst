.. MusicBrainz Picard Documentation Project

:index:`Starting Picard <starting>`
===================================

Once Picard has been installed on your system, most of the time you will be starting it by
clicking an icon on your desktop or in a start menu.  This will run the program using the
default location for the configuration file and configured logging level.  Picard can also
be started from a command line prompt with some overrides available.  From the command line,
you can also specify files or directories to load into Picard for processing.  Please see
:doc:`/appendices/command_line` for more details about the available options.

As of version 3, Picard will try to only run a single instance of the program at a time.
When the program is started, it checks to see if there is another instance of that version
already running.  If the same version is already running, any files or directories specified
on the command line of the new instance will be passed to the already running instance for
processing and the new duplicate instance will be shut down.  This allows batch processing
of files to be initiated automatically from other processes.  If there is no instance of that
version already running, Picard will start normally.  Additionally, Picard can be started in
"stand-alone" mode, in which case it neither sends information to an already running instance
nor accepts information from another instance.

The following cases will always start Picard in stand-alone mode:

- Instances started with command-line argument ``-s / --stand-alone`` always start as stand-alone.

- Instances started with command-line arguments ``-c / --config-file`` and/or ``-P / --no-plugins`` always start as stand-alone.  This is because the arguments provided could result in changes to the configured processing.

- Windows portable instances always start as stand-alone by virtue of them using a different configuration file location than the standard location used for a desktop version of the program.

If there is already an instance running when another instance is started that doesn't result in a
stand-alone instance, any of the command-line overrides ``-d / --debug``, ``-M / --no-player``
or ``-N / -no-restore`` of the new duplicate instance will be ignored, and only the specified
files or directories (if any) will be passed to the running instance for processing.  Similarly,
if a primary instance has been started with any of these overrides specified on the command line,
starting a subsequent instance of that version without the override will not modify the user
interface settings of the currently running instance.

All instances started with the ``-h / --help``, ``-v / --version`` or ``-V / --long-version``
command line arguments will always output the requested product information and exit, regardless of
whether or not another instance is running.

.. warning::

   Picard's stand-alone mode is implemented via the use of an inter-process-communication (IPC) file, which will be named according to the following format: ``$PICARD_NAME_v$PICARD_VERSION_pipe_file``. If this IPC file is deleted, Picard will not exit cleanly and will have to be forcefully terminated. It is strongly suggested that users do not manually interact with this file.

.. raw:: latex

   \clearpage

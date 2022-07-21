.. MusicBrainz Picard Documentation Project

Appendix C: :index:`Command Line Options <pair: command line; options>`
========================================================================

Picard can be started from the command line with the following arguments:

.. code::

   picard [-h] [-c CONFIG_FILE] [-d] [-N] [-P] [-v] [-V] [FILE [FILE ...]]

where the options are:

.. option:: -h, --help

   show a help message and exit

.. option:: -c CONFIG_FILE, --config-file CONFIG_FILE

   location of the configuration file to use (implies ``--stand-alone-instance``)

.. option:: -d, --debug

   enable debug-level logging

.. option:: -M, --no-player

   disable built-in media player

.. option:: -N, --no-restore

   do not restore window positions or sizes

.. option:: -P, --no-plugins

   do not load any plugins (starts a stand-alone instance)
   
.. option:: -s, --stand-alone-instance
                        
   force Picard to create a new, stand-alone instance

.. option:: -v, --version

   display the version information and exit

.. option:: -V, --long-version

   display the long version information and exit

.. describe:: FILE

   the file or files to load

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

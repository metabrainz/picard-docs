.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Appendix 3: Command Line Options
================================

.. index::
   pair: command line; options

Picard can be started from the command line with the following arguments:

.. code::

   picard [-h] [-c CONFIG_FILE] [-d] [-N] [-P] [-v] [-V] [FILE [FILE ...]]

where the options are:

``-h``, ``--help`` show a help message and exit

``-c CONFIG_FILE``, ``--config-file CONFIG_FILE`` location of the configuration file to use

``-d``, ``--debug`` enable debug-level logging

``-M``, ``--no-player`` disable built-in media player

``-N``, ``--no-restore`` do not restore window positions or sizes

``-P``, ``--no-plugins`` do not load any plugins

``-v``, ``--version`` display the version information and exit

``-V``, ``--long-version`` display the long version information and exit

``FILE`` is the file or files to load

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

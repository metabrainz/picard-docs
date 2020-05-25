..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Scripts
=======

.. index::
   single: scripts

There are two types of scripts used in Picard: the file naming script and tagging scripts. These are
managed from the "File Naming" and "Scripting" sections of the :menuselection:`"Options --> Options..."` menu. All scripts are written
using the :doc:`Picard scripting language <../scripting>`. Scripts are often discussed in the
`MetaBrainz Community Forum <https://community.metabrainz.org/>`_, and there is a thread specific to
`file naming and script snippets <https://community.metabrainz.org/t/repository-for-neat-file-name-string-patterns-and-tagger-script-snippets/2786/>`_.

File Naming Script
------------------

.. index::
   pair: file naming; scripts

There is only one file naming script defined in a user’s settings, although it can vary from a simple
one-line script such as ``%album%/%title%`` to a very complex script using different file naming formats
based on different criteria. In all cases, the files will be saved using the text output by the script.

.. note::

   Any new tags set or tags modified by the file naming script will not be written to the output
   files' metadata.

Tagging Scripts
---------------

.. index::
   pair: tagging; scripts

There can be multiple tagging scripts defined in a user’s settings. Individual scripts can be enabled or
disabled, and the order of execution of the scripts can be set. Whenever a script is run automatically (i.e.:
when an album is loaded), it is processed once for each track in the album that triggered the
run. For example, if there are two tagging scripts enabled (A and B) and an album with three tracks is
loaded, the scripts will be processed in the following order:

1. Script A Track 1;
2. Script A Track 2;
3. Script A Track 3;
4. Script B Track 1;
5. Script B Track 2;
6. Script B Track 3.

Metadata updates are not shared between tracks, so you cannot append data from one track to a tag in another
track.

Any new tags set or tags modified by the tagging scripts will be written to the output files' metadata,
unless the tag name begins with an underscore. These "hidden" tags are typically used as variables to hold
temporary values that are used later in either the tagging or file naming scripts. Tagging scripts are run
once for each track in the data, using the metadata for that track.

Tagging scripts can also be run manually by right-clicking either an album or a track in the right-hand pane
in Picard. If run from the album entry, the script is run for each track in the album. If run from an
individual track, the script is only run for that track.

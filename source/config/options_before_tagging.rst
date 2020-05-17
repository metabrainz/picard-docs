..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Before Tagging
==============

.. only:: html

   .. image:: ../images/options-tags.png
      :width: 100 %

**Clear existing tags**

   Checking this will remove all existing metadata and leave your files with only MusicBrainz metadata. Information you
   may have added through another media player such as "genre", "comments" or "ratings" will be removed.

**Remove ID3 tags from FLAC files**

   Check to remove ID3 tags from FLAC files – Vorbis Comments are recommended for FLAC files. Picard will write Vorbis
   Comments to FLAC files regardless of this setting.

**Remove APEv2 tags from MP3 files**

   Check to remove APEv2 tags from MP3 files – ID3 is recommended for MP3 files. Picard will write ID3 tags to MP3 files
   regardless of this setting.

**Preserve these tags from being cleared or overwritten with MusicBrainz data**

   This is an advanced option: If you have tags which you need to preserve, enter their names here to stop Picard from
   overwriting them.

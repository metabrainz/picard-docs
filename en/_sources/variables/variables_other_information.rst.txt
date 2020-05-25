..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Other Information
=================

.. index::
   single: tags; writing

For technical details on how tags are written into files, see `Picard Tag Mapping <https://picard.musicbrainz.org/docs/mappings/>`_.

If you set new variables, these will be saved as new tags in ID3, APEv2 and VORBIS based files. For ID3 based files these will be
saved to, and reloaded from, ID3 user defined text information (TXXX) frames. They will not be saved in ASF, MP4 or WAV based files.

For ID3 based tags (i.e.: MP3 files), you can also set ID3 tags directly from your scripts by setting a special variable starting with
"_id3:". Currently these tags are not loaded into variables when you reload the file into Picard. (*since Picard 0.9*)

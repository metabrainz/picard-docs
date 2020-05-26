.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Other Information
=================

.. index::
   single: tags; writing

For technical details on how tags are written into files, see `Picard Tag Mapping <https://picard.musicbrainz.org/docs/mappings/>`_.

If you set new variables, these will be saved as new tags in ID3, APEv2 and VORBIS based files. For ID3 based files these will be
saved to, and reloaded from, ID3 user defined text information (TXXX) frames. They will not be saved in ASF, MP4 or WAV based files.

For ID3 based tags (i.e.: MP3 files), you can also set ID3 tags directly from your scripts by setting a special variable starting with
"_id3:". Currently these tags are not loaded into variables when you reload the file into Picard. (*since Picard 0.9*)

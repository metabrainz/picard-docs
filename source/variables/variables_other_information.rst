.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Other Information
=================

.. index::
   single: tags; writing

.. only:: html

   For technical details on how tags are written into files, see the :doc:`Picard Tag Mapping <../technical/tag_mapping>` section.

.. only:: latex

   For technical details on how tags are written into files, see the :doc:`Picard Tag Mapping <../technical/tag_mapping_pdf>` section.

If you set variables that are not known to Picard, these will be saved as new tags in ID3, MP4, APEv2 and Vorbis based files.
They will not be saved in ASF based files.

- For ID3 based files these tags will be saved to, and reloaded from, ID3 user defined text information (TXXX) frames.
- For MP4 files these tags will be saved with a prefix of ``----:com.apple.iTunes:``.  This is widely understood by
  other tools to be used for custom tags.
- For Vorbis and APEv2 files these tags will be saved as given.

For ID3 based tags (i.e.: MP3 files), you can also set ID3 tags directly from your scripts by setting a special variable starting with
``_id3:``, e.g. ``%_id3:TXXX:mytag``. Currently these tags are not loaded into variables when you reload the file into Picard (*since Picard 0.9*).

.. note::

   Saving custom tags to MP4 files is supported since Picard 2.3.  Earlier versions will neither save nor load
   custom tags in MP4 files.
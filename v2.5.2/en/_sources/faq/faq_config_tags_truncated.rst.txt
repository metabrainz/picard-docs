.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


My tags are truncated to 30 characters in Windows Media Player!
==================================================================================

Windows Media Player (WMP) can only read ID3v2.3 tags. If you have tagged your files with ID3v2.4 WMP falls back to ID3v1 which has a
limitation of 30 characters per title. Writing ID3v2.3 is the default, but you can configure it in the :doc:`tag options for ID3
<../config/options_tags_compatibility_id3>`.

Prior to version 0.14, Picard's default setting was to write ID3v2.4 to files.

.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`I tagged a file in Picard, but iTunes is not seeing the tags! <itunes>`
==================================================================================

First, you need to force iTunes to re-read the information from your tags and update its library. This is discussed in the `iTunes
Guide <https://musicbrainz.org/doc/iTunes_Guide>`_.

Additionally, iTunes has a known bug in its ID3v2.4 implementation, which makes it unable to read such tags if they also contain
embedded cover art. As a work-around, you can configure Picard to write ID3v2.3 tags.

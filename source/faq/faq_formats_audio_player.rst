.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`The built-in audio player cannot play my file. Which formats does it support? <audio player>`
=========================================================================================================

The formats supported by the built-in audio player depend on the formats supported by your operating system.

**Windows:**

   The supported formats depend on the installed codecs. Depending on the Windows version certain codecs are pre-installed, but you can install
   additional codecs.

   You might want to install the `Directshow Filters for Ogg <https://xiph.org/dshow/downloads/>`_ to add support for Ogg Vorbis, Ogg Speex, Ogg
   Theora, Ogg FLAC, native FLAC, and WebM files.

   .. seealso::

      Additional information is available from  `Microsoft's Codecs FAQ <https://support.microsoft.com/en-us/help/15070/windows-media-player-codecs-frequently-asked-questions>`_.

**Linux:**

   On Linux systems the player uses GStreamer which supports most common audio formats, although some distributions might exclude some codecs due to
   licensing issues. For the widest format support make sure you install all of the GStreamer plugins available for your distribution.

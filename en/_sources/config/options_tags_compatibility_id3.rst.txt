.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


ID3 Files
=========

.. index::
   single: configuration; id3 tag options

.. image:: ../images/options-tags-compatibility-id3.png
   :width: 100 %

**ID3v2 version**

   Although ID3v2.4 is the latest version, its support in music players is still lacking. While somesoftware has
   no problem using version 2.4 tags, others may not be able to read the tags and display the information. Support
   for ID3v2.4 in other media players (such as smartphones) is variable. Other than native support for
   multi-valued tags in v2.4, the `Picard Tag Mapping <https://picard.musicbrainz.org/docs/mappings/>`_ will show
   you what you lose when choosing v2.3 instead of v2.4.

**ID3v2 text encoding**

   The default for version 2.4 is UTF-8, the default for version 2.3 is UTF-16. Use ISO-8859-1 only if you face
   compatibility issues with your player.

**Join ID3v23 tags with**

   As mentioned above, ID3v2.3 does not support multi-value tags, and so Picard flattens these to strings before
   saving them to ID3v2.3 tags. This setting defines the string used to separate the values when flattened. Use
   '; ' for the greatest compatibility (rather than '/' since tags more often contain a '/' than a ';') and for
   the best visual compatibility in Picard between ID3v2.3 and other tagging formats.

**Save iTunes compatible grouping and work**

   Save the tags grouping and work so that they are compatible with current iTunes versions. Without this option
   grouping will be displayed in iTunes as "work name" and work will not be available. See the
   `Picard Tag Mapping page <https://picard.musicbrainz.org/docs/mappings/>`_ for details.

   .. note::

      For other players supporting grouping and work you might need to disable this option.
      `MusicBee <https://getmusicbee.com/>`_ is one example of this.

**Also include ID3v1 tags in the files**

   This is not recommended at all. ID3v1.1 tags are obsolete and may not work with non-latin scripts.

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Tag Compatibility
=================

.. image:: ../images/options-tags-compatibility.png
   :width: 100 %

**ID3v2 version**

   Although ID3v2.4 is the latest version, its support in music players is still lacking. While software such as
   `foobar2000 <https://www.foobar2000.org/>`_ and `MediaMonkey <https://www.mediamonkey.com/>`_ have no problem
   using version 2.4 tags, you will not be able to read the tags in Windows Explorer or Windows Media Player (in
   any Windows or WMP version). Apple iTunes is also still based in ID3v2.3, and support for ID3v2.4 in other
   media players (such as smartphones) is variable. Other than native support for multi-valued tags in v2.4, the
   `Picard Tag Mapping <https://picard.musicbrainz.org/docs/mappings/>`_ will show you what you lose when
   choosing v2.3 instead of v2.4.

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

**AAC / AC3 files**

   Picard can save APEv2 tags to pure AAC or AC3 files, which by default do not support tagging. APEv2 tags in AAC
   or AC3 are supported by some players (e.g.: foobar2000 or MusicBee), but players not supporting AAC or AC3 files
   with APEv2 tags can have issues loading and playing those files. Most often they display a wrong duration, causing
   issues on track change. To deal with this you can choose whether to save tags to those files:

   * **Save APEv2 tags**: Picard will save APEv2 tags to the files.

   * **Do not save tags**: Picard will not save any tags to the files, but you can still use Picard to rename them.
     By default existing APEv2 tags will be kept in the file.

   * **Remove APEv2 tags**: If you have "Do not save tags" enabled checking this option will cause Picard to remove
     existing APEv2 tags from the file on saving.

   Regardless of how you have configured saving tags Picard will always read existing APEv2 tags in AAC or AC3 files.

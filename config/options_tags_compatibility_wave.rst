.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


WAVE Files
==========

.. index::
   single: configuration; wave tag options

.. image:: images/options-tags-compatibility-wave.png
   :width: 100 %

WAVE by itself as a standard only supports the INFO chunk tags, which are very limited.  In addition, INFO chunks
don't have any proper support for encoding.

In all cases Picard will write ID3 tags to the WAVE files. This is supported by quite a few tools; however, it is
not supported universally.  Tools not supporting ID3 tags should just ignore them.  If possible, this is likely
the best option to have proper tags in WAVE files. For compatibility with software that does not support ID3v2 tags,
Picard can also save `Resource Interchange File Format <https://wikipedia.org/wiki/Resource_Interchange_File_Format>`_
(RIFF) INFO tags to WAVE files.  RIFF INFO is read and written only as an extra. If there are no existing ID3 tags,
the data from RIFF INFO will be used.  When saving files, RIFF INFO will be written in addition to the ID3v2 tags.

Picard's use of the RIFF INFO tags is determined by the following configuration settings:

**Also include RIFF INFO tags in the files**

   Picard will save the RIFF INFO tags to the files.

**Remove existing RIFF INFO tags from WAVE files**

   Picard will remove any existing RIFF INFO tags from the WAVE files.
   This setting is ignored if the previous setting is enabled to allow writing the RIFF INFO tags to the files.

**RIFF INFO Text Encoding**

   This setting allows you to specify the encoding used for the RIFF INFO tags written.  The default setting is
   Windows-1252 encoding.  Picard can also use UTF-8 as an alternative, which allows for full language support,
   but it depends on the software reading it.  Typically, if the software supports this, it will read the ID3 tags
   anyway so there is not much to be gained.

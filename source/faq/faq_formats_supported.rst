.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


What formats does Picard support?
==========================================

.. index::
   single: file formats

Picard supports the following file formats:

* MPEG-1 Audio (.mp3, .mp2, .m2a)
* MPEG-4 Audio (.m4a, .m4b, .m4p, .m4v, .mp4)
* Windows Media Audio (.wma, .wmv, .asf)
* Microsoft WAVE (.wav)
* The True Audio (.tta)
* FLAC (.flac)
* Audio Interchange File Format (.aiff, .aif, .aifc)
* Musepack (.mpc, .mp+)
* WavPack (.wv)
* OptimFROG (.ofr, .ofs)
* Monkey's Audio (.ape)
* Tom's lossless Audio Kompressor (.tak)
* Speex (.spx)
* Generic Ogg files (.ogg)
* Ogg FLAC (.ogg, .ogv)
* Ogg Theora (.ogg, .oga)
* Ogg Opus (.opus)
* Ogg Audio (.oga)
* Ogg Video (.ogv)
* ADTS stream / AAC (.aac)
* AC-3 (.ac3, .eac3)
* Direct Stream Digital (.dff, .dsf)

.. note::

   WAVE files lack a standard for proper tagging. Picard uses ID3v2 tags to tag WAVE files, but this is
   not supported by all software. For compatibility with software which does not support ID3v2 tags in
   WAVE files additional RIFF INFO tags can be written to the files. RIFF INFO has only limited support
   for tags and character encodings.

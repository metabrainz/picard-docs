.. MusicBrainz Picard Documentation Project

:index:`File Formats <file formats>`
=====================================

What formats does Picard support?
--------------------------------------

Picard supports the following file formats:

* MPEG-1 Audio (.mp3, .mp2, .m2a)
* MPEG-4 Audio (.m4a, .m4b, .m4p, .m4v, .m4r, .mp4)
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
* Ogg FLAC (.ogg, .oga)
* Ogg Theora (.ogg, .ogv)
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


What formats will Picard support?
-------------------------------------

Picard is intended to eventually support all formats (including fingerprinting), but this is a complex (arguably never-ending) process,
and will take some time.

.. _faq_supported_rippers:

What rippers are supported for looking up from logs?
----------------------------------------------------

As of version 2.9, Picard supports the use of log files produced by popular CD file rippers for looking up a release. Because the log
files of these rippers contain sufficient information to generate the CD table of contents they can be used in place of reading
the CD itself.  The supported rippers include:

- `dBpoweramp <https://dbpoweramp.com/>`_ for macOS and Windows
- `Exact Audio Copy (EAC) <http://exactaudiocopy.de/>`_ for Windows
- `fre:ac <https://www.freac.org>`_ for Linux, macOS, Windows and others
- `Whipper <https://github.com/whipper-team/whipper>`_ for Linux
- `X Lossless Decoder (XLD) <https://tmkk.undo.jp/xld/index_e.html>`_ for macOS


Which tags can Picard write to my files?
-------------------------------------------

See the :doc:`/variables/variables` section for information on which MusicBrainz fields Picard writes to tags. `Picard Tag Mapping
<https://picard.musicbrainz.org/docs/mappings/>`_ contains more technical information on how these are further mapped into each tag format.


How do I edit tags in several files at once?
--------------------------------------------

1. Click and select several files with :kbd:`Ctrl` or :kbd:`Shift`.
2. The metadata view at the bottom will show which tags are present in the selected files
   and whether they are the same across all files or different.
3. If you edit any value in the "New values" column you will change this tag for all selected files.
4. You need to click Save in order to persist these changes to your files.

Please understand that Picard is not designed as a general purpose :index:`tag editor <tags; editing>`. Its primary goal is to retrieve community-maintained MusicBrainz
data to write into your tags. Some secondary goals include:

* allowing rule-based customization of that data using scripts and plugins
* encouraging users to create an account and fix and update data via the MusicBrainz website, thus sharing their work with the rest of the community rather than simply fixing their tags locally.

To that end, Picard is likely to never have as much development focus on manual bulk editing of tags as other general purpose editors (e.g.:
`Mp3tag <https://www.mp3tag.de/en/>`_, `foobar2000 <https://www.foobar2000.org/>`_, or even many library managers such as iTunes, Windows
Media Player, and MediaMonkey). That doesn't mean that the team won't welcome patches in this area!


Why is saving files sometimes slow, but saving a second time much faster?
-------------------------------------------------------------------------

In most file formats the tags are near the beginning of the file, before the actual music data.  If changed
tags get written to the file and the newly written tags take more space than before the entire file needs
to be rewritten. This is usually much slower than just rewriting part of the file containing the tags,
especially for larger files and/or if the files are on a slow storage (e.g. a network share or slow external drive).

To mitigate the issue most tagging software (including Picard) leaves some free space (the so called padding)
after the tags and before the actual music data. If the newly written are only a bit larger than before this free space
can be used instead of rewriting the entire files. Likewise if the newly written tags take less space than before this
only leads to an increase in padding, avoiding rewriting the file.

This all means that when you add many tags to the files (or if there is no or only small padding) you experience
slow writing speed. If you do only small changes or just remove and later re-add tags the writing is much faster.


Why does Picard not use Vinyl style track numbers (e.g. A1, A2, ...) by default?
--------------------------------------------------------------------------------

For Vinyl releases the track numbers on MusicBrainz are usually entered as A1, A2, ..., B1, B2, ... and so on.
Other releases might use even different more uncommon numbering schemes.  Yet Picard will by default always write
decimal track numbers, starting with 1 for the first track on a medium.

The main reason for this is that this is how track numbers are defined for most file formats.  The formats expect
decimal numbers, and likewise music players might only expect decimal numbers when reading the files.

If you really want to you can use the scripting variable ``%_musicbrainz_tracknumber%`` which always holds the
track number as it was entered in the MusicBrainz database.  The following script will set the tracknumber tag
to the value as displayed in the MusicBrainz database:

.. code-block:: taggerscript

   $set(tracknumber,%_musicbrainz_tracknumber%)

Please be aware that for MP4 files this will result in the track number not being saved, as the MP4 format
does not allow for non integer values in this tag.  For other formats it depends on the playback software and
devices you use if they can handle these non-standard track numbers.


The built-in audio player cannot play my file. Which formats does it support?
-----------------------------------------------------------------------------------

The formats supported by the built-in :index:`audio player` depend on the formats supported by your operating system.

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


I am using Fedora. Why doesn't :index:`acoustic fingerprinting <acoustic fingerprint, fingerprint; acoustic>` work?
------------------------------------------------------------------------------------------------------------------------

Acoustic fingerprinting in Picard uses a tool called :program:`fpcalc`, which is not available in Fedora. You can get it by installing the chromaprint-toolspackage
from the `RPM Fusion repository <https://rpmfusion.org/>`_. This functionality is not contained in the main Fedora ``picard`` package because it requires
the ``ffmpeg`` package which `cannot be distributed by Fedora <https://fedoraproject.org/wiki/Forbidden_items>`_. After `enabling the "rpmfusion-free" RPM
Fusion repository <https://rpmfusion.org/Configuration>`_, install the package (as root) using::

   yum install chromaprint-tools

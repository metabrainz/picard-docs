.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


File Formats
============

.. index::
   single: file formats

**What formats does Picard support?**

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

**What formats will Picard support?**

   Picard is intended to eventually support all formats (including fingerprinting), but this is a complex (arguably never-ending) process,
   and will take some time.

**Which tags can Picard write to my files?**

   See the :doc:`../variables/variables` section for information on which MusicBrainz fields that Picard writes to tags. `Picard Tag Mapping
   <https://picard.musicbrainz.org/docs/mappings/>`_ contains more technical information on how these are further mapped into each tag format.

.. index::
   single: tags; editing

**How to I edit several tags at once? Why is it not easier do so?**

   Please understand that Picard is not designed as a general purpose tag editor. Its primary goal is to retrieve community-maintained MusicBrainz
   data to write into your tags. Some secondary goals include:

   * allowing rule-based customization of that data using scripts and plugins
   * encouraging users to create an account and fix and update data via the MusicBrainz website, thus sharing their work with the rest of the
     community rather than simply fixing their tags locally.

   To that end, Picard is likely to never have as much development focus on manual bulk editing of tags as other general purpose editors (e.g.:
   `Mp3tag <https://www.mp3tag.de/en/>`_, `foobar2000 <https://www.foobar2000.org/>`_, or even many library managers such as iTunes, Windows
   Media Player, and MediaMonkey). That doesn't mean that the team won't welcome patches in this area!

   Having said all this, it is still possible to edit several tags at once in Picard by following the steps:

   1. Click and select several files with CTRL or SHIFT
   2. Right click on one of them, then click Details...
   3. On the popup dialog you can see the tags, with entries that denote where tags are different across files. You can edit or add new tags here.
   4. On exiting the dialog, you have changed the tags in memory. You need to click Save in order to persist these changes to your files.

   This process should work in both panes.

.. index::
   single: audio player

**The built-in audio player cannot play my file. Which formats does it support?**

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

.. index::
   single: acoustic fingerprint
   single: fingerprint; acoustic

**I am using Fedora. Why doesn't acoustic fingerprinting work?**

   Acoustic fingerprinting in Picard uses a tool called ``fpcalc``, which is not available in Fedora. You can get it by installing the chromaprint-toolspackage
   from the `RPM Fusion repository <https://rpmfusion.org/>`_. This functionality is not contained in the main Fedora ``picard`` package because it requires
   the ``ffmpeg`` package which `cannot be distributed by Fedora <https://fedoraproject.org/wiki/Forbidden_items>`_. After `enabling the "rpmfusion-free" RPM
   Fusion repository <https://rpmfusion.org/Configuration>`_, install the package using (as root)::

      yum install chromaprint-tools

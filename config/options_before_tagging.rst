.. MusicBrainz Picard Documentation Project

:index:`Before Tagging <configuration; before tagging>`
========================================================

.. only:: html

   .. image:: images/options-tags.png
      :width: 100 %

**Clear existing tags**

   Checking this will remove all existing metadata and leave your files with only MusicBrainz metadata. Information you
   may have added through another media player such as "genre", "comments" or "ratings" will be removed.

**Keep embedded images when clearing tags**

   The default is for Picard to remove any embedded images from the files when clearing existing tags. Checking this
   option will keep the embedded images in the files.

**Remove ID3 tags from FLAC files**

   Check to remove ID3 tags from FLAC files – Vorbis Comments are recommended for FLAC files. Picard will write Vorbis
   Comments to FLAC files regardless of this setting.

**Remove APEv2 tags from MP3 files**

   Check to remove APEv2 tags from MP3 files – ID3 is recommended for MP3 files. Picard will write ID3 tags to MP3 files
   regardless of this setting.

**Preserve these tags from being cleared or overwritten with MusicBrainz data**

   This is an advanced option: If you have tags which you need to preserve, enter their names here to stop Picard from
   overwriting them.

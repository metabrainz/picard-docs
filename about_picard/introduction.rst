.. MusicBrainz Picard Documentation Project

Introduction
============

MusicBrainz Picard is a cross-platform music file tagger.
For any people who don't know what this means, here is a quick explanation which can be
skipped by those people who already know.

Your music files don't just contain music. They also contain "metadata", consisting of "tags"
which consist of a tag name or type and associated data, for example the album or track name,
the name of the artist, the record label, the year of issue etc.
Unless you rip the music files yourself with a very basic tool, your music files probably already
contain some basic metadata, however there are literally hundreds of tags that can be applied to
your music if you are interested.

Obviously, if you wanted to you could painstakingly research all this information for each
album and track individually, and type the data into a tagging tool, but clearly it makes more
sense in this internet connected age for one person to do this for each album and track,
to upload that data to a shared database and then for the tagging tool to access that database
and use the data to tag the music files. And **that** is what MusicBrainz Picard does.

**MusicBrainz** is the database, and **Picard** is the tool that tags the music files.

This User Guide is intended to provide comprehensive information related to the use of `MusicBrainz
Picard <https://picard.musicbrainz.org/>`_ and additionally to make this available in
alternate formats, including a PDF version suitable for printing. Links to additional
information such as scripts, plugins and tutorials are provided when available rather than trying
to reproduce the information in this document.

.. only:: html

   .. note::

      There is also an :doc:`Introduction to Picard Video Tutorial </tutorials/v_introduction>` available.

In order to effectively use Picard, it is important to understand what the program can do and,
equally important, what it cannot do.  Picard is primarily intended to tag and organize albums containing tracks,
guided by the user to the specific release of the album that they have, and then to keep the metadata for these
tracks up to date as users around the world enhance the quality of the MusicBrainz data associated with that
particular release and track; Picard does this very well indeed. However, it is not intended to automatically
organize your collection of thousands of random music files, and if this is what you are hoping for then you will likely
be disappointed.  To quote from the Picard website, *"Picard is not built to be a mass single-track
tag fixer. Picard believes in quality over quantity and provides a plethora of customizations to
tweak music collections to your needs."*

Picard Can...
-------------

...add metadata tags to your music files, based on information available from the `MusicBrainz
website <https://musicbrainz.org/>`_.

...look up the metadata either manually or automatically based on existing information, including
artist and song name, disc id (for CDs), and a track's AcoustID fingerprint.

...retrieve and embed coverart images from a variety of sources.

...rename and place the music files in directories based on naming template instructions provided
in a naming script.

...calculate and submit a disc id to the MusicBrainz database, attaching it to a specified release.

...calculate and submit a music file's AcoustID fingerprint to the `AcoustID database <https://acoustid.org/>`_.


Picard Cannot...
----------------

...automatically identify and remove all duplicate music files in your collection.

...provide metadata not already existing in the MusicBrainz database.


:index:`Limitations <limitations>`
-----------------------------------

**File Formats**

Picard currently supports most music file formats, with Matroska (.mka) being one notable exception.
Microsoft WAVE (.wav) files can be fingerprinted and renamed and can be tagged using ID3v2 tags, but this is
not supported by all playback software.  In addition, Picard does not support writing custom tags for all formats.

The :doc:`Picard Tag Mappings </appendices/tag_mapping>` section provides more information
regarding the mapping between Picard internal tag names and various tagging formats.

**Request Rate Limiting**

Picard's metadata retrieval is limited to the standard **one request per second** :index:`rate limiting` for the MusicBrainz
API.  This becomes quite noticeable when trying to process a large list of files, and is exacerbated by
extensions that perform additional information requests from the database.

**Network File Processing**

Sometimes Picard needs to rewrite the entire music file in order to add or update the tags.  This can take a
few seconds, and the delay becomes even longer if the file is accessed across a network (e.g.: file is
read from or written to a NAS device).  The recommended "best practice" is to process all files on a local drive
and then move them to the desired remote directory once processing is complete.

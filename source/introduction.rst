.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


Introduction
============

MusicBrainz Picard is a cross-platform music file tagger.  This User Guide is intended to
augment the information provided on the `Picard website <https://picard.musicbrainz.org/>`_
and to provide an alternate format for the documentation, including a PDF document suitable
for printing.  Links to additional information such as scripts, plugins and tutorials are
provided when available rather than trying to reproduce the information in this document.

In order to effectively use Picard, it is important to understand what the program can do and,
equally important, what it cannot do.  What Picard does, it does very well, but if you're expecting
it to automatically organize your collection of thousands of random music files you will likely
be disappointed.  To quote from the Picard website, *"Picard is not built to be a mass single-track
tag fixer. Picard believes in quality over quantity and provides a plethora of customizations to
tweak music collections to your needs."*

.. only:: latex

   .. toctree::

      acknowledgements


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


.. index::
   single: limitations
   single: rate limiting

Limitations
-----------

**File Formats**

Picard currently supports most music file formats, with Matroska (.mka) being one notable exception.
Microsoft WAVE (.wav) files can be fingerprinted and renamed and can be tagged using ID3v2 tags, but this is
not supported by all playback software.  In addition, Picard does not support writing custom tags for all formats.
The `Picard Tag Mappings <https://picard.musicbrainz.org/docs/mappings/>`_ webpage provides more information
regarding the mapping between Picard internal tag names and various tagging formats.

**Request Rate Limiting**

Picard's metadata retrieval is limited to the standard **one request per second** rate limiting for the MusicBrainz
API.  This becomes quite noticable when trying to process a large list of files, and is exacerbated by
extensions that perform additional information requests from the database.

**Network File Processing**

Sometimes Picard needs to rewrite the entire music file in order to add or update the tags.  This can take a
few seconds, and the delay becomes even longer if the file is accessed across a network (e.g.: file is
read from or written to a NAS device).  The recommended "best practice" is to process all files on a local drive
and then move them to the desired remote directory once processing is complete.

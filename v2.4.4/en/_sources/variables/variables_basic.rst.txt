.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Basic Variables
===============

.. index::
   single: variables; basic

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

.. note::

   Variables that rely on information from the files (e.g.: _bitrate) are only available for use in the file naming script.

**_absolutetracknumber**

    The absolute number of this track disregarding the disc number (i.e.: ``%_absolutetracknumber%`` of ``%_totalalbumtracks%``).
    For example, this value would be 11 for the second track on disc 2 where disc 1 has 9 tracks. (*since Picard 1.3*)

**_albumartists**

    The Album's Artists' Name(s) (multi-value). (*since Picard 1.3*)

**_albumartists_sort**

    The Album Artist's Sort Name(s) (multi-value). (*since Picard 1.3*)

**_artists_sort**

    The Artist's Sort Name(s) (multi-value). (*since Picard 1.3*)

**_bitrate**

    Approximate bitrate in kbps.  Only available to the file naming script.

**_bits_per_sample**

    Bits of data per sample.  Only available to the file naming script.

**_channels**

    Number of audio channels in the file.  Only available to the file naming script.

**_dirname**

    The name of the directory containing the file at the point of being loaded into Picard.  Only available to the file naming script. (*since Picard 1.1*)

**_extension**

    The file's extension.  Only available to the file naming script. (*since Picard 0.9*)

**_filename**

    The name of the file without extension.  Only available to the file naming script. (*since Picard 1.1*)

**_format**

    Media format of the file (e.g.: MPEG-1 Audio).  Only available to the file naming script.

**_length**

    The length of the track in format mins:secs.

**_multiartist**

    0 if tracks on the album all have the same primary artist, 1 otherwise. (*since Picard 1.3*)

.. _ref_primaryreleasetype:

**_primaryreleasetype**

    Release Group Primary type (i.e.: album, single, ep, broadcast, or other).

**_rating**

    Rating 0-5 by Musicbrainz users.

**_releasecomment**

    Release disambiguation comment. (*since Picard 0.15*)

**_releasegroup**

    Release Group Title which is typically the same as the Album Title, but can be different.

**_releasegroupcomment**

    Release Group disambiguation comment.

**_releaselanguage**

    Release Language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_. (*since Picard 0.10*)

**_sample_rate**

    Number of digitizing samples per second (Hz).  Only available to the file naming script.

.. _ref_secondaryreleasetype:

**_secondaryreleasetype**

    Zero or more Release Group Secondary types (i.e.: audiobook, compilation, dj-mix, interview, live, mixtape/street, remix, soundtrack, or spokenword).

**_totalalbumtracks**

    The total number of tracks across all discs of this release.

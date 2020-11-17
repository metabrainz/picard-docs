.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

:index:`Basic Variables <variables; basic>`
============================================

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

**_absolutetracknumber**

    The absolute number of this track disregarding the disc number (i.e.: ``%_absolutetracknumber%`` of ``%_totalalbumtracks%``).
    For example, this value would be 11 for the second track on disc 2 where disc 1 has 9 tracks (*since Picard 1.3*).

**_albumartists**

    The Album's Artists' Name(s) (multi-value) (*since Picard 1.3*).

**_albumartists_sort**

    The Album Artist's Sort Name(s) (multi-value) (*since Picard 1.3*).

**_artists_sort**

    The Artist's Sort Name(s) (multi-value) (*since Picard 1.3*).

**_datatrack**

    Set to 1 if the track is a "`data track <https://wiki.musicbrainz.org/Style/Unknown_and_untitled/Special_purpose_track_title#Data_tracks>`_" (*since Picard 1.3.1*).

**_discpregap**

    Set to 1 if the disc the track is on has a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_" (*since Picard 1.4*).

**_multiartist**

    0 if tracks on the album all have the same primary artist, 1 otherwise (*since Picard 1.3*).

**_pregap**

    Set to 1 if the track is a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_" (*since Picard 1.3.1*).

.. _ref_primaryreleasetype:

**_primaryreleasetype**

    Release Group Primary type (i.e.: album, single, ep, broadcast, or other).

**_rating**

    Rating 0-5 by MusicBrainz users.

**_releasecomment**

    Release disambiguation comment (*since Picard 0.15*).

**_releasegroup**

    Release Group Title which is typically the same as the Album Title, but can be different.

**_releasegroupcomment**

    Release Group disambiguation comment.

**_releaselanguage**

    Release Language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_ (*since Picard 0.10*).

.. _ref_secondaryreleasetype:

**_secondaryreleasetype**

    Zero or more Release Group Secondary types (i.e.: audiobook, compilation, dj-mix, interview, live, mixtape/street, remix, soundtrack, or spokenword).

**_totalalbumtracks**

    The total number of tracks across all discs of this release.

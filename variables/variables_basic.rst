.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

:index:`Basic Variables <variables; basic>`
============================================

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

**_absolutetracknumber**

    The absolute number of this track disregarding the disc number (i.e.: ``%_absolutetracknumber%`` of ``%_totalalbumtracks%``).
    For example, this value would be 11 for the second track on disc 2 where disc 1 has 9 tracks. (*since Picard 1.3*)

**_albumartists**

    The Album's Artists' Name(s) (multi-value). (*since Picard 1.3*)

**_albumartists_sort**

    The Album Artist's Sort Name(s) (multi-value). (*since Picard 1.3*)

**_artists_sort**

    The Artist's Sort Name(s) (multi-value). (*since Picard 1.3*)

**_datatrack**

   Set to 1 if the track is a "`data track <https://wiki.musicbrainz.org/Style/Unknown_and_untitled/Special_purpose_track_title#Data_tracks>`_". (*since Picard 1.3.1*)

**_discpregap**

   Set to 1 if the disc the track is on has a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_". (*since Picard 1.4*)

**_multiartist**

    Set to 1 if not all of the tracks on the album have the same primary artist, otherwise empty. (*since Picard 1.3*)

**_musicbrainz_discids**

    This multi-value variable contains a list of all of the disc ids attached to the selected release.  The list provided for each medium only includes
    the disc ids attached to that medium. For example, the list provided for Disc 1 of a three CD set will not include the disc ids attached to discs 2
    and 3 of the set.

**_musicbrainz_tracknumber**

    The track number written as on the MusicBrainz release, such as vinyl numbering (A1, A2...).

**_pregap**

   Set to 1 if the track is a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_". (*since Picard 1.3.1*)

.. _ref_primaryreleasetype:

**_primaryreleasetype**

    Release Group Primary type (i.e.: album, single, ep, broadcast, or other).

**_rating**

    Rating 0-5 by MusicBrainz users.

**_recording_comment**

   The disambiguation comment for the recording associated with a track.

**_recording_firstreleasedate**

   The date of the earliest recording for a track in the format YYYY-MM-DD.  (*Since Picard 2.6*)

**_releaseannotation**

   The annotation comment for the release. (*since Picard 2.6*)

**_releasecomment**

    Release disambiguation comment. (*since Picard 0.15*)

**_releasecountries**

    This provides the complete list of release countries for the release as a multi-value variable. (*since Picard 2.3.1*)

**_releasegroup**

    Release Group Title which is typically the same as the Album Title, but can be different.

**_releasegroupcomment**

    Release Group disambiguation comment.

**_releasegroup_firstreleasedate**

   The date of the earliest release in the Release Group in the format YYYY-MM-DD. This is intended to provide, for example, the release date of the vinyl version of what you have on CD. (*Since Picard 2.6*)

   .. note::

      This is the same information provided by default in the ``originaldate`` tag.

**_releaselanguage**

    Release Language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_. (*since Picard 0.10*)

.. _ref_secondaryreleasetype:

**_secondaryreleasetype**

    Zero or more Release Group Secondary types (i.e.: audiobook, compilation, dj-mix, interview, live, mixtape/street, remix, soundtrack, or spokenword).

**_totalalbumtracks**

    The total number of tracks across all discs of this release.

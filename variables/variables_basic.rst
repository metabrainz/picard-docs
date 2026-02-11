.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

:index:`Basic Variables <variables; basic>`
===========================================

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

Some variables provide the :index:`MusicBrainz Identifier (MBID) <identifier; musicbrainz, mbid>` of the entity. The MBID is a 32-character identifier assigned to an entity (e.g.: artist, album, track or work) to uniquely identify the entity. For more information about MBIDs, please see the `MusicBrainz Identifier <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_ page in the MusicBrainz documentation.

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

**_absolutetracknumber**

   The absolute number of this track disregarding the disc number (i.e.: ``%_absolutetracknumber%`` of ``%_totalalbumtracks%``). For example, this value would be 11 for the second track on disc 2 where disc 1 has 9 tracks. (*since Picard 1.3*)

**_albumartists**

   A multi-value variable containing the names of the album's artists. These could be either "standardized" or "as credited" depending on whether the "Use standardized artist names" metadata option is enabled. (*since Picard 1.3*)

**_albumartists_countries**

   A multi-value variable containing the country codes for all of the credited album artists, in the same order as the artists. Duplicate country codes will be shown if there are more than one artist from the same country. If a country code is not provided by the webservice the code "XX" will be used to indicate an unknown country. For example, if the first credited artist is from Great Britain and there are two other credited artists from Canada, the value would be "GB; CA; CA".

**_albumartists_sort**

   A multi-value variable containing the sort names of the album's artists. (*since Picard 1.3*)

**_artists_countries**

   A multi-value variable containing the country codes for all of the credited track artists, in the same order as the artists. Duplicate country codes will be shown if there are more than one artist from the same country. If a country code is not provided by the webservice the code "XX" will be used to indicate an unknown country. For example, if the first credited artist is from Great Britain and there are two other credited artists from Canada, the value would be "GB; CA; CA".

**_artists_sort**

   A multi-value variable containing the sort names of the track's artists. (*since Picard 1.3*)

**_datatrack**

   Set to 1 if the track is a "`data track <https://wiki.musicbrainz.org/Style/Unknown_and_untitled/Special_purpose_track_title#Data_tracks>`_", otherwise empty. (*since Picard 1.3.1*)

**_discpregap**

   Set to 1 if the disc the track is on has a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_", otherwise empty. (*since Picard 1.4*)

**_multiartist**

   Set to 1 if not all of the tracks on the album have the same primary artist, otherwise empty. (*since Picard 1.3*)

**_musicbrainz_discids**

   A multi-value variable containing a list of all of the disc ids attached to the selected release. The list provided for each medium only includes the disc ids attached to that medium. For example, the list provided for Disc 1 of a three CD set will not include the disc ids attached to discs 2 and 3 of the set.

**_musicbrainz_tracknumber**

   The track number written as on the MusicBrainz release, such as vinyl numbering (A1, A2…).

**_pregap**

   Set to 1 if the track is a "`pregap track <https://musicbrainz.org/doc/Terminology#hidden_track>`_", otherwise empty. (*since Picard 1.3.1*)

.. _ref_primaryreleasetype:

**_primaryreleasetype**

   The primary type of the release group (i.e.: *album*, *single*, *ep*, *broadcast*, or *other*).

**_rating**

   The rating of the track from 0-5 by MusicBrainz users.

**_recordingcomment**

   The disambiguation comment for the recording associated with a track. (*since Picard 0.15*)

**_recording_firstreleasedate**

   The date of the earliest recording for a track in the format YYYY-MM-DD. (*Since Picard 2.6*)

**_releaseannotation**

   The annotation comment for the release. (*since Picard 2.6*)

**_releasecomment**

   The disambiguation comment for the release. (*since Picard 0.15*)

**_releasecountries**

   A multi-value variable containing the complete list of release countries for the release. (*since Picard 2.3.1*)

**_releasegroup**

   The title of the release group. This is typically the same as the album title, but can be different.

**_releasegroup_firstreleasedate**

   The date of the earliest release in the release group in the format YYYY-MM-DD. This is intended to provide, for example, the release date of the vinyl version of what you have on CD. (*Since Picard 2.6*)

   .. note::

      This is the same information provided by default in the ``originaldate`` tag.

**_releasegroupcomment**

   The disambiguation comment for the release group.

**_releaselanguage**

   The language of the release as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_. (*since Picard 0.10*)

.. _ref_secondaryreleasetype:

**_secondaryreleasetype**

   Zero or more secondary types (i.e.: *audiobook*, *compilation*, *dj-mix*, *interview*, *live*, *mixtape/street*, *remix*, *soundtrack*, or *spokenword*) for the release group.

**_totalalbumtracks**

   The total number of tracks across all discs of this release.

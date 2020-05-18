..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Basic Tags
==========
The following tags are populated from MusicBrainz data for most releases, without any special Picard settings.

All of these are also available as variables for use in Picard Scripts (for tagging, for file renaming and in
several other more minor settings) by wrapping them between percent '%' symbols (e.g. ``%title%``).

**acoustid_fingerprint**

    AcoustID Fingerprint for the track.

**acoustid_id**

    AcoustID associated with the track.

**album**

    Title of the release.

**albumartist**

    Artist(s) primarily credited on the release.

**albumartistsort**

    Release Artist's Sort Name

**albumsort**

    Release Title's Sort Name

**artist**

    Track Artist Name(s) (string)

**artists**

    Track Artist Name(s) (multi-value) (*since Picard 1.3*)

**artistsort**

    Track Artist Sort Name

**asin**

    Amazon Standard Identification Number

**barcode**

    Release Barcode

**bpm**

    Beats per minute of the track.

**catalognumber**

    The number(s) assigned to the release by the label(s) which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved.

**comment**

    Disambiguation Comment

**compilation**

    | (*since Picard 1.3, compatible with iTunes*) 1 for Various Artist albums, otherwise 0.
    | (*Picard 1.2 or previous*) 1 if multiple track artists (including featured artists), otherwise 0.

**copyright**

    Contain copyright message for the copyright holder of the original sound, begin with a year and a space character.

**date**

    Release Date (YYYY-MM-DD)

**discid**

    Disc ID is the code number which MusicBrainz uses to link a physical CD to a release listing.

**discnumber**

    Number of the disc in this release that contains this track.

**discsubtitle**

    The Media Title given to a specific disc.

**encodedby**

    Encoded by (person or organization)

**encodersettings**

    Encoder Settings

**isrc**

    International Standard Recording Code (*since Picard 0.12*)

**key**

    Key of the music

**label**

    Release Label Name(s)

**language**

    Work lyric language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_ if track relationships are enabled in Options and a related work exists. (*since Picard 0.10*)

**lyrics**

    Lyrics for the track.

**media**

    Release Format (e.g.: CD).  See the `Release Format <https://musicbrainz.org/doc/Release/Format>`_ page on the MusicBrainz website for more information.

**musicbrainz_albumartistid**

    Release Artist's MusicBrainz Identifier

**musicbrainz_albumid**

    Release MusicBrainz Identifier

**musicbrainz_artistid**

    Track Artist's MusicBrainz Identifier

**musicbrainz_discid**

    Disc ID if the album was added using CD Lookup (*since Picard 0.12*)

**musicbrainz_originalalbumid**

    Original Release's MusicBrainz Identifier

**musicbrainz_originalartistid**

    Original Track Artist's MusicBrainz Identifier

**musicbrainz_recordingid**

    Recording's MusicBrainz Identifier

**musicbrainz_releasegroupid**

    Release Group's MusicBrainz Identifier

**musicbrainz_releasetrackid**

    Release Track MusicBrainz Identifier (*since Picard 1.3*)

**musicbrainz_trackid**

    Recording MusicBrainz Identifier

**musicbrainz_workid**

    Work Name MusicBrainz Identifier

**musicip_fingerprint**

    MusicIP's Fingerprint

**musicip_puid**

    MusicIP PUID’s associated with the track.

**originalalbum**

    Release Title of the earliest release in the Release Group intended for the title of the original recording.

**originalartist**

    Track Artist of the earliest release in the Release Group intended for the performer(s) of the original recording.

**originaldate**

    Release Date (YYYY-MM-DD) of the earliest release in the Release Group intended to provide, for example, the release date of the vinyl version of what you have on CD. (*Included as standard from Picard 0.15, and using the Original Release Date plugin if you are still using a non-NGS version earlier than Picard 0.15*)

    .. note::

        If you are storing tags in MP3 files as ID3v2.3 (which is the Windows and iTunes compatible version) then the original date can only be stored as a year.

**originalyear**

    Year of the original Release Date intended for release year of the original recording.

**releasecountry**

    Country in which the release was issued.

**releasestatus**

    Release Status indicating the "official" status of the release.  Possible values include official, promotional, bootleg, and pseudo-release.

**releasetype**

    Release Group Type (see also :ref:`_primaryreleasetype <ref_primaryreleasetype>` and :ref:`_secondaryreleasetype <ref_secondaryreleasetype>`)

**script**

    The script used to write the release's track list. The possible values are taken from the `ISO 15924 <https://en.wikipedia.org/wiki/ISO_15924>`_ standard. (*since Picard 0.10*)

**subtitle**

    Used for information directly related to the contents title

**title**

    Track Title

**titlesort**

    Track Title's Sort Name

**totaldiscs**

    Total number of discs in this release

**totaltracks**

    Total tracks on this disc

**tracknumber**

    Track number on the disc

**website**

    Used for official artist website.


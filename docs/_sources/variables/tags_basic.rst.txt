..  Picard Scripting Variables

Basic Tags
==========
The following tags are populated from MusicBrainz data for most releases, without any special Picard settings.

All of these are also available as variables for use in Picard Scripts (for tagging, for file renaming and in
several other more minor settings) by wrapping them between '%' symbols (e.g. ``%title%``).

**acoustid_fingerprint**

    AcoustID's Fingerprint

**acoustid_id**

    AcoustID associated with the track.

**album**

    Release Title

**albumartist**

    Release Artist

**albumartistsort**

    Release Artist's Sort Name

**albumsort**

    Release Title's Sort Name

**artist**

    Track Artist Name(s) (string)

**artists**

    Track Artist Name(s) (multi-value) (since Picard 1.3)

**artistsort**

    Track Artist Sort Name

**asin**

    Amazon Standard Identification Number

**barcode**

    Release Barcode

**bpm**

    Beats per minute

**catalognumber**

    Release Catalog Number(s)

**comment**

    Disambiguation Comment

**compilation**

    | (since Picard 1.3, compatible with iTunes) 1 for Various Artist albums, otherwise 0.
    | (Picard 1.2 or previous) 1 if multiple track artists (including featured artists), otherwise 0.

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

    Encoded by (person/organisation)

**encodersettings**

    Encoder Settings

**isrc**

    International Standard Recording Code (since Picard 0.12)

**key**

    Key of the music

**label**

    Release Label Name(s)

**language**

    Work lyric language as per ISO 639-3 if track relationships are enabled in Options and a related work exists. (since Picard 0.10)

**lyrics**

    Lyrics

**media**

    Release Format (e.g. CD)

**musicbrainz_albumartistid**

    Release Artist's MusicBrainz Identifier

**musicbrainz_albumid**

    Release MusicBrainz Identifier

**musicbrainz_artistid**

    Track Artist's MusicBrainz Identifier

**musicbrainz_discid**

    Disc ID if the album was added using CD Lookup (since Picard 0.12)

**musicbrainz_originalalbumid**

    Original Release's MusicBrainz Identifier

**musicbrainz_originalartistid**

    Original Track Artist's MusicBrainz Identifier

**musicbrainz_recordingid**

    Recording's MusicBrainz Identifier

**musicbrainz_releasegroupid**

    Release Group's MusicBrainz Identifier

**musicbrainz_releasetrackid**

    Release Track MusicBrainz Identifier (since Picard 1.3)

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

    Release Date (YYYY-MM-DD) of the earliest release in the Release Group intended to provide, for example, the release date of the vinyl version of what you have on CD. (Included as standard from Picard 0.15, and using the Original Release Date plugin if you are still using a non-NGS version earlier than Picard 0.15)

    Note: If you are storing tags in mp3 files as ID3v23 (which is the Windows / iTunes compatible version) then the original date can only be stored as a year.

**originalyear**

    Year of the original Release Date intended for release year of the original recording.

**releasecountry**

    Release Country

**releasestatus**

    Release Status

**releasetype**

    Release Group Type (see also _primaryreleasetype / _secondaryreleasetype)

**script**

    Release Script (since Picard 0.10)

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


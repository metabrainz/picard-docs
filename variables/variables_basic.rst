..  Picard Scripting Variables

Basic Variables
===============

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

**_absolutetracknumber**

    The absolute number of this track disregarding the disc number i.e. ``%_absolutetracknumber%`` of ``%_totalalbumtracks%`` (c.f. ``%tracknumber%`` of ``%totaltracks%``). (Since Picard 1.3)

**_albumartists**

    The Album's Artists' Name(s) (multi-value) (Since Picard 1.3).

**_albumartists_sort**

    The Album Artist's Sort Name(s) (multi-value) (Since Picard 1.3).

**_artists_sort**

    The Artist's Sort Name(s) (multi-value) (Since Picard 1.3).

**_bitrate**

    Approximate bitrate in kbps.

**_bits_per_sample**

    Bits of data per sample

**_channels**

    No. of audio channels in the file

**_dirname**

    The name of the directory the file is in at the point of being loaded into Picard. (Since Picard 1.1)

**_extension**

    The files extension (since Picard 0.9)

**_filename**

    The name of the file without extension (since Picard 1.1)

**_format**

    Media format of the file (e.g. MPEG-1 Audio)

**_length**

    The length of the track in format mins:secs.

**_multiartist**

    0 if tracks on the album all have the same primary artist, 1 otherwise. (Since Picard 1.3)

**_primaryreleasetype**

    Release Group Primary type (i.e. Album, Single, EP, Broadcast, Other).

**_rating**

    Rating 0-5 by Musicbrainz users

**_releasecomment**

    Release disambiguation comment (since Picard 0.15)

**_releasegroup**

    Release Group Title which is typically the same as the Album Title, but can be different.

**_releasegroupcomment**

    Release Group disambiguation comment.

**_releaselanguage**

    Release Language as per ISO 639-3 (since Picard 0.10)

**_sample_rate**

    Number of digitising samples per second Hz

**_secondaryreleasetype**

    Zero or more Release Group Secondary types (i.e. Audiobook, Compilation, DJ-mix, Interview, Live, Mixtape/Street, Remix, Soundtrack, Spokenword).

**_totalalbumtracks**

    The total number of tracks across all discs of this release.

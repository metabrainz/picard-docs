.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

.. #metabrainz [May 22, 16:54:30] <rdswift> zas: The Picard docs refer to the following as basic tags, but I haven't yet
..                                found a release that will produce them.  Do you know if they are still valid, or have
..                                they been deprecated?  musicbrainz_originalalbumid, musicbrainz_originalartistid,
..                                musicbrainz_releasetrackid, originalalbum, originalartist
.. #metabrainz [May 23, 02:50:44] <zas> rdswift: dunno, perhaps outsidecontext could tell
.. #metabrainz [May 23, 02:52:20] <zas> but there were relatively recent changes regarding few of them, see PICARD-1426
.. #metabrainz [May 23, 02:52:21] <+BrainzBot> PICARD-1426: Map musicbrainz_originalalbumid and musicbrainz_originalartistid
..                                to MP4 and WMA https://tickets.metabrainz.org/browse/PICARD-1426
.. #metabrainz [May 23, 02:53:34] <zas> PICARD-720
.. #metabrainz [May 23, 02:53:35] <+BrainzBot> PICARD-720: Files are immediately recognized as "non-album tracks" if
..                                MUSICBRAINZ_ALBUMID is missing https://tickets.metabrainz.org/browse/PICARD-720
.. #metabrainz [May 23, 03:50:42] <Mineo> rdswift: musicbrainz_releasetrackid is only written for some formats (ape and vorbis)
.. #metabrainz [May 23, 03:51:53] <Mineo> rdswift: for the original... tags, see https://tickets.metabrainz.org/browse/PICARD-1034
.. #metabrainz [May 23, 03:51:54] <+BrainzBot> PICARD-1034: Picard not seeing TOPE and TOAL


:index:`Basic Tags <tags; basic>`
==================================

The following tags are populated from MusicBrainz data for most releases, without any special Picard settings.

All of these are also available as variables for use in Picard Scripts (for tagging, for file renaming and in
several other more minor settings) by wrapping them between percent '%' symbols (e.g. ``%title%``).

.. note::

   Tags will not be created and will not be available as variables if there was no value retrieved for the tag
   from the MusicBrainz database.

.. note::

   Some of these tags are only supported for certain file types or tag formats.  Please see the :doc:`Picard Tag Mapping
   <../appendices/tag_mapping>` section for details.

**acoustid_fingerprint**

    AcoustID Fingerprint for the track.

**acoustid_id**

    AcoustID associated with the track.

**album**

    Title of the release.

**albumartist**

    Artist(s) primarily credited on the release.

**albumartistsort**

    Release Artist's Sort Name (e.g.: "Beatles, The").

**albumsort**

    Release Title's Sort Name.

**artist**

    Track Artist Name(s). (string)

**artists**

    Track Artist Name(s). (multi-value) (*since Picard 1.3*)

**artistsort**

    Track Artist Sort Name.

**asin**

    Amazon Standard Identification Number - the number identifying the item on Amazon.

**barcode**

    Release Barcode - the barcode assigned to the release.

**bpm**

    Beats per minute of the track.  Only available to the file naming script.

**catalognumber**

    The number(s) assigned to the release by the label(s), which can often be found on the spine or near the barcode.
    There may be more than one, especially when multiple labels are involved.

**comment**

    Disambiguation Comment - the comment entered to help distinguish one release from another (e.g.: Deluxe version with 2 bonus tracks).

**compilation**

    | (*since Picard 1.3, compatible with iTunes*) 1 for Various Artist albums, otherwise 0.
    | (*Picard 1.2 or previous*) 1 if multiple track artists (including featured artists), otherwise 0.

**copyright**

    Contain copyright message for the copyright holder of the original sound, begin with a year and a space character.

**date**

    Release Date (YYYY-MM-DD) - the date that the release was issued.

**discid**

    Disc ID is the code number which MusicBrainz uses to link a physical CD to a release listing.  This is based on the table of
    contents (TOC) information read from the disc.

**discnumber**

    Number of the disc in this release that contains this track.

**discsubtitle**

    The Media Title given to a specific disc.

**encodedby**

    Encoded by (person or organization).  Only available to the file naming script.

**encodersettings**

    Encoder Settings used.  Only available to the file naming script.

**isrc**

    International Standard Recording Code - an international standard code for uniquely identifying sound recordings and music video recordings.
    See `Wikipedia <https://en.wikipedia.org/wiki/International_Standard_Recording_Code>`_ for more information. (*since Picard 0.12*)

**key**

    Key of the music.

**label**

    Release Label Name(s).

**language**

    Work lyric language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_ if track relationships are enabled in Options and a related work exists. (*since Picard 0.10*)

**lyrics**

    Lyrics for the track.

**media**

    Release Format (e.g.: CD).  See the `Release Format <https://musicbrainz.org/doc/Release/Format>`_ page on the MusicBrainz website for more information.

**musicbrainz_albumartistid**

    Release Artist's MusicBrainz Identifier.

**musicbrainz_albumid**

    Release MusicBrainz Identifier.

**musicbrainz_artistid**

    Track Artist's MusicBrainz Identifier.

**musicbrainz_discid**

    Disc ID if the album was added using :menuselection:`"Tools --> Lookup CD"`. (*since Picard 0.12*)

**musicbrainz_originalalbumid**

    Original Release's MusicBrainz Identifier.

**musicbrainz_originalartistid**

    Original Track Artist's MusicBrainz Identifier.

**musicbrainz_recordingid**

    Recording's MusicBrainz Identifier.

**musicbrainz_releasegroupid**

    Release Group's MusicBrainz Identifier.

**musicbrainz_releasetrackid**

    Release Track MusicBrainz Identifier. (*since Picard 1.3*)

**musicbrainz_trackid**

    MusicBrainz Identifier for the track.

**musicbrainz_workid**

    MusicBrainz Identifier for the work.

.. **musicip_fingerprint**

..     MusicIP's Fingerprint.

.. **musicip_puid**

..     MusicIP PUID’s associated with the track.

**originalalbum**

    Release Title of the earliest release in the Release Group intended for the title of the original recording.

**originalartist**

    Track Artist of the earliest release in the Release Group intended for the performer(s) of the original recording.

**originaldate**

   The original release date in the format YYYY-MM-DD.  Prior to Picard version 2.6, this date was based on the earliest
   release in the Release Group providing, for example, the release date of the vinyl version of what you have on CD. As of
   Picard version 2.6, the source of the information for this tag can be selected in the :doc:`../config/options_metadata`
   section of the Options settings.  The selection options are:

   *  the first release date of the recording (varies by track)
   *  the first release date of the release group (varies by album)

   .. warning::

      If the option to use the recording release date is selected and the ``originaldate`` tag is used in the path portion of
      your file naming script, this may (and likely will) cause your album to be scattered across multiple directories.  To
      help prevent this from happening, the ``_releaseoriginaldate`` variable has been added, which will provide a consistent
      value across all tracks on a release, regardless of this option setting.

   .. note::

      If you are storing tags in MP3 files as ID3v2.3 (which is the Windows and iTunes compatible version) then the original date can only be stored as a year.

**originalyear**

   Year portion of the ``originaldate`` tag.

   .. warning::

      If the option to use the recording release date is selected and the ``originalyear`` tag is used in the path portion of
      your file naming script, this may (and likely will) cause your album to be scattered across multiple directories.  To
      help prevent this from happening, the ``_releaseoriginaldate`` variable has been added, which will provide a consistent
      value across all tracks on a release, regardless of this option setting. To get just the year portion of this variable,
      simply use ``$left(%_releaseoriginaldate%,4)``.

**releasecountry**

    Country in which the release was issued.

**releasestatus**

    Release Status indicating the "official" status of the release.  Possible values include official, promotional, bootleg, and pseudo-release.

**releasetype**

    Release Group Type (see also :ref:`_primaryreleasetype <ref_primaryreleasetype>` and :ref:`_secondaryreleasetype <ref_secondaryreleasetype>`)

**script**

    The script used to write the release's track list. The possible values are taken from the `ISO 15924 <https://en.wikipedia.org/wiki/ISO_15924>`_ standard. (*since Picard 0.10*)

**subtitle**

    Used for information directly related to the contents title.

**title**

    Track Title.

**titlesort**

    Track Title's Sort Name.

**totaldiscs**

    Total number of discs in this release

**totaltracks**

    Total tracks on this disc.

**tracknumber**

    Track number on the disc.

**website**

    Used for official artist website.

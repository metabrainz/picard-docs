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
=================================

The following tags are supported and are written in the standard format that can be read by other software. The information is populated from MusicBrainz data for most releases, without any special Picard settings. Note that some of the information such as 'lyrics' is not contained within the MusicBrainz database, and will not be provided automatically.

All of these are also available as variables for use in Picard Scripts (for tagging, for file renaming and in several other more minor settings) by wrapping them between percent '%' symbols (e.g. ``%title%``).

Some tags provide the :index:`MusicBrainz Identifier (MBID) <identifier; musicbrainz, mbid>` of the entity. The MBID is a 32-character identifier assigned to an entity (e.g.: artist, album, track or work) to uniquely identify the entity. For more information about MBIDs, please see the `MusicBrainz Identifier <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_ page in the MusicBrainz documentation.

.. note::

   Tags will not be created and will not be available as variables if there was no value retrieved for the tag from the MusicBrainz database.

.. note::

   Some of these tags are only supported for certain file types or tag formats. Please see the :doc:`Picard Tag Mapping </appendices/tag_mapping>` section for details.


Tags Provided from MusicBrainz Data
-----------------------------------

These tags will be provided based on the information from the MusicBrainz database and will be populated automatically by Picard if the information is available.

**album**

   The title of the release.

**albumartist**

   The artists primarily credited on the release, separated by the specified join phrases. These could be either "standardized" or "as credited" depending on whether the "Use standardized artist names" metadata option is enabled.

**albumartistsort**

   The release artists sort names, separated by the specified join phrases. (e.g.: "Beatles, The")

**artist**

   The track artist names, separated by the specified join phrases. These could be either "standardized" or "as credited" depending on whether the "Use standardized artist names" metadata option is enabled.

**artists**

   A multi-value tag containing the track artist names. These could be either "standardized" or "as credited" depending on whether the "Use standardized artist names" metadata option is enabled. (*since Picard 1.3*)

**artistsort**

   The track artists sort names, separated by the specified join phrases.

**asin**

   The Amazon Standard Identification Number - the number identifying the item on Amazon.

**barcode**

   The barcode assigned to the release.

**catalognumber**

   A multi-value tag contining the numbers assigned to the release by the labels, which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved.

**comment**

   The disambiguation comment entered to help distinguish one release from another (e.g.: Deluxe version with 2 bonus tracks).

**compilation**

   | 1 for Various Artist albums, otherwise empty. (*since Picard 1.3, compatible with iTunes*)
   | 1 if multiple track artists (including featured artists), otherwise 0. (*Picard 1.2 or previous*)

**date**

   The date that the release (album) was issued, in the format YYYY-MM-DD.

**discnumber**

   The number of the disc in the release that contains this track.

**discsubtitle**

   The media title given to a specific disc in the release.

**isrc**

   The International Standard Recording Code - an international standard code for uniquely identifying sound recordings and music video recordings. See `Wikipedia <https://en.wikipedia.org/wiki/International_Standard_Recording_Code>`_ for more information. (*since Picard 0.12*)

**label**

   A multi-value tag containing the names of the labels associated with the release.

**media**

   The media on which the release was distributed (e.g.: CD). See the `Release Format <https://musicbrainz.org/doc/Release/Format>`_ page on the MusicBrainz website for more information.

**musicbrainz_albumartistid**

   A multi-value tag containing the MBIDs for the release artists.

**musicbrainz_albumid**

   The MBID for the release.

**musicbrainz_artistid**

   A multi-value tag containing the MBIDs for the track artists.

**musicbrainz_discid**

   The Disc ID is the code number which MusicBrainz uses to link a physical CD to a release listing. This is based on the table of contents (TOC) information read from the disc. This tag contains the Disc ID if the album information was retrieved using :menuselection:`"Tools --> Lookup CD"`. (*since Picard 0.12*)

**musicbrainz_originalalbumid**

   The MBID for the original release. This is only available if the release has been merged with another release.

**musicbrainz_originalartistid**

   A multi-value tag containing the MBIDs for the track artists of the original recording. This is only available if the recording has been merged with another recording.

**musicbrainz_recordingid**

   The MBID for the recording.

**musicbrainz_releasegroupid**

   The MBID for the release group.

**musicbrainz_trackid**

   The MBID for the track.

**originaldate**

   The original release date in the format YYYY-MM-DD. By default this is set to the earliest release in the release group. This can provide, for example, the release date of the vinyl version of what you have on CD. (*Included as standard from Picard 0.15, and using the Original Release Date plugin if you are still using a non-NGS version earlier than Picard 0.15*)

   .. note::

      This is the same information provided in the ``_releasegroup_firstreleasedate`` variable, and is consistent across all tracks in the release. If you prefer to have this tag populated with the date of the earliest recording of the track in the database, which will likely be different for each track in the release, this can be achieved by enabling a one-line tagging script as ``$set(originaldate,%_recording_firstreleasedate%)``. Be aware that setting this can cause a release to be scattered across multiple directories if you use ``%originaldate%`` as part of the path portion of your file naming script.

   .. note::

      If you are storing tags in MP3 files as ID3v2.3 then the original date can only be stored as a year.

**originalyear**

   The year of the original release date in the format YYYY. By default this is set to the earliest release in the release group. This can provide, for example, the release year of the vinyl version of what you have on CD.

**releasecountry**

   The two-character code for the country in which the release was issued. If more than one release country was specified, this tag will contain the first one in the list.

**releasestatus**

   An indicator of the "official" status of the release. Possible values include *official*, *promotional*, *bootleg*, and *pseudo-release*.

**releasetype**

   A multi-value tag containing the types of release assigned to the release group. See also :ref:`_primaryreleasetype <ref_primaryreleasetype>` and :ref:`_secondaryreleasetype <ref_secondaryreleasetype>`.

**script**

   The script used to write the release's track list. The possible values are taken from the `ISO 15924 <https://en.wikipedia.org/wiki/ISO_15924>`_ standard. (*since Picard 0.10*)

**title**

   The title of the track.

**totaldiscs**

   The total number of discs in this release.

**totaltracks**

   The total number of tracks on this disc.

**tracknumber**

   The number of the track on the disc.

**website**

   The official website for the artist.


Tags Not Provided from MusicBrainz Data
---------------------------------------

These tags are not able to be populated by stock Picard, however they may be used and populated by certain plugins or scripts.

**acoustid_fingerprint**

   The Acoustic Fingerprint for the track. The fingerprint is based on the audio information found in a file, and is calculated using the `Chromaprint <https://acoustid.org/chromaprint>`_ software.

**acoustid_id**

   The AcoustID associated with the track. The AcoustID is the identifier assigned to an audio file based on its acoustic fingerprint. Multiple fingerprints may be assigned the same AcoustID if the fingerprints are similar enough. See the section on :doc:`Understanding Acoustic Fingerprinting and AcoustIDs </tutorials/acoustid>` for more information.

**albumsort**

   The sort name of the title of the release.

**bpm**

   The number of beats per minute of the track.

**copyright**

   The copyright message for the copyright holder of the original sound, beginning with a year and a space character.

**encodedby**

   The person or organization that encoded the track.

**encodersettings**

   The settings used when encoding the track.

**key**

   The key of the music.

**lyrics**

   The lyrics for the track.

**musicip_fingerprint**

   The MusicIP Fingerprint for the track.

**musicip_puid**

   The MusicIP PUIDs associated with the track.

**originalalbum**

   The release title of the earliest release in the release group intended for the title of the original recording.

**originalartist**

   The track artist of the earliest release in the release group intended for the performers of the original recording.

**originalfilename**

   The original name of the audio file.

**releasedate**

   Explicit tag for the release date (*since Picard 2.9*). This tag exists for specific use in scripts and plugins, but is not filled by default. In most cases it is recommended to use the ``date`` tag instead for compatibility with existing software.

**showmovement**

   The work and movement of the track.

**subtitle**

   This is used for information directly related to the contents title.

**titlesort**

   The sort name of the track title.


iTunes-Specific Tags
--------------------

These tags are only available in iTunes files and are not able to be populated by stock Picard, however they may be used and populated by certain plugins or scripts.

**gapless**

   Indicates whether or not there are gaps between the recordings on the release.

**podcast**

   Indicates whether or not the recording is a podcast.

**podcasturl**

   The associated url if the recording is a podcast.

**show**

   The name of the show if the recording is associated with a television program.

**showsort**

   The sort name of the show if the recording is associated with a television program.

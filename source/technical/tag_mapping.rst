.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Tag Mapping
===========

.. index::
   pair: mapping; tags

The following is a mapping between Picard internal tag names and those used by various tagging formats.


AcoustID
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``acoustid_id``"
   "ID3v2", "``TXXX:Acoustid Id``"
   "Vorbis", "``ACOUSTID_ID``"
   "APEv2", "``ACOUSTID_ID``"
   "iTunes MP4", "``----:com.apple.iTunes:Acoustid Id``"
   "ASF/Windows Media", "``Acoustid/Id``"


AcoustID Fingerprint
--------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``acoustid_fingerprint``"
   "ID3v2", "``TXXX:Acoustid Fingerprint``"
   "Vorbis", "``ACOUSTID_FINGERPRINT``"
   "APEv2", "``ACOUSTID_FINGERPRINT``"
   "iTunes MP4", "``----:com.apple.iTunes:Acoustid Fingerprint``"
   "ASF/Windows Media", "``Acoustid/Fingerprint``"


Album
-----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``album``"
   "ID3v2", "``TALB``"
   "Vorbis", "``ALBUM``"
   "APEv2", "``Album``"
   "iTunes MP4", "``©alb``"
   "ASF/Windows Media", "``WM/AlbumTitle``"


Album Artist
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``albumartist``"
   "ID3v2", "``TPE2``"
   "Vorbis", "``ALBUMARTIST``"
   "APEv2", "``Album Artist``"
   "iTunes MP4", "``aART``"
   "ASF/Windows Media", "``WM/AlbumArtist``"


Album Artist Sort Order
-----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``albumartistsort``"
   "ID3v2", "``TSO2`` (Picard>=1.2) ``TXXX:ALBUMARTISTSORT`` (Picard<=1.1)"
   "Vorbis", "``ALBUMARTISTSORT``"
   "APEv2", "``ALBUMARTISTSORT``"
   "iTunes MP4", "``soaa``"
   "ASF/Windows Media", "``WM/AlbumArtistSortOrder``"


Album Sort Order [#f4]_
-----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``albumsort``"
   "ID3v2", "``TSOA``"
   "Vorbis", "``ALBUMSORT``"
   "APEv2", "``ALBUMSORT``"
   "iTunes MP4", "``soal``"
   "ASF/Windows Media", "``WM/AlbumSortOrder``"


Arranger
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``arranger``"
   "ID3v2", "``TIPL:arranger`` (id3v24) ``IPLS:arranger`` (id3v23)"
   "Vorbis", "``ARRANGER``"
   "APEv2", "``Arranger``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "n/a"


Artist
------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``artist``"
   "ID3v2", "``TPE1``"
   "Vorbis", "``ARTIST``"
   "APEv2", "``Artist``"
   "iTunes MP4", "``©ART``"
   "ASF/Windows Media", "``Author``"


Artist Sort Order
-----------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``artistsort``"
   "ID3v2", "``TSOP``"
   "Vorbis", "``ARTISTSORT``"
   "APEv2", "``ARTISTSORT``"
   "iTunes MP4", "``soar``"
   "ASF/Windows Media", "``WM/ArtistSortOrder``"


Artists
-------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``artists``"
   "ID3v2", "``TXXX:Artists``"
   "Vorbis", "``ARTISTS``"
   "APEv2", "``Artists``"
   "iTunes MP4", "``----:com.apple.iTunes:ARTISTS``"
   "ASF/Windows Media", "``WM/ARTISTS``"


ASIN
----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``asin``"
   "ID3v2", "``TXXX:ASIN``"
   "Vorbis", "``ASIN``"
   "APEv2", "``ASIN``"
   "iTunes MP4", "``----:com.apple.iTunes:ASIN``"
   "ASF/Windows Media", "``ASIN``"


Barcode
-------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``barcode``"
   "ID3v2", "``TXXX:BARCODE``"
   "Vorbis", "``BARCODE``"
   "APEv2", "``Barcode``"
   "iTunes MP4", "``----:com.apple.iTunes:BARCODE``"
   "ASF/Windows Media", "``WM/Barcode``"


BPM [#f4]_
----------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``bpm``"
   "ID3v2", "``TBPM``"
   "Vorbis", "``BPM``"
   "APEv2", "``BPM``"
   "iTunes MP4", "``tmpo``"
   "ASF/Windows Media", "``WM/BeatsPerMinute``"


Catalog Number
--------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``catalognumber``"
   "ID3v2", "``TXXX:CATALOGNUMBER``"
   "Vorbis", "``CATALOGNUMBER``"
   "APEv2", "``CatalogNumber``"
   "iTunes MP4", "``----:com.apple.iTunes:CATALOGNUMBER``"
   "ASF/Windows Media", "``WM/CatalogNo``"


Comment [#f4]_
--------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``comment:description``"
   "ID3v2", "``COMM:description``"
   "Vorbis", "``COMMENT``"
   "APEv2", "``Comment``"
   "iTunes MP4", "``©cmt``"
   "ASF/Windows Media", "``Description``"


Compilation (iTunes) [#f5]_
---------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``compilation``"
   "ID3v2", "``TCMP``"
   "Vorbis", "``COMPILATION``"
   "APEv2", "``Compilation``"
   "iTunes MP4", "``cpil``"
   "ASF/Windows Media", "``WM/IsCompilation``"


Composer
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``composer``"
   "ID3v2", "``TCOM``"
   "Vorbis", "``COMPOSER``"
   "APEv2", "``Composer``"
   "iTunes MP4", "``©wrt``"
   "ASF/Windows Media", "``WM/Composer``"


Composer Sort Order
-------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``composersort``"
   "ID3v2", "``TSOC`` (Picard>=1.3) ``TXXX:COMPOSERSORT`` (Picard<=1.2)"
   "Vorbis", "``COMPOSERSORT``"
   "APEv2", "``COMPOSERSORT``"
   "iTunes MP4", "``soco``"
   "ASF/Windows Media", "``WM/ComposerSortOrder`` (Picard>=1.3)"


Conductor
---------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``conductor``"
   "ID3v2", "``TPE3``"
   "Vorbis", "``CONDUCTOR``"
   "APEv2", "``Conductor``"
   "iTunes MP4", "``----:com.apple.iTunes:CONDUCTOR``"
   "ASF/Windows Media", "``WM/Conductor``"


Copyright [#f4]_
----------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``copyright``"
   "ID3v2", "``TCOP``"
   "Vorbis", "``COPYRIGHT``"
   "APEv2", "``Copyright``"
   "iTunes MP4", "``cprt``"
   "ASF/Windows Media", "``Copyright``"


Disc Number
-----------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``discnumber``"
   "ID3v2", "``TPOS``"
   "Vorbis", "``DISCNUMBER``"
   "APEv2", "``Disc``"
   "iTunes MP4", "``disk``"
   "ASF/Windows Media", "``WM/PartOfSet``"


Disc Subtitle
-------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``discsubtitle``"
   "ID3v2", "``TSST`` (id3v24 only)"
   "Vorbis", "``DISCSUBTITLE``"
   "APEv2", "``DiscSubtitle``"
   "iTunes MP4", "``----:com.apple.iTunes:DISCSUBTITLE``"
   "ASF/Windows Media", "``WM/SetSubTitle``"


Encoded By [#f4]_
-----------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``encodedby``"
   "ID3v2", "``TENC``"
   "Vorbis", "``ENCODEDBY``"
   "APEv2", "``EncodedBy``"
   "iTunes MP4", "``©too``"
   "ASF/Windows Media", "``WM/EncodedBy``"


Encoder Settings [#f4]_
-----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``encodersettings``"
   "ID3v2", "``TSSE``"
   "Vorbis", "``ENCODERSETTINGS``"
   "APEv2", "``EncoderSettings``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/EncodingSettings`` (Picard>=1.3.1)"


Engineer
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``engineer``"
   "ID3v2", "``TIPL:engineer`` (id3v24) ``IPLS:engineer`` (id3v23)"
   "Vorbis", "``ENGINEER``"
   "APEv2", "``Engineer``"
   "iTunes MP4", "``----:com.apple.iTunes:ENGINEER``"
   "ASF/Windows Media", "``WM/Engineer``"


Gapless Playback [#f4]_
-----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``gapless``"
   "ID3v2", "n/a"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "``pgap``"
   "ASF/Windows Media", "n/a"


Genre
-----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``genre``"
   "ID3v2", "``TCON``"
   "Vorbis", "``GENRE``"
   "APEv2", "``Genre``"
   "iTunes MP4", "``©gen``"
   "ASF/Windows Media", "``WM/Genre``"


Grouping [#f3]_
---------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``grouping``"
   "ID3v2", "``TIT1`` ``GRP1`` [#f8]_"
   "Vorbis", "``GROUPING``"
   "APEv2", "``Grouping``"
   "iTunes MP4", "``©grp``"
   "ASF/Windows Media", "``WM/ContentGroupDescription``"


Initial key (Picard>=1.4)
-------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``key``"
   "ID3v2", "``TKEY``"
   "Vorbis", "``KEY``"
   "APEv2", "``KEY``"
   "iTunes MP4", "``----:com.apple.iTunes:initialkey``"
   "ASF/Windows Media", "``WM/InitialKey``"


ISRC
----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``isrc``"
   "ID3v2", "``TSRC``"
   "Vorbis", "``ISRC``"
   "APEv2", "``ISRC``"
   "iTunes MP4", "``----:com.apple.iTunes:ISRC``"
   "ASF/Windows Media", "``WM/ISRC``"


Language
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``language``"
   "ID3v2", "``TLAN``"
   "Vorbis", "``LANGUAGE``"
   "APEv2", "``Language``"
   "iTunes MP4", "``----:com.apple.iTunes:LANGUAGE``"
   "ASF/Windows Media", "``WM/Language``"


License [#f6]_ [#f7]_
---------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``license``"
   "ID3v2", "``WCOP`` (single URL) ``TXXX:LICENSE`` (multiple or non-URL)"
   "Vorbis", "``LICENSE``"
   "APEv2", "``LICENSE``"
   "iTunes MP4", "``----:com.apple.iTunes:LICENSE``"
   "ASF/Windows Media", "n/a"


Lyricist
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``lyricist``"
   "ID3v2", "``TEXT``"
   "Vorbis", "``LYRICIST``"
   "APEv2", "``Lyricist``"
   "iTunes MP4", "``----:com.apple.iTunes:LYRICIST``"
   "ASF/Windows Media", "``WM/Writer``"


Lyrics [#f4]_
-------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``lyrics:description``"
   "ID3v2", "``USLT:description``"
   "Vorbis", "``LYRICS``"
   "APEv2", "``Lyrics``"
   "iTunes MP4", "``©lyr``"
   "ASF/Windows Media", "``WM/Lyrics``"


Media
-----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``media``"
   "ID3v2", "``TMED``"
   "Vorbis", "``MEDIA``"
   "APEv2", "``Media``"
   "iTunes MP4", "``----:com.apple.iTunes:MEDIA``"
   "ASF/Windows Media", "``WM/Media``"


Mix-DJ
------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``djmixer``"
   "ID3v2", "``TIPL:DJ-mix`` (id3v24) ``IPLS:DJ-mix`` (id3v23)"
   "Vorbis", "``DJMIXER``"
   "APEv2", "``DJMixer``"
   "iTunes MP4", "``----:com.apple.iTunes:DJMIXER``"
   "ASF/Windows Media", "``WM/DJMixer``"


Mixer
-----
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``mixer``"
   "ID3v2", "``TIPL:mix`` (id3v24) ``IPLS:mix`` (id3v23)"
   "Vorbis", "``MIXER``"
   "APEv2", "``Mixer``"
   "iTunes MP4", "``----:com.apple.iTunes:MIXER``"
   "ASF/Windows Media", "``WM/Mixer``"


Mood [#f3]_
-----------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``mood``"
   "ID3v2", "``TMOO`` (id3v24 only)"
   "Vorbis", "``MOOD``"
   "APEv2", "``Mood``"
   "iTunes MP4", "``----:com.apple.iTunes:MOOD``"
   "ASF/Windows Media", "``WM/Mood``"


Movement [#f4]_ (Picard>=2.1)
-----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``movement``"
   "ID3v2", "``MVNM``"
   "Vorbis", "``MOVEMENTNAME``"
   "APEv2", "``MOVEMENTNAME``"
   "iTunes MP4", "``©mvn``"
   "ASF/Windows Media", "n/a"


Movement Count [#f4]_ (Picard>=2.1)
-----------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``movementtotal``"
   "ID3v2", "``MVIN``"
   "Vorbis", "``MOVEMENTTOTAL``"
   "APEv2", "``MOVEMENTTOTAL``"
   "iTunes MP4", "``mvc``"
   "ASF/Windows Media", "n/a"


Movement Number [#f4]_ (Picard>=2.1)
------------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``movementnumber``"
   "ID3v2", "``MVIN``"
   "Vorbis", "``MOVEMENT``"
   "APEv2", "``MOVEMENT``"
   "iTunes MP4", "``mvi``"
   "ASF/Windows Media", "n/a"


MusicBrainz Artist Id
---------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_artistid``"
   "ID3v2", "``TXXX:MusicBrainz Artist Id``"
   "Vorbis", "``MUSICBRAINZ_ARTISTID``"
   "APEv2", "``MUSICBRAINZ_ARTISTID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Artist Id``"
   "ASF/Windows Media", "``MusicBrainz/Artist Id``"


MusicBrainz Disc Id
-------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_discid``"
   "ID3v2", "``TXXX:MusicBrainz Disc Id``"
   "Vorbis", "``MUSICBRAINZ_DISCID``"
   "APEv2", "``MUSICBRAINZ_DISCID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Disc Id``"
   "ASF/Windows Media", "``MusicBrainz/Disc Id``"


MusicBrainz Original Artist Id
------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_originalartistid``"
   "ID3v2", "``TXXX:MusicBrainz Original Artist Id``"
   "Vorbis", "``MUSICBRAINZ_ORIGINALARTISTID``"
   "APEv2", "n/a"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Original Artist Id`` (Picard>=2.1)"
   "ASF/Windows Media", "``MusicBrainz/Original Artist Id`` (Picard>=2.1)"


MusicBrainz Original Release Id
-------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_originalalbumid``"
   "ID3v2", "``TXXX:MusicBrainz Original Album Id``"
   "Vorbis", "``MUSICBRAINZ_ORIGINALALBUMID``"
   "APEv2", "n/a"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Original Album Id`` (Picard>=2.1)"
   "ASF/Windows Media", "``MusicBrainz/Original Album Id`` (Picard>=2.1)"


MusicBrainz Recording Id
------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_recordingid``"
   "ID3v2", "``UFID://musicbrainz.org``"
   "Vorbis", "``MUSICBRAINZ_TRACKID``"
   "APEv2", "``MUSICBRAINZ_TRACKID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Track Id``"
   "ASF/Windows Media", "``MusicBrainz/Track Id``"


MusicBrainz Release Artist Id
-----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_albumartistid``"
   "ID3v2", "``TXXX:MusicBrainz Album Artist Id``"
   "Vorbis", "``MUSICBRAINZ_ALBUMARTISTID``"
   "APEv2", "``MUSICBRAINZ_ALBUMARTISTID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Album Artist Id``"
   "ASF/Windows Media", "``MusicBrainz/Album Artist Id``"


MusicBrainz Release Group Id
----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_releasegroupid``"
   "ID3v2", "``TXXX:MusicBrainz Release Group Id``"
   "Vorbis", "``MUSICBRAINZ_RELEASEGROUPID``"
   "APEv2", "``MUSICBRAINZ_RELEASEGROUPID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Release Group Id``"
   "ASF/Windows Media", "``MusicBrainz/Release Group Id``"


MusicBrainz Release Id
----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_albumid``"
   "ID3v2", "``TXXX:MusicBrainz Album Id``"
   "Vorbis", "``MUSICBRAINZ_ALBUMID``"
   "APEv2", "``MUSICBRAINZ_ALBUMID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Album Id``"
   "ASF/Windows Media", "``MusicBrainz/Album Id``"


MusicBrainz Track Id
--------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_trackid``"
   "ID3v2", "``TXXX:MusicBrainz Release Track Id``"
   "Vorbis", "``MUSICBRAINZ_RELEASETRACKID``"
   "APEv2", "``MUSICBRAINZ_RELEASETRACKID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Release Track Id``"
   "ASF/Windows Media", "``MusicBrainz/Release Track Id``"


MusicBrainz TRM Id
------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_trmid``"
   "ID3v2", "``TXXX:MusicBrainz TRM Id``"
   "Vorbis", "``MUSICBRAINZ_TRMID``"
   "APEv2", "``MUSICBRAINZ_TRMID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz TRM Id``"
   "ASF/Windows Media", "``MusicBrainz/TRM Id``"


MusicBrainz Work Id
-------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicbrainz_workid``"
   "ID3v2", "``TXXX:MusicBrainz Work Id``"
   "Vorbis", "``MUSICBRAINZ_WORKID``"
   "APEv2", "``MUSICBRAINZ_WORKID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Work Id``"
   "ASF/Windows Media", "``MusicBrainz/Work Id``"


MusicIP Fingerprint
-------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicip_fingerprint``"
   "ID3v2", "``TXXX:MusicMagic Fingerprint``"
   "Vorbis", "``FINGERPRINT=MusicMagic Fingerprint {fingerprint}``"
   "APEv2", "n/a"
   "iTunes MP4", "``----:com.apple.iTunes:fingerprint``"
   "ASF/Windows Media", "n/a"


MusicIP PUID
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``musicip_puid``"
   "ID3v2", "``TXXX:MusicIP PUID``"
   "Vorbis", "``MUSICIP_PUID``"
   "APEv2", "``MUSICIP_PUID``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicIP PUID``"
   "ASF/Windows Media", "``MusicIP/PUID``"


Original Album
--------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``originalalbum``"
   "ID3v2", "``TOAL``"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/OriginalAlbumTitle`` (Picard>=2.1)"


Original Artist
---------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``originalartist``"
   "ID3v2", "``TOPE``"
   "Vorbis", "n/a"
   "APEv2", "``Original Artist`` (Picard>=2.1)"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/OriginalArtist`` (Picard>=2.1)"


Original Release Date [#f1]_
----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``originaldate``"
   "ID3v2", "``TDOR`` (id3v24) ``TORY`` (id3v23)"
   "Vorbis", "``ORIGINALDATE``"
   "APEv2", "n/a"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/OriginalReleaseTime`` (Picard>=1.3.1) ``WM/OriginalReleaseYear`` (Picard<=1.3.0)"


Original Release Year [#f1]_
----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``originalyear``"
   "ID3v2", "n/a"
   "Vorbis", "``ORIGINALYEAR``"
   "APEv2", "``ORIGINALYEAR``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/OriginalReleaseYear`` (Picard>=1.3.1)"


Performer (instrument)
----------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``performer:instrument``"
   "ID3v2", "``TMCL:instrument`` (id3v24) ``IPLS:instrument`` (id3v23)"
   "Vorbis", "``PERFORMER={artist} (instrument)``"
   "APEv2", "``Performer={artist} (instrument)``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "n/a"


Podcast [#f4]_
--------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``podcast``"
   "ID3v2", "n/a"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "``pcst``"
   "ASF/Windows Media", "n/a"


Podcast URL [#f4]_
------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``podcasturl``"
   "ID3v2", "n/a"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "``purl``"
   "ASF/Windows Media", "n/a"


Producer
--------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``producer``"
   "ID3v2", "``TIPL:producer`` (id3v24) ``IPLS:producer`` (id3v23)"
   "Vorbis", "``PRODUCER``"
   "APEv2", "``Producer``"
   "iTunes MP4", "``----:com.apple.iTunes:PRODUCER``"
   "ASF/Windows Media", "``WM/Producer``"


Rating
------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``_rating``"
   "ID3v2", "``POPM``"
   "Vorbis", "``RATING:user@email``"
   "APEv2", "n/a"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/SharedUserRating``"


Record Label
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``label``"
   "ID3v2", "``TPUB``"
   "Vorbis", "``LABEL``"
   "APEv2", "``Label``"
   "iTunes MP4", "``----:com.apple.iTunes:LABEL``"
   "ASF/Windows Media", "``WM/Publisher``"


Release Country
---------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``releasecountry``"
   "ID3v2", "``TXXX:MusicBrainz Album Release Country``"
   "Vorbis", "``RELEASECOUNTRY``"
   "APEv2", "``RELEASECOUNTRY``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Album Release Country``"
   "ASF/Windows Media", "``MusicBrainz/Album Release Country``"


Release Date
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``date``"
   "ID3v2", "``TDRC`` (id3v24) ``TYER`` + ``TDAT`` (id3v23)"
   "Vorbis", "``DATE``"
   "APEv2", "``Year``"
   "iTunes MP4", "``©day``"
   "ASF/Windows Media", "``WM/Year``"


Release Status
--------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``releasestatus``"
   "ID3v2", "``TXXX:MusicBrainz Album Status``"
   "Vorbis", "``RELEASESTATUS``"
   "APEv2", "``MUSICBRAINZ_ALBUMSTATUS``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Album Status``"
   "ASF/Windows Media", "``MusicBrainz/Album Status``"


Release Type
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``releasetype``"
   "ID3v2", "``TXXX:MusicBrainz Album Type``"
   "Vorbis", "``RELEASETYPE``"
   "APEv2", "``MUSICBRAINZ_ALBUMTYPE``"
   "iTunes MP4", "``----:com.apple.iTunes:MusicBrainz Album Type``"
   "ASF/Windows Media", "``MusicBrainz/Album Type``"


Remixer
-------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``remixer``"
   "ID3v2", "``TPE4``"
   "Vorbis", "``REMIXER``"
   "APEv2", "``MixArtist``"
   "iTunes MP4", "``----:com.apple.iTunes:REMIXER``"
   "ASF/Windows Media", "``WM/ModifiedBy``"


ReplayGain Album Gain (Picard>=2.2)
-----------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_album_gain``"
   "ID3v2", "``TXXX:REPLAYGAIN_ALBUM_GAIN``"
   "Vorbis", "``REPLAYGAIN_ALBUM_GAIN``"
   "APEv2", "``REPLAYGAIN_ALBUM_GAIN``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_GAIN``"
   "ASF/Windows Media", "``REPLAYGAIN_ALBUM_GAIN``"


ReplayGain Album Peak (Picard>=2.2)
-----------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_album_peak``"
   "ID3v2", "``TXXX:REPLAYGAIN_ALBUM_PEAK``"
   "Vorbis", "``REPLAYGAIN_ALBUM_PEAK``"
   "APEv2", "``REPLAYGAIN_ALBUM_PEAK``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_PEAK``"
   "ASF/Windows Media", "``REPLAYGAIN_ALBUM_PEAK``"


ReplayGain Album Range (Picard>=2.2)
------------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_album_range``"
   "ID3v2", "``TXXX:REPLAYGAIN_ALBUM_RANGE``"
   "Vorbis", "``REPLAYGAIN_ALBUM_RANGE``"
   "APEv2", "``REPLAYGAIN_ALBUM_RANGE``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_RANGE``"
   "ASF/Windows Media", "``REPLAYGAIN_ALBUM_RANGE``"


ReplayGain Reference Loudness (Picard>=2.2)
-------------------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_reference_loudness``"
   "ID3v2", "``TXXX:REPLAYGAIN_REFERENCE_LOUDNESS``"
   "Vorbis", "``REPLAYGAIN_REFERENCE_LOUDNESS``"
   "APEv2", "``REPLAYGAIN_REFERENCE_LOUDNESS``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_REFERENCE_LOUDNESS``"
   "ASF/Windows Media", "``REPLAYGAIN_REFERENCE_LOUDNESS``"


ReplayGain Track Gain (Picard>=2.2)
-----------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_track_gain``"
   "ID3v2", "``TXXX:REPLAYGAIN_TRACK_GAIN``"
   "Vorbis", "``REPLAYGAIN_TRACK_GAIN``"
   "APEv2", "``REPLAYGAIN_TRACK_GAIN``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_TRACK_GAIN``"
   "ASF/Windows Media", "``REPLAYGAIN_TRACK_GAIN``"


ReplayGain Track Peak (Picard>=2.2)
-----------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_track_peak``"
   "ID3v2", "``TXXX:REPLAYGAIN_TRACK_PEAK``"
   "Vorbis", "``REPLAYGAIN_TRACK_PEAK``"
   "APEv2", "``REPLAYGAIN_TRACK_PEAK``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_TRACK_PEAK``"
   "ASF/Windows Media", "``REPLAYGAIN_TRACK_PEAK``"


ReplayGain Track Range (Picard>=2.2)
------------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``replaygain_track_range``"
   "ID3v2", "``TXXX:REPLAYGAIN_TRACK_RANGE``"
   "Vorbis", "``REPLAYGAIN_TRACK_RANGE``"
   "APEv2", "``REPLAYGAIN_TRACK_RANGE``"
   "iTunes MP4", "``----:com.apple.iTunes:REPLAYGAIN_TRACK_RANGE``"
   "ASF/Windows Media", "``REPLAYGAIN_TRACK_RANGE``"


Script
------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``script``"
   "ID3v2", "``TXXX:SCRIPT``"
   "Vorbis", "``SCRIPT``"
   "APEv2", "``Script``"
   "iTunes MP4", "``----:com.apple.iTunes:SCRIPT``"
   "ASF/Windows Media", "``WM/Script``"


Show Name [#f4]_
----------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``show``"
   "ID3v2", "n/a"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "``tvsh``"
   "ASF/Windows Media", "n/a"


Show Name Sort Order [#f4]_
---------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``showsort``"
   "ID3v2", "n/a"
   "Vorbis", "n/a"
   "APEv2", "n/a"
   "iTunes MP4", "``sosn``"
   "ASF/Windows Media", "n/a"


Show Work & Movement [#f4]_ (Picard>=2.1)
-----------------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``showmovement``"
   "ID3v2", "``TXXX:SHOWMOVEMENT``"
   "Vorbis", "``SHOWMOVEMENT``"
   "APEv2", "``SHOWMOVEMENT``"
   "iTunes MP4", "``shwm``"
   "ASF/Windows Media", "n/a"


Subtitle [#f4]_
---------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``subtitle``"
   "ID3v2", "``TIT3``"
   "Vorbis", "``SUBTITLE``"
   "APEv2", "``Subtitle``"
   "iTunes MP4", "``----:com.apple.iTunes:SUBTITLE``"
   "ASF/Windows Media", "``WM/SubTitle``"


Total Discs
-----------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``totaldiscs``"
   "ID3v2", "``TPOS``"
   "Vorbis", "``DISCTOTAL and TOTALDISCS``"
   "APEv2", "``Disc``"
   "iTunes MP4", "``disk``"
   "ASF/Windows Media", "``WM/PartOfSet`` (Picard>=1.3.1)"


Total Tracks
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``totaltracks``"
   "ID3v2", "``TRCK``"
   "Vorbis", "``TRACKTOTAL and TOTALTRACKS``"
   "APEv2", "``Track``"
   "iTunes MP4", "``trkn``"
   "ASF/Windows Media", "n/a"


Track Number
------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``tracknumber``"
   "ID3v2", "``TRCK``"
   "Vorbis", "``TRACKNUMBER``"
   "APEv2", "``Track``"
   "iTunes MP4", "``trkn``"
   "ASF/Windows Media", "``WM/TrackNumber``"


Track Title
-----------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``title``"
   "ID3v2", "``TIT2``"
   "Vorbis", "``TITLE``"
   "APEv2", "``Title``"
   "iTunes MP4", "``©nam``"
   "ASF/Windows Media", "``Title``"


Track Title Sort Order [#f4]_
-----------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``titlesort``"
   "ID3v2", "``TSOT``"
   "Vorbis", "``TITLESORT``"
   "APEv2", "``TITLESORT``"
   "iTunes MP4", "``sonm``"
   "ASF/Windows Media", "``WM/TitleSortOrder``"


Website (official artist website)
---------------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``website``"
   "ID3v2", "``WOAR``"
   "Vorbis", "``WEBSITE``"
   "APEv2", "``Weblink``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "``WM/AuthorURL`` (Picard>=1.3.1)"


Work Title (Picard>=1.3)
------------------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``work``"
   "ID3v2", "``TXXX:WORK`` ``TIT1`` [#f8]_"
   "Vorbis", "``WORK``"
   "APEv2", "``WORK``"
   "iTunes MP4", "``©wrk`` (Picard>=2.1)"
   "ASF/Windows Media", "``WM/Work``"


Writer [#f2]_
-------------
.. csv-table::
   :width: 100%
   :widths: 35 100

   "Internal Name", "``writer``"
   "ID3v2", "``TXXX:Writer`` (Picard>=1.3)"
   "Vorbis", "``WRITER``"
   "APEv2", "``Writer``"
   "iTunes MP4", "n/a"
   "ASF/Windows Media", "n/a"


.. only:: html

   .. rubric:: Footnotes:

.. [#f1] Taken from the earliest release in the release group.
.. [#f2] Used when uncertain whether composer or lyricist.
.. [#f3] This is populated by LastFMPlus plugin and not by stock Picard.
.. [#f4] This is not able to be populated by stock Picard. It may be used and populated by certain plugins.
.. [#f5] For Picard>=1.3 this indicates a Various Artists album; for Picard<=1.2 this indicates albums with tracks by different artists (which is incorrect (e.g.: an original album with a duet with a feat. artist would show as a Compilation). In neither case does this indicate a MusicBrainz Release Group subtype of compilation.
.. [#f6] Release-level license relationship type.
.. [#f7] Recording-level license relationship type.
.. [#f8] With "Save iTunes compatible grouping and work" (since Picard>=2.1.0)

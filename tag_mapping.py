#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Module to maintain tag mapping information and to automatically generate the
tag mapping pages, HTML table and Excel spreadsheet.
"""

# Tag Reference Table by outsidecontext:
# https://docs.google.com/spreadsheets/d/1afugW3R1FRDN-mwt5SQLY4R7aLAu3RqzjN3pR1497Ok/edit#gid=0

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

import re
import sys

import xlsxwriter

# Column headings to use for the table
#
# Each tuple comprises the following:
#  - the key used to get the corresponding value for each tag from the tag's dictionary.
#  - the name to print in the table header
#  - the width to set for the column in the spreadsheet
#  - The width to set the column in the HTML table (in pixels)
#
# Each item name may contain RST links but not newlines.  References to notes
# may be included by enclosing the note number in square brackets (e.g.: [1]).  If
# there are multiple note references, each should be entered within its own set of
# square brackets (e.g.: [1] [2]).
COLUMNS = [
    ("tag_name", "Tag Name", 30, 250),
    ("picard_name", "Internal Name", 50, 350),
    ("id3v2", "ID3v2", 50, 450),
    ("vorbis", "Vorbis", 50, 350),
    ("apev2", "APEv2", 30, 250),
    ("itunes", "iTunes MP4", 60, 550),
    ("wmp", "ASF/Windows Media", 60, 500),
    ("riff", "RIFF INFO", 20, 150),
]

# Notes to display below the tag information
#
# Notes may include RST links and newlines.
NOTES = {
    1: "Taken from the earliest release in the release group.",
    2: "Used when uncertain whether composer or lyricist.",
    3: "This is populated by LastFMPlus plugin and not by stock Picard.",
    4: "This is not able to be populated by stock Picard. It may be used and populated by certain plugins.",
    5: "For Picard>=1.3 this indicates a Various Artists album; for Picard<=1.2 this indicates albums with tracks by different artists which is incorrect (e.g.: an original album with a duet with a feat. artist would show as a Compilation). In neither case does this indicate a MusicBrainz Release Group subtype of compilation.",
    6: "`Release-level license <https://musicbrainz.org/relationship/004bd0c3-8a45-4309-ba52-fa99f3aa3d50>`_ relationship type.",
    7: "`Recording-level license <https://musicbrainz.org/relationship/f25e301d-b87b-4561-86a0-5d2df6d26c0a>`_ relationship type.",
    8: "With \"Save iTunes compatible grouping and work\" (since Picard>=2.1.0)",
}
NOTES_NUMBERS = list(NOTES.keys())
NOTES_NUMBERS.sort()

# Tag Mapping information
#
# Each list item is a dictionary comprising the following keys:
#  - tag_name: the name / title of the tag
#  - picard_name: the tag name used by Picard
#  - id3v2: the "ID3v2" tag information
#  - vorbis: the "Vorbis" tag information
#  - apev2: the "APEv2" tag information
#  - itunes: the "iTunes MP4" tag information
#  - wmp: the "ASF/Windows Media" tag information
#  - riff: the "RIFF INFO" tag information
#  - seealso: additional information to be included in a "See Also" block in RST files produced. (optional)
#
# Each item may contain RST links and newlines.  References to notes
# may be included by enclosing the note number in square brackets (e.g.: [1]).  If
# there are multiple note references, each should be entered within its own set of
# square brackets (e.g.: [1] [2]).
TAG_MAP = [
    {
        "tag_name": "AcoustID",
        "picard_name": "``acoustid_id``",
        "id3v2": "``TXXX:Acoustid Id``",
        "vorbis": "``ACOUSTID_ID``",
        "apev2": "``ACOUSTID_ID``",
        "itunes": "``----:com.apple.iTunes:Acoustid Id``",
        "wmp": "``Acoustid/Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "AcoustID Fingerprint",
        "picard_name": "``acoustid_fingerprint``",
        "id3v2": "``TXXX:Acoustid Fingerprint``",
        "vorbis": "``ACOUSTID_FINGERPRINT``",
        "apev2": "``ACOUSTID_FINGERPRINT``",
        "itunes": "``----:com.apple.iTunes:Acoustid Fingerprint``",
        "wmp": "``Acoustid/Fingerprint``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Album <https://musicbrainz.org/doc/Release_Title>`_",
        "picard_name": "``album``",
        "id3v2": "``TALB``",
        "vorbis": "``ALBUM``",
        "apev2": "``Album``",
        "itunes": "``©alb``",
        "wmp": "``WM/AlbumTitle``",
        "riff": "``IPRD``",
    },

    {
        "tag_name": "`Album Artist <https://musicbrainz.org/doc/Release_Artist>`_",
        "picard_name": "``albumartist``",
        "id3v2": "``TPE2``",
        "vorbis": "``ALBUMARTIST``",
        "apev2": "``Album Artist``",
        "itunes": "``aART``",
        "wmp": "``WM/AlbumArtist``",
        "riff": "n/a",
    },

    {
        "tag_name": "Album Artist Sort Order",
        "picard_name": "``albumartistsort``",
        "id3v2": "``TSO2`` (Picard>=1.2)\n``TXXX:ALBUMARTISTSORT`` (Picard<=1.1)",
        "vorbis": "``ALBUMARTISTSORT``",
        "apev2": "``ALBUMARTISTSORT``",
        "itunes": "``soaa``",
        "wmp": "``WM/AlbumArtistSortOrder``",
        "riff": "n/a",
    },

    {
        "tag_name": "Album Sort Order [4]",
        "picard_name": "``albumsort``",
        "id3v2": "``TSOA``",
        "vorbis": "``ALBUMSORT``",
        "apev2": "``ALBUMSORT``",
        "itunes": "``soal``",
        "wmp": "``WM/AlbumSortOrder``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Arranger <https://musicbrainz.org/relationship/22661fb8-cdb7-4f67-8385-b2a8be6c9f0d>`_",
        "picard_name": "``arranger``",
        "id3v2": "``TIPL:arranger`` (ID3v2.4)\n``IPLS:arranger`` (ID3v2.3)",
        "vorbis": "``ARRANGER``",
        "apev2": "``Arranger``",
        "itunes": "n/a",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`Artist <https://musicbrainz.org/doc/Artist>`_",
        "picard_name": "``artist``",
        "id3v2": "``TPE1``",
        "vorbis": "``ARTIST``",
        "apev2": "``Artist``",
        "itunes": "``©ART``",
        "wmp": "``Author``",
        "riff": "``IART``",
    },

    {
        "tag_name": "Artist Sort Order",
        "picard_name": "``artistsort``",
        "id3v2": "``TSOP``",
        "vorbis": "``ARTISTSORT``",
        "apev2": "``ARTISTSORT``",
        "itunes": "``soar``",
        "wmp": "``WM/ArtistSortOrder``",
        "riff": "n/a",
    },

    {
        "tag_name": "Artists",
        "picard_name": "``artists``",
        "id3v2": "``TXXX:Artists``",
        "vorbis": "``ARTISTS``",
        "apev2": "``Artists``",
        "itunes": "``----:com.apple.iTunes:ARTISTS``",
        "wmp": "``WM/ARTISTS``",
        "riff": "n/a",
    },

    {
        "tag_name": "`ASIN <https://musicbrainz.org/doc/ASIN>`_",
        "picard_name": "``asin``",
        "id3v2": "``TXXX:ASIN``",
        "vorbis": "``ASIN``",
        "apev2": "``ASIN``",
        "itunes": "``----:com.apple.iTunes:ASIN``",
        "wmp": "``ASIN``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Barcode <https://musicbrainz.org/doc/Barcode>`_",
        "picard_name": "``barcode``",
        "id3v2": "``TXXX:BARCODE``",
        "vorbis": "``BARCODE``",
        "apev2": "``Barcode``",
        "itunes": "``----:com.apple.iTunes:BARCODE``",
        "wmp": "``WM/Barcode``",
        "riff": "n/a",
    },

    {
        "tag_name": "BPM [4]",
        "picard_name": "``bpm``",
        "id3v2": "``TBPM``",
        "vorbis": "``BPM``",
        "apev2": "``BPM``",
        "itunes": "``tmpo``",
        "wmp": "``WM/BeatsPerMinute``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Catalog Number <https://musicbrainz.org/doc/Release_Catalog_Number>`_",
        "picard_name": "``catalognumber``",
        "id3v2": "``TXXX:CATALOGNUMBER``",
        "vorbis": "``CATALOGNUMBER``",
        "apev2": "``CatalogNumber``",
        "itunes": "``----:com.apple.iTunes:CATALOGNUMBER``",
        "wmp": "``WM/CatalogNo``",
        "riff": "n/a",
    },

    {
        "tag_name": "Comment [4]",
        "picard_name": "``comment:description``",
        "id3v2": "``COMM:description``",
        "vorbis": "``COMMENT``",
        "apev2": "``Comment``",
        "itunes": "``©cmt``",
        "wmp": "``Description``",
        "riff": "``ICMT``",
    },

    {
        "tag_name": "Compilation (iTunes) [5]",
        "picard_name": "``compilation``",
        "id3v2": "``TCMP``",
        "vorbis": "``COMPILATION``",
        "apev2": "``Compilation``",
        "itunes": "``cpil``",
        "wmp": "``WM/IsCompilation``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Composer <https://musicbrainz.org/relationship/d59d99ea-23d4-4a80-b066-edca32ee158f>`_",
        "picard_name": "``composer``",
        "id3v2": "``TCOM``",
        "vorbis": "``COMPOSER``",
        "apev2": "``Composer``",
        "itunes": "``©wrt``",
        "wmp": "``WM/Composer``",
        "riff": "``IMUS``",
    },

    {
        "tag_name": "Composer Sort Order",
        "picard_name": "``composersort``",
        "id3v2": "``TSOC`` (Picard>=1.3)\n``TXXX:COMPOSERSORT`` (Picard<=1.2)",
        "vorbis": "``COMPOSERSORT``",
        "apev2": "``COMPOSERSORT``",
        "itunes": "``soco``",
        "wmp": "``WM/ComposerSortOrder`` (Picard>=1.3)",
        "riff": "n/a",
    },

    {
        "tag_name": "`Conductor <https://musicbrainz.org/relationship/234670ce-5f22-4fd0-921b-ef1662695c5d>`_",
        "picard_name": "``conductor``",
        "id3v2": "``TPE3``",
        "vorbis": "``CONDUCTOR``",
        "apev2": "``Conductor``",
        "itunes": "``----:com.apple.iTunes:CONDUCTOR``",
        "wmp": "``WM/Conductor``",
        "riff": "n/a",
    },

    {
        "tag_name": "Copyright [4]",
        "picard_name": "``copyright``",
        "id3v2": "``TCOP``",
        "vorbis": "``COPYRIGHT``",
        "apev2": "``Copyright``",
        "itunes": "``cprt``",
        "wmp": "``Copyright``",
        "riff": "``ICOP``",
    },

    {
        "tag_name": "Disc Number",
        "picard_name": "``discnumber``",
        "id3v2": "``TPOS``",
        "vorbis": "``DISCNUMBER``",
        "apev2": "``Disc``",
        "itunes": "``disk``",
        "wmp": "``WM/PartOfSet``",
        "riff": "n/a",
    },

    {
        "tag_name": "Disc Subtitle",
        "picard_name": "``discsubtitle``",
        "id3v2": "``TSST`` (ID3v2.4 only)",
        "vorbis": "``DISCSUBTITLE``",
        "apev2": "``DiscSubtitle``",
        "itunes": "``----:com.apple.iTunes:DISCSUBTITLE``",
        "wmp": "``WM/SetSubTitle``",
        "riff": "n/a",
    },

    {
        "tag_name": "Encoded By [4]",
        "picard_name": "``encodedby``",
        "id3v2": "``TENC``",
        "vorbis": "``ENCODEDBY``",
        "apev2": "``EncodedBy``",
        "itunes": "``©too``",
        "wmp": "``WM/EncodedBy``",
        "riff": "``IENC``",
    },

    {
        "tag_name": "Encoder Settings [4]",
        "picard_name": "``encodersettings``",
        "id3v2": "``TSSE``",
        "vorbis": "``ENCODERSETTINGS``",
        "apev2": "``EncoderSettings``",
        "itunes": "n/a",
        "wmp": "``WM/EncodingSettings`` (Picard>=1.3.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "`Engineer <https://musicbrainz.org/relationship/5dcc52af-7064-4051-8d62-7d80f4c3c907>`_",
        "picard_name": "``engineer``",
        "id3v2": "``TIPL:engineer`` (ID3v2.4)\n``IPLS:engineer`` (ID3v2.3)",
        "vorbis": "``ENGINEER``",
        "apev2": "``Engineer``",
        "itunes": "``----:com.apple.iTunes:ENGINEER``",
        "wmp": "``WM/Engineer``",
        "riff": "``IENG``",
    },

    {
        "tag_name": "Gapless Playback [4]",
        "picard_name": "``gapless``",
        "id3v2": "n/a",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "``pgap``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`Genre <https://musicbrainz.org/doc/Genre>`_",
        "picard_name": "``genre``",
        "id3v2": "``TCON``",
        "vorbis": "``GENRE``",
        "apev2": "``Genre``",
        "itunes": "``©gen``",
        "wmp": "``WM/Genre``",
        "riff": "``IGNR``",
    },

    {
        "tag_name": "Grouping [3]",
        "picard_name": "``grouping``",
        "id3v2": "``TIT1``\n``GRP1`` [8]",
        "vorbis": "``GROUPING``",
        "apev2": "``Grouping``",
        "itunes": "``©grp``",
        "wmp": "``WM/ContentGroupDescription``",
        "riff": "n/a",
    },

    {
        "tag_name": "Initial Key",
        "picard_name": "``key`` (Picard>=1.4)",
        "id3v2": "``TKEY``",
        "vorbis": "``KEY``",
        "apev2": "``KEY``",
        "itunes": "``----:com.apple.iTunes:initialkey``",
        "wmp": "``WM/InitialKey``",
        "riff": "n/a",
    },

    {
        "tag_name": "`ISRC <https://musicbrainz.org/doc/ISRC>`_",
        "picard_name": "``isrc``",
        "id3v2": "``TSRC``",
        "vorbis": "``ISRC``",
        "apev2": "``ISRC``",
        "itunes": "``----:com.apple.iTunes:ISRC``",
        "wmp": "``WM/ISRC``",
        "riff": "n/a",
    },

    {
        "tag_name": "Language",
        "picard_name": "``language``",
        "id3v2": "``TLAN``",
        "vorbis": "``LANGUAGE``",
        "apev2": "``Language``",
        "itunes": "``----:com.apple.iTunes:LANGUAGE``",
        "wmp": "``WM/Language``",
        "riff": "``ILNG``",
    },

    {
        "tag_name": "License [6] [7]",
        "picard_name": "``license``",
        "id3v2": "``WCOP`` (single URL)\n``TXXX:LICENSE`` (multiple or non-URL)",
        "vorbis": "``LICENSE``",
        "apev2": "``LICENSE``",
        "itunes": "``----:com.apple.iTunes:LICENSE``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`Lyricist <https://musicbrainz.org/relationship/3e48faba-ec01-47fd-8e89-30e81161661c>`_",
        "picard_name": "``lyricist``",
        "id3v2": "``TEXT``",
        "vorbis": "``LYRICIST``",
        "apev2": "``Lyricist``",
        "itunes": "``----:com.apple.iTunes:LYRICIST``",
        "wmp": "``WM/Writer``",
        "riff": "n/a",
    },

    {
        "tag_name": "Lyrics [4]",
        "picard_name": "``lyrics:description``",
        "id3v2": "``USLT:description``",
        "vorbis": "``LYRICS``",
        "apev2": "``Lyrics``",
        "itunes": "``©lyr``",
        "wmp": "``WM/Lyrics``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Media <https://musicbrainz.org/doc/Release_Format>`_",
        "picard_name": "``media``",
        "id3v2": "``TMED``",
        "vorbis": "``MEDIA``",
        "apev2": "``Media``",
        "itunes": "``----:com.apple.iTunes:MEDIA``",
        "wmp": "``WM/Media``",
        "riff": "``IMED``",
    },

    {
        "tag_name": "`Mix-DJ <https://musicbrainz.org/relationship/28338ee6-d578-485a-bb53-61dbfd7c6545>`_",
        "picard_name": "``djmixer``",
        "id3v2": "``TIPL:DJ-mix`` (ID3v2.4)\n``IPLS:DJ-mix`` (ID3v2.3)",
        "vorbis": "``DJMIXER``",
        "apev2": "``DJMixer``",
        "itunes": "``----:com.apple.iTunes:DJMIXER``",
        "wmp": "``WM/DJMixer``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Mixer <https://musicbrainz.org/relationship/3e3102e1-1896-4f50-b5b2-dd9824e46efe>`_",
        "picard_name": "``mixer``",
        "id3v2": "``TIPL:mix`` (ID3v2.4)\n``IPLS:mix`` (ID3v2.3)",
        "vorbis": "``MIXER``",
        "apev2": "``Mixer``",
        "itunes": "``----:com.apple.iTunes:MIXER``",
        "wmp": "``WM/Mixer``",
        "riff": "n/a",
    },

    {
        "tag_name": "Mood [3]",
        "picard_name": "``mood``",
        "id3v2": "``TMOO`` (ID3v2.4 only)",
        "vorbis": "``MOOD``",
        "apev2": "``Mood``",
        "itunes": "``----:com.apple.iTunes:MOOD``",
        "wmp": "``WM/Mood``",
        "riff": "n/a",
    },

    {
        "tag_name": "Movement [4]",
        "picard_name": "``movement`` (Picard>=2.1)",
        "id3v2": "``MVNM``",
        "vorbis": "``MOVEMENTNAME``",
        "apev2": "``MOVEMENTNAME``",
        "itunes": "``©mvn``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Movement Count [4]",
        "picard_name": "``movementtotal`` (Picard>=2.1)",
        "id3v2": "``MVIN``",
        "vorbis": "``MOVEMENTTOTAL``",
        "apev2": "``MOVEMENTTOTAL``",
        "itunes": "``mvc``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Movement Number [4]",
        "picard_name": "``movementnumber`` (Picard>=2.1)",
        "id3v2": "``MVIN``",
        "vorbis": "``MOVEMENT``",
        "apev2": "``MOVEMENT``",
        "itunes": "``mvi``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Artist ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_artistid``",
        "id3v2": "``TXXX:MusicBrainz Artist Id``",
        "vorbis": "``MUSICBRAINZ_ARTISTID``",
        "apev2": "``MUSICBRAINZ_ARTISTID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Artist Id``",
        "wmp": "``MusicBrainz/Artist Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Disc ID <https://musicbrainz.org/doc/Disc_ID>`_",
        "picard_name": "``musicbrainz_discid``",
        "id3v2": "``TXXX:MusicBrainz Disc Id``",
        "vorbis": "``MUSICBRAINZ_DISCID``",
        "apev2": "``MUSICBRAINZ_DISCID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Disc Id``",
        "wmp": "``MusicBrainz/Disc Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Original Artist ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_originalartistid``",
        "id3v2": "``TXXX:MusicBrainz Original Artist Id``",
        "vorbis": "``MUSICBRAINZ_ORIGINALARTISTID``",
        "apev2": "n/a",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Original Artist Id`` (Picard>=2.1)",
        "wmp": "``MusicBrainz/Original Artist Id`` (Picard>=2.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Original Release ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_originalalbumid``",
        "id3v2": "``TXXX:MusicBrainz Original Album Id``",
        "vorbis": "``MUSICBRAINZ_ORIGINALALBUMID``",
        "apev2": "n/a",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Original Album Id`` (Picard>=2.1)",
        "wmp": "``MusicBrainz/Original Album Id`` (Picard>=2.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Recording ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_recordingid``",
        "id3v2": "``UFID:http://musicbrainz.org``",
        "vorbis": "``MUSICBRAINZ_TRACKID``",
        "apev2": "``MUSICBRAINZ_TRACKID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Track Id``",
        "wmp": "``MusicBrainz/Track Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Release Artist ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_albumartistid``",
        "id3v2": "``TXXX:MusicBrainz Album Artist Id``",
        "vorbis": "``MUSICBRAINZ_ALBUMARTISTID``",
        "apev2": "``MUSICBRAINZ_ALBUMARTISTID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Album Artist Id``",
        "wmp": "``MusicBrainz/Album Artist Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "MusicBrainz Release Group ID",
        "picard_name": "``musicbrainz_releasegroupid``",
        "id3v2": "``TXXX:MusicBrainz Release Group Id``",
        "vorbis": "``MUSICBRAINZ_RELEASEGROUPID``",
        "apev2": "``MUSICBRAINZ_RELEASEGROUPID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Release Group Id``",
        "wmp": "``MusicBrainz/Release Group Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Release ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_albumid``",
        "id3v2": "``TXXX:MusicBrainz Album Id``",
        "vorbis": "``MUSICBRAINZ_ALBUMID``",
        "apev2": "``MUSICBRAINZ_ALBUMID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Album Id``",
        "wmp": "``MusicBrainz/Album Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz Track ID <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_",
        "picard_name": "``musicbrainz_trackid``",
        "id3v2": "``TXXX:MusicBrainz Release Track Id``",
        "vorbis": "``MUSICBRAINZ_RELEASETRACKID``",
        "apev2": "``MUSICBRAINZ_RELEASETRACKID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Release Track Id``",
        "wmp": "``MusicBrainz/Release Track Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicBrainz TRM ID <https://musicbrainz.org/doc/TRM>`_",
        "picard_name": "``musicbrainz_trmid`` (deprecated)",
        "id3v2": "``TXXX:MusicBrainz TRM Id``",
        "vorbis": "``MUSICBRAINZ_TRMID``",
        "apev2": "``MUSICBRAINZ_TRMID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz TRM Id``",
        "wmp": "``MusicBrainz/TRM Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "MusicBrainz Work ID",
        "picard_name": "``musicbrainz_workid``",
        "id3v2": "``TXXX:MusicBrainz Work Id``",
        "vorbis": "``MUSICBRAINZ_WORKID``",
        "apev2": "``MUSICBRAINZ_WORKID``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Work Id``",
        "wmp": "``MusicBrainz/Work Id``",
        "riff": "n/a",
    },

    {
        "tag_name": "MusicIP Fingerprint",
        "picard_name": "``musicip_fingerprint``",
        "id3v2": "``TXXX:MusicMagic Fingerprint``",
        "vorbis": "``FINGERPRINT=MusicMagic Fingerprint {fingerprint}``",
        "apev2": "n/a",
        "itunes": "``----:com.apple.iTunes:fingerprint``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`MusicIP PUID <https://musicbrainz.org/doc/PUID>`_",
        "picard_name": "``musicip_puid``",
        "id3v2": "``TXXX:MusicIP PUID``",
        "vorbis": "``MUSICIP_PUID``",
        "apev2": "``MUSICIP_PUID``",
        "itunes": "``----:com.apple.iTunes:MusicIP PUID``",
        "wmp": "``MusicIP/PUID``",
        "riff": "n/a",
    },

    {
        "tag_name": "Original Album",
        "picard_name": "``originalalbum``",
        "id3v2": "``TOAL``",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "n/a",
        "wmp": "``WM/OriginalAlbumTitle`` (Picard>=2.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "Original Artist",
        "picard_name": "``originalartist``",
        "id3v2": "``TOPE``",
        "vorbis": "n/a",
        "apev2": "``Original Artist`` (Picard>=2.1)",
        "itunes": "n/a",
        "wmp": "``WM/OriginalArtist`` (Picard>=2.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "Original Filename",
        "picard_name": "``originalfilename`` (Picard>=2.3)",
        "id3v2": "``TOFN``",
        "vorbis": "``ORIGINALFILENAME``",
        "apev2": "``ORIGINALFILENAME``",
        "itunes": "n/a",
        "wmp": "``WM/OriginalFilename``",
        "riff": "n/a",
    },

    {
        "tag_name": "Original Release Date [1]",
        "picard_name": "``originaldate``",
        "id3v2": "``TDOR`` (ID3v2.4)\n``TORY`` (ID3v2.3)",
        "vorbis": "``ORIGINALDATE``",
        "apev2": "n/a",
        "itunes": "n/a",
        "wmp": "``WM/OriginalReleaseTime`` (Picard>=1.3.1)\n``WM/OriginalReleaseYear`` (Picard<=1.3.0)",
        "riff": "n/a",
    },

    {
        "tag_name": "Original Release Year [1]",
        "picard_name": "``originalyear``",
        "id3v2": "n/a",
        "vorbis": "``ORIGINALYEAR``",
        "apev2": "``ORIGINALYEAR``",
        "itunes": "n/a",
        "wmp": "``WM/OriginalReleaseYear`` (Picard>=1.3.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "Performer",
        "picard_name": "``performer:instrument``",
        "id3v2": "``TMCL:instrument`` (ID3v2.4)\n``IPLS:instrument`` (ID3v2.3)",
        "vorbis": "``PERFORMER={artist} (instrument)``",
        "apev2": "``Performer={artist} (instrument)``",
        "itunes": "n/a",
        "wmp": "n/a",
        "riff": "n/a",
        "seealso": "Please refer to\n"
                   "`Relationship Types / Artist-Release / Performer <https://musicbrainz.org/relationship/888a2320-52e4-4fe8-a8a0-7a4c8dfde167>`_ ,\n"
                   "`Relationship Types / Artist-Release / Vocal <https://musicbrainz.org/relationship/eb10f8a0-0f4c-4dce-aa47-87bcb2bc42f3>`_ ,\n"
                   "`Relationship Types / Artist-Release / Instrument <https://musicbrainz.org/relationship/67555849-61e5-455b-96e3-29733f0115f5>`_ ,\n"
                   "`Relationship Types / Artist-Recording / Performer <https://musicbrainz.org/relationship/628a9658-f54c-4142-b0c0-95f031b544da>`_ ,\n"
                   "`Relationship Types / Artist-Recording / Vocal <https://musicbrainz.org/relationship/0fdbe3c6-7700-4a31-ae54-b53f06ae1cfa>`_ , and\n"
                   "`Relationship Types / Artist-Recording / Instrument <https://musicbrainz.org/relationship/59054b12-01ac-43ee-a618-285fd397e461>`_\n"
                   "for more information.",
    },

    {
        "tag_name": "Podcast [4]",
        "picard_name": "``podcast``",
        "id3v2": "n/a",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "``pcst``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Podcast URL [4]",
        "picard_name": "``podcasturl``",
        "id3v2": "n/a",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "``purl``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "`Producer <https://musicbrainz.org/relationship/5c0ceac3-feb4-41f0-868d-dc06f6e27fc0>`_",
        "picard_name": "``producer``",
        "id3v2": "``TIPL:producer`` (ID3v2.4)\n``IPLS:producer`` (ID3v2.3)",
        "vorbis": "``PRODUCER``",
        "apev2": "``Producer``",
        "itunes": "``----:com.apple.iTunes:PRODUCER``",
        "wmp": "``WM/Producer``",
        "riff": "``IPRO``",
    },

    {
        "tag_name": "`Rating <https://musicbrainz.org/doc/Rating_System>`_",
        "picard_name": "``_rating``",
        "id3v2": "``POPM``",
        "vorbis": "``RATING:user@email``",
        "apev2": "n/a",
        "itunes": "n/a",
        "wmp": "``WM/SharedUserRating``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Record Label <https://musicbrainz.org/doc/Label_Name>`_",
        "picard_name": "``label``",
        "id3v2": "``TPUB``",
        "vorbis": "``LABEL``",
        "apev2": "``Label``",
        "itunes": "``----:com.apple.iTunes:LABEL``",
        "wmp": "``WM/Publisher``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Release Country <https://musicbrainz.org/doc/Release_Country>`_",
        "picard_name": "``releasecountry``",
        "id3v2": "``TXXX:MusicBrainz Album Release Country``",
        "vorbis": "``RELEASECOUNTRY``",
        "apev2": "``RELEASECOUNTRY``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Album Release Country``",
        "wmp": "``MusicBrainz/Album Release Country``",
        "riff": "``ICNT``",
    },

    {
        "tag_name": "`Release Date <https://musicbrainz.org/doc/Release_Date>`_",
        "picard_name": "``date``",
        "id3v2": "``TDRC`` (ID3v2.4)\n``TYER`` + ``TDAT`` (ID3v2.3)",
        "vorbis": "``DATE``",
        "apev2": "``Year``",
        "itunes": "``©day``",
        "wmp": "``WM/Year``",
        "riff": "``ICRD``",
    },

    {
        "tag_name": "`Release Status <https://musicbrainz.org/doc/Release_Status>`_",
        "picard_name": "``releasestatus``",
        "id3v2": "``TXXX:MusicBrainz Album Status``",
        "vorbis": "``RELEASESTATUS``",
        "apev2": "``MUSICBRAINZ_ALBUMSTATUS``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Album Status``",
        "wmp": "``MusicBrainz/Album Status``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Release Type <https://musicbrainz.org/doc/Release_Type>`_",
        "picard_name": "``releasetype``",
        "id3v2": "``TXXX:MusicBrainz Album Type``",
        "vorbis": "``RELEASETYPE``",
        "apev2": "``MUSICBRAINZ_ALBUMTYPE``",
        "itunes": "``----:com.apple.iTunes:MusicBrainz Album Type``",
        "wmp": "``MusicBrainz/Album Type``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Remixer <https://musicbrainz.org/relationship/7950be4d-13a3-48e7-906b-5af562e39544>`_",
        "picard_name": "``remixer``",
        "id3v2": "``TPE4``",
        "vorbis": "``REMIXER``",
        "apev2": "``MixArtist``",
        "itunes": "``----:com.apple.iTunes:REMIXER``",
        "wmp": "``WM/ModifiedBy``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Album Gain",
        "picard_name": "``replaygain_album_gain`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_ALBUM_GAIN``",
        "vorbis": "``REPLAYGAIN_ALBUM_GAIN``",
        "apev2": "``REPLAYGAIN_ALBUM_GAIN``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_GAIN``",
        "wmp": "``REPLAYGAIN_ALBUM_GAIN``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Album Peak",
        "picard_name": "``replaygain_album_peak`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_ALBUM_PEAK``",
        "vorbis": "``REPLAYGAIN_ALBUM_PEAK``",
        "apev2": "``REPLAYGAIN_ALBUM_PEAK``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_PEAK``",
        "wmp": "``REPLAYGAIN_ALBUM_PEAK``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Album Range",
        "picard_name": "``replaygain_album_range`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_ALBUM_RANGE``",
        "vorbis": "``REPLAYGAIN_ALBUM_RANGE``",
        "apev2": "``REPLAYGAIN_ALBUM_RANGE``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_ALBUM_RANGE``",
        "wmp": "``REPLAYGAIN_ALBUM_RANGE``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Reference Loudness",
        "picard_name": "``replaygain_reference_loudness`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_REFERENCE_LOUDNESS``",
        "vorbis": "``REPLAYGAIN_REFERENCE_LOUDNESS``",
        "apev2": "``REPLAYGAIN_REFERENCE_LOUDNESS``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_REFERENCE_LOUDNESS``",
        "wmp": "``REPLAYGAIN_REFERENCE_LOUDNESS``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Track Gain",
        "picard_name": "``replaygain_track_gain`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_TRACK_GAIN``",
        "vorbis": "``REPLAYGAIN_TRACK_GAIN``",
        "apev2": "``REPLAYGAIN_TRACK_GAIN``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_TRACK_GAIN``",
        "wmp": "``REPLAYGAIN_TRACK_GAIN``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Track Peak",
        "picard_name": "``replaygain_track_peak`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_TRACK_PEAK``",
        "vorbis": "``REPLAYGAIN_TRACK_PEAK``",
        "apev2": "``REPLAYGAIN_TRACK_PEAK``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_TRACK_PEAK``",
        "wmp": "``REPLAYGAIN_TRACK_PEAK``",
        "riff": "n/a",
    },

    {
        "tag_name": "ReplayGain Track Range",
        "picard_name": "``replaygain_track_range`` (Picard>=2.2)",
        "id3v2": "``TXXX:REPLAYGAIN_TRACK_RANGE``",
        "vorbis": "``REPLAYGAIN_TRACK_RANGE``",
        "apev2": "``REPLAYGAIN_TRACK_RANGE``",
        "itunes": "``----:com.apple.iTunes:REPLAYGAIN_TRACK_RANGE``",
        "wmp": "``REPLAYGAIN_TRACK_RANGE``",
        "riff": "n/a",
    },

    {
        "tag_name": "Script",
        "picard_name": "``script``",
        "id3v2": "``TXXX:SCRIPT``",
        "vorbis": "``SCRIPT``",
        "apev2": "``Script``",
        "itunes": "``----:com.apple.iTunes:SCRIPT``",
        "wmp": "``WM/Script``",
        "riff": "n/a",
    },

    {
        "tag_name": "Show Name [4]",
        "picard_name": "``show``",
        "id3v2": "n/a",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "``tvsh``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Show Name Sort Order [4]",
        "picard_name": "``showsort``",
        "id3v2": "n/a",
        "vorbis": "n/a",
        "apev2": "n/a",
        "itunes": "``sosn``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Show Work & Movement [4]",
        "picard_name": "``showmovement`` (Picard>=2.1)",
        "id3v2": "``TXXX:SHOWMOVEMENT``",
        "vorbis": "``SHOWMOVEMENT``",
        "apev2": "``SHOWMOVEMENT``",
        "itunes": "``shwm``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Subtitle [4]",
        "picard_name": "``subtitle``",
        "id3v2": "``TIT3``",
        "vorbis": "``SUBTITLE``",
        "apev2": "``Subtitle``",
        "itunes": "``----:com.apple.iTunes:SUBTITLE``",
        "wmp": "``WM/SubTitle``",
        "riff": "n/a",
    },

    {
        "tag_name": "Total Discs",
        "picard_name": "``totaldiscs``",
        "id3v2": "``TPOS``",
        "vorbis": "``DISCTOTAL and TOTALDISCS``",
        "apev2": "``Disc``",
        "itunes": "``disk``",
        "wmp": "``WM/PartOfSet`` (Picard>=1.3.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "Total Tracks",
        "picard_name": "``totaltracks``",
        "id3v2": "``TRCK``",
        "vorbis": "``TRACKTOTAL`` and ``TOTALTRACKS``",
        "apev2": "``Track``",
        "itunes": "``trkn``",
        "wmp": "n/a",
        "riff": "n/a",
    },

    {
        "tag_name": "Track Number",
        "picard_name": "``tracknumber``",
        "id3v2": "``TRCK``",
        "vorbis": "``TRACKNUMBER``",
        "apev2": "``Track``",
        "itunes": "``trkn``",
        "wmp": "``WM/TrackNumber``",
        "riff": "``ITRK``",
    },

    {
        "tag_name": "`Track Title <https://musicbrainz.org/doc/Track_Title>`_",
        "picard_name": "``title``",
        "id3v2": "``TIT2``",
        "vorbis": "``TITLE``",
        "apev2": "``Title``",
        "itunes": "``©nam``",
        "wmp": "``Title``",
        "riff": "``INAM``",
    },

    {
        "tag_name": "Track Title Sort Order [4]",
        "picard_name": "``titlesort``",
        "id3v2": "``TSOT``",
        "vorbis": "``TITLESORT``",
        "apev2": "``TITLESORT``",
        "itunes": "``sonm``",
        "wmp": "``WM/TitleSortOrder``",
        "riff": "n/a",
    },

    {
        "tag_name": "Website (official artist website)",
        "picard_name": "``website``",
        "id3v2": "``WOAR``",
        "vorbis": "``WEBSITE``",
        "apev2": "``Weblink``",
        "itunes": "n/a",
        "wmp": "``WM/AuthorURL`` (Picard>=1.3.1)",
        "riff": "n/a",
    },

    {
        "tag_name": "Work Title",
        "picard_name": "``work`` (Picard>=1.3)",
        "id3v2": "``TXXX:WORK`` ``TIT1`` [8]",
        "vorbis": "``WORK``",
        "apev2": "``WORK``",
        "itunes": "``©wrk`` (Picard>=2.1)",
        "wmp": "``WM/Work``",
        "riff": "n/a",
    },

    {
        "tag_name": "`Writer <https://musicbrainz.org/relationship/a255bca1-b157-4518-9108-7b147dc3fc68>`_ [2]",
        "picard_name": "``writer``",
        "id3v2": "``TXXX:Writer`` (Picard>=1.3)",
        "vorbis": "``WRITER``",
        "apev2": "``Writer``",
        "itunes": "n/a",
        "wmp": "n/a",
        "riff": "``IWRI``",
    },
]


def rc2cell(row, col):
    """Convert zero-based row and column to Excel cell identifier.

    Args:
        row (int): Row number (zero-based)
        col (int): Column number (zero-based)

    Returns:
        str: Excel cell identification string.
    """
    if col <= 0:
        cell_col = 'A'
    else:
        cell_col = ''
        col += 1
        while col > 0:
            col, temp = divmod(col, 26)
            if temp < 1:
                temp = 26
                col -= 1
            cell_col += chr(64 + temp)
        cell_col = cell_col[::-1]
    cell_row = int(max(row, 0)) + 1
    return '{0}{1}'.format(cell_col, cell_row)


def write_spreadsheet(filename):    # pylint: disable=too-many-locals
    """Output the tag mapping information in the form of an Excel spreadsheet (*.xlsx) file.

    Args:
        filename (str): the path and filename of the output file to use.  Overwrites if existing.
    """
    RE_STRIP_URL = re.compile(r'`(.*)\s+<[^`]*`_')

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Define formatting settings
    title_format = workbook.add_format({'bold': True, 'font_size': 30})
    tag_header_format = workbook.add_format({'bold': True, 'align': 'left', 'bg_color': '#e6e6e6', 'top': 6, 'bottom': 6, 'right': 1})
    tag_name_format = workbook.add_format({'bold': True, 'align': 'left', 'valign': 'top', 'bg_color': '#e6e6e6', 'bottom': 1})
    tag_info_format = workbook.add_format({'align': 'left', 'valign': 'top', 'text_wrap': True})
    notes_title_format = workbook.add_format({'bold': True, 'align': 'left', 'font_size': 18})
    # notes_number_format = workbook.add_format({'align': 'right', 'valign': 'top'})
    # notes_text_format = workbook.add_format({'align': 'left', 'valign': 'top'})

    # Write the title
    worksheet.write('A1', 'MusicBrainz Picard Tag Mapping', title_format)

    row = 2

    # Write the table headers
    for col, (name, val, pts, px) in enumerate(COLUMNS):    # pylint: disable=unused-variable
        worksheet.write(row, col, val, tag_header_format)
        worksheet.set_column(col, col, pts)

    # Write the tag values
    for tag in TAG_MAP:
        row += 1
        for col, (name, val, pts, px) in enumerate(COLUMNS):
            text = str(tag[name]).replace('``', '')
            text = re.sub(RE_STRIP_URL, r'\1', text)
            if col:
                worksheet.write(row, col, text, tag_info_format)
            else:
                worksheet.write(row, col, text, tag_name_format)

    # Freeze the table headers and first column
    worksheet.freeze_panes(3, 1, 3, 1)

    # Write the notes section
    row += 2
    worksheet.write(row, 1, 'Notes:', notes_title_format)
    for num in NOTES_NUMBERS:
        row += 1
        text = str(NOTES[num]).replace('``', '')
        text = re.sub(RE_STRIP_URL, r'\1', text)
        worksheet.write(row, 1, '{0}.  {1}'.format(num, text,))

    workbook.close()


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <title>MusicBrainz Picard Tag Mapping</title>
  <meta charset="utf-8">
  <meta name="keywords" content="MusicBrainz, Picard, Tags, Tag Map">
  <meta name="description" content="Mapping of the metadata tags used with MusicBrainz Picard.">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {
      background-color: white;
      color: black;
      font-family: arial;
      font-size: 11pt
    }
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    th, td {
      padding: 5px;
      margin: 0;
      text-align: left;
    }
    th, .column1 {
      font-weight: bold;
      background-color: #e6e6e6;
    }
    code {
      background-color: lightgray;
    }
  </style>

  <link rel="shortcut icon" href="https://picard-docs.musicbrainz.org/en/_static/picard-icon.png"/>
</head>
<body>
  <h1>MusicBrainz Picard Tag Mapping</h1>
{{table_info}}
</body>
</html>
"""


def write_html(filename):
    """Output the tag mapping information in the form of a stand-alone HTML file.

    Args:
        filename (str): the path and filename of the output file to use.  Overwrites if existing.
    """
    RE_MAKE_FOOTNOTE = re.compile(r'(\[([0-9]+)\])')
    RE_MAKE_CODE = re.compile(r'``([^`]*)``')
    RE_MAKE_ANCHOR = re.compile(r'`(.*)\s+<([^>]*)>`_')
    width = 0
    for (name, val, pts, px) in COLUMNS:    # pylint: disable=unused-variable
        width += px + 15
    html = '<table width="{0}">\n<tr>\n'.format(width,)

    # Write the table headers
    for (name, val, pts, px) in COLUMNS:
        text = str(val).replace('\n', '<br />')
        text = re.sub(RE_MAKE_FOOTNOTE, r'<sup><a href="#fn\2">\1</a></sup>', text)
        text = re.sub(RE_MAKE_CODE, r'<code>\1</code>', text)
        text = re.sub(RE_MAKE_ANCHOR, r'<a href="\2">\1</a>', text)
        html += '  <th style="width: {0}px">{1}</th>\n'.format(px, text)
    html += '</tr>\n'

    # Write the tag values
    for tag in TAG_MAP:
        html += '<tr>\n'
        for col, (name, val, pts, px) in enumerate(COLUMNS):
            text = str(tag[name]).replace('\n', '<br />')
            text = re.sub(RE_MAKE_FOOTNOTE, r'<sup><a href="#fn\2">\1</a></sup>', text)
            text = re.sub(RE_MAKE_CODE, r'<code>\1</code>', text)
            text = re.sub(RE_MAKE_ANCHOR, r'<a href="\2">\1</a>', text)
            if col:
                html += '  <td>{0}</td>\n'.format(text,)
            else:
                html += '  <td class="column1">{0}</td>\n'.format(text,)
        html += '</tr>\n'
    html += '</table>\n\n'

    # Write the notes section
    html += '<h2>Notes:</h2>\n<ol>\n'
    for num in NOTES_NUMBERS:
        text = str(NOTES[num]).replace('\n', '<br />')
        text = re.sub(RE_MAKE_CODE, r'<code>\1</code>', text)
        text = re.sub(RE_MAKE_ANCHOR, r'<a href="\2">\1</a>', text)
        html += '  <li style="width: 1200px;" id="fn{0}">{1}</li>\n'.format(num, text)
    html += '</ol>\n'

    # Write the output file
    with open(filename, 'w', encoding='utf8') as ofile:
        ofile.write(HTML_TEMPLATE.replace(r'{{table_info}}', html))


def write_rst(filename, pdf=False):
    """Output the tag mapping information in the form of a restructured text (*.rst) file.

    Args:
        filename (str): the path and filename of the output file to use.  Overwrites if existing.
        pdf (bool, optional): Format file suitable for use in building a PDF document. Defaults to False.
    """
    RE_MAKE_FOOTNOTE = re.compile(r'(\[([0-9]+)\])')
    rst = '.. MusicBrainz Picard Documentation Project\n\n'
    rst += '.. Picard Tag Mapping\n\n.. This file is automatically generated. Any changes entered manually will be overwritten.\n\n'
    # rst += ':orphan:\n\n'   # Only required if generating separate files for HTML and PDF output.
    temp = 'Appendix B: :index:`Tag Mapping <pair: mapping; tags>`'
    rst += temp + '\n' + '=' * len(temp) + '\n\n'
    rst += 'The following is a mapping between Picard internal tag names and those used by various tagging formats.\n'
    rst += 'The mapping is also available as a `table <https://picard-docs.musicbrainz.org/downloads/MusicBrainz_Picard_Tag_Map.html>`_'
    rst += ' and a `spreadsheet <https://picard-docs.musicbrainz.org/downloads/MusicBrainz_Picard_Tag_Map.xlsx>`_.\n'
    rst += '\n'

    # Write the tag values
    for tag in TAG_MAP:
        temp = str(tag['tag_name']).replace('\n', ' ')
        temp = re.sub(RE_MAKE_FOOTNOTE, r' :sup:`\1` ', temp)
        temp = re.sub(r'\s+', ' ', temp)
        temp = temp.replace(']` :sup:`[', ', ')
        temp = temp.strip()
        temp += '\n'
        rst += temp + '-' * len(temp) + '\n.. csv-table::\n   :width: 100%\n   :widths: 37 100\n\n'
        for col, (name, val, pts, px) in enumerate(COLUMNS):    # pylint: disable=unused-variable
            if col:
                temp = '"' + str(val).replace('\n', ' ') + '", "' + str(tag[name]).replace('\n', ' ') + '"'
                temp = re.sub(RE_MAKE_FOOTNOTE, r' :sup:`\1` ', temp)
                temp = re.sub(r'\s+', ' ', temp)
                rst += '   ' + temp.strip() + '\n'
        if 'seealso' in tag and tag['seealso']:
            rst += '\n.. seealso::\n\n'
            for temp in str(tag['seealso']).split('\n'):
                rst += '   ' + temp.strip() + '\n'
        rst += '\n\n'

    # Write the notes
    rst += '.. rubric:: Notes:\n\n'
    for num in NOTES_NUMBERS:
        temp = '#.'
        rst += temp + ' ' + str(NOTES[num]).replace('\n', ' ').strip() + '\n'
    if pdf:
        rst += '\n.. raw:: latex\n\n   \\clearpage\n'

    # Write the output file
    with open(filename, 'w', encoding='utf8') as ofile:
        ofile.write(rst)


def main():
    """Main part of script to execute.
    """
    sys.exit()


##############################################################################


if __name__ == '__main__':
    main()

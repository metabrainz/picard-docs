# -*- coding: utf-8 -*-
"""\
Module to maintain tag mapping information to automatically generate the
tag mapping pages, HTML table and Excel spreadsheet.
"""
# Copyright (C) 2020-2026 Bob Swift
# Copyright (C) 2021, 2026 Philipp Wolfer
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# Tag Reference Table by outsidecontext:
# https://docs.google.com/spreadsheets/d/1afugW3R1FRDN-mwt5SQLY4R7aLAu3RqzjN3pR1497Ok/edit#gid=0

#########################################################################################################
#                                                                                                       #
#   This file contains all of the tag mapping information and notes used to prepare the tag mapping     #
#   spreadsheet, HTML file and reStructuredText files for the Picard Documentation website.  Tag        #
#   mapping information is stored in the constant `TAG_MAP`, which is a list of all of the tags.        #
#   Notes regarding the mapping are stored in the constant `NOTES` which is a dictionary with the       #
#   keys being the numbers of the notes.  The notes can be attached to either a tag or a mapped tag     #
#   by including the number of the note in the `notes` parameter.  If multiple notes are to be          #
#   attched, the parameter is entered as a list of the applicable note numbers.                         #
#                                                                                                       #
#   Each tag handled by Picard is stored in the list as a `TagMap` item.  The elements for the items    #
#   are:                                                                                                #
#                                                                                                       #
#       - tag_name: the name / title of the tag (required)                                              #
#       - picard: the "Picard" tag information (required)                                               #
#       - id3v2: the "ID3v2" tag information (optional)                                                 #
#       - vorbis: the "Vorbis" tag information (optional)                                               #
#       - apev2: the "APEv2" tag information (optional)                                                 #
#       - itunes: the "iTunes MP4" tag information (optional)                                           #
#       - wmp: the "ASF/Windows Media" tag information (optional)                                       #
#       - riff: the "RIFF INFO" tag information (optional)                                              #
#       - notes: standard notes associated with the tag (optional)                                      #
#       - link: link associated with the tag (optional)                                                 #
#       - seealso: additional information to be shown in a "See Also" block in RST files. (optional)    #
#                                                                                                       #
#   The optional 'id3v2', 'vorbis', 'apev2', 'itunes', 'wmp' and 'riff' mapped tag information items    #
#   are entered as a `TagMapInfo` item, or a list of `TagMapInfo` items if required.  The elements      #
#   for the items are:                                                                                  #
#                                                                                                       #
#       - id: the identifier used for the tag (required)                                                #
#       - desc: disambiguation comment (optional)                                                       #
#       - notes: standard notes associated with the tag mapping (optional)                              #
#                                                                                                       #
#   When entering or updating the items in the `TAG_MAP` list, you only need to include the elements    #
#   that apply to the tag.  For example, if there is no associated "RIFF INFO" tag mapping and no       #
#   notes then the'riff' and 'notes' elements can be safely omitted.                                    #
#                                                                                                       #
#   Each item in the `NOTES` dictionary can contain reStructuredText links and newlines if necessary.   #
#   Generally, newlines are not required because the string will be wrapped as required automatically.  #
#                                                                                                       #
#   When entering new items into the `TAG_MAP` list, please enter them in alphabetical order by         #
#   'tag_name' to maintain an orderly list for ease of locating items for future maintenance.           #
#                                                                                                       #
#########################################################################################################

# pylint: disable=too-many-lines

from dataclasses import (
    dataclass,
    field,
)


############################################
#   Column headings to use for the table   #
############################################

# Each tuple comprises the following:
#  - the key used to get the corresponding value for each tag from the tag's dictionary.
#  - the name to print in the table header
#  - the width to set for the column in the spreadsheet
#  - The width to set the column in the HTML table (in pixels)

TAG_COLUMNS = [
    ("tag_name", "Tag Name", 30, 250),
    ("picard", "Internal Name", 50, 350),
    ("id3v2", "ID3v2", 50, 450),
    ("vorbis", "Vorbis", 50, 350),
    ("apev2", "APEv2", 30, 250),
    ("itunes", "iTunes MP4", 60, 550),
    ("wmp", "ASF/Windows Media", 60, 500),
    ("riff", "RIFF INFO", 20, 150),
]

##################################################
#   Notes to display below the tag information   #
##################################################

# Can contain reStructuredText links and newlines if necessary.  Generally, newlines
# are not required because the string will be wrapped as required automatically.

TAG_NOTES = {
    1: "Taken from the earliest release in the release group.",
    2: "Used when uncertain whether composer or lyricist.",
    3: "This is populated by LastFMPlus plugin and not by stock Picard.",
    4: "This is not able to be populated by stock Picard. It may be used and populated by certain plugins.",
    5: (
        "For Picard>=1.3 this indicates a Various Artists album; for Picard<=1.2 this indicates albums with tracks by different "
        "artists which is incorrect (e.g.: an original album with a duet with a feat. artist would show as a Compilation). "
        "In neither case does this indicate a MusicBrainz Release Group subtype of compilation."
    ),
    6: "`Release-level license <https://musicbrainz.org/relationship/004bd0c3-8a45-4309-ba52-fa99f3aa3d50>`_ relationship type.",
    7: "`Recording-level license <https://musicbrainz.org/relationship/f25e301d-b87b-4561-86a0-5d2df6d26c0a>`_ relationship type.",
    8: 'With "Save iTunes compatible grouping and work" (since Picard>=2.1.0)',
    9: "From iTunes Metadata Format Specification",
}


##############################################################
#   Data class definitions for the tag mapping information   #
##############################################################

@dataclass
class TagMapInfo:
    """Information specific to a mapped tag."""
    id: str
    """Tag identifier"""
    desc: str = ''
    """Disambiguation comment"""
    notes: int | list[int] | None = field(default=None)
    """Standard notes associated with the tag mapping"""


@dataclass
class TagMap:   # pylint: disable=too-many-instance-attributes
    """Tag mapping information to other formats."""
    tag_name: str
    """Name of the tag"""
    picard: TagMapInfo
    """Picard mapping information"""
    id3v2: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """ID3v2 mapping information"""
    vorbis: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """Vorbis mapping information"""
    apev2: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """APEv2 mapping information"""
    itunes: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """iTunes MP4 mapping information"""
    wmp: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """ASF/Windows Media mapping information"""
    riff: TagMapInfo | list[TagMapInfo] | None = field(default=None)
    """RIFF INFO mapping information"""
    notes: int | list[int] | None = field(default=None)
    """Standard notes applicable to the tag"""
    link: str = ''
    """Link to attach to the tag"""
    seealso: str = ''
    """Text to include in a See Also block in the RestructuredText file"""


###############################
#   Tag Mapping Information   #
###############################
TAG_MAP = [
    TagMap(
        tag_name='AcoustID',
        picard=TagMapInfo('acoustid_id'),
        id3v2=TagMapInfo('TXXX:Acoustid Id'),
        vorbis=TagMapInfo('ACOUSTID_ID'),
        apev2=TagMapInfo('ACOUSTID_ID'),
        itunes=TagMapInfo('----:com.apple.iTunes:Acoustid Id'),
        wmp=TagMapInfo('Acoustid/Id'),
    ),
    TagMap(
        tag_name='AcoustID Fingerprint',
        picard=TagMapInfo('acoustid_fingerprint'),
        id3v2=TagMapInfo('TXXX:Acoustid Fingerprint'),
        vorbis=TagMapInfo('ACOUSTID_FINGERPRINT'),
        apev2=TagMapInfo('ACOUSTID_FINGERPRINT'),
        itunes=TagMapInfo('----:com.apple.iTunes:Acoustid Fingerprint'),
        wmp=TagMapInfo('Acoustid/Fingerprint'),
    ),
    TagMap(
        tag_name='Album',
        picard=TagMapInfo('album'),
        id3v2=TagMapInfo('TALB'),
        vorbis=TagMapInfo('ALBUM'),
        apev2=TagMapInfo('Album'),
        itunes=TagMapInfo('©alb'),
        wmp=TagMapInfo('WM/AlbumTitle'),
        riff=TagMapInfo('IPRD'),
        link='https://musicbrainz.org/doc/Release_Title',
    ),
    TagMap(
        tag_name='Album Artist',
        picard=TagMapInfo('albumartist'),
        id3v2=TagMapInfo('TPE2'),
        vorbis=TagMapInfo('ALBUMARTIST'),
        apev2=TagMapInfo('Album Artist'),
        itunes=TagMapInfo('aART'),
        wmp=TagMapInfo('WM/AlbumArtist'),
        link='https://musicbrainz.org/doc/Release_Artist',
    ),
    TagMap(
        tag_name='Album Artist Sort Order',
        picard=TagMapInfo('albumartistsort'),
        id3v2=[
            TagMapInfo('TSO2', desc='(Picard>=1.2)'),
            TagMapInfo('TXXX:ALBUMARTISTSORT', desc='(Picard<=1.1)'),
        ],
        vorbis=TagMapInfo('ALBUMARTISTSORT'),
        apev2=TagMapInfo('ALBUMARTISTSORT'),
        itunes=TagMapInfo('soaa'),
        wmp=TagMapInfo('WM/AlbumArtistSortOrder'),
    ),
    TagMap(
        tag_name='Album Sort Order',
        picard=TagMapInfo('albumsort'),
        id3v2=TagMapInfo('TSOA'),
        vorbis=TagMapInfo('ALBUMSORT'),
        apev2=TagMapInfo('ALBUMSORT'),
        itunes=TagMapInfo('soal'),
        wmp=TagMapInfo('WM/AlbumSortOrder'),
        notes=4,
    ),
    TagMap(
        tag_name='Arranger',
        picard=TagMapInfo('arranger'),
        id3v2=[
            TagMapInfo('TIPL:arranger', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:arranger', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('ARRANGER'),
        apev2=TagMapInfo('Arranger'),
        link='https://musicbrainz.org/relationship/22661fb8-cdb7-4f67-8385-b2a8be6c9f0d',
    ),
    TagMap(
        tag_name='Artist',
        picard=TagMapInfo('artist'),
        id3v2=TagMapInfo('TPE1'),
        vorbis=TagMapInfo('ARTIST'),
        apev2=TagMapInfo('Artist'),
        itunes=TagMapInfo('©ART'),
        wmp=TagMapInfo('Author'),
        riff=TagMapInfo('IART'),
        link='https://musicbrainz.org/doc/Artist',
    ),
    TagMap(
        tag_name='Artist Sort Order',
        picard=TagMapInfo('artistsort'),
        id3v2=TagMapInfo('TSOP'),
        vorbis=TagMapInfo('ARTISTSORT'),
        apev2=TagMapInfo('ARTISTSORT'),
        itunes=TagMapInfo('soar'),
        wmp=TagMapInfo('WM/ArtistSortOrder'),
    ),
    TagMap(
        tag_name='Artists',
        picard=TagMapInfo('artists'),
        id3v2=TagMapInfo('TXXX:Artists'),
        vorbis=TagMapInfo('ARTISTS'),
        apev2=TagMapInfo('Artists'),
        itunes=TagMapInfo('----:com.apple.iTunes:ARTISTS'),
        wmp=TagMapInfo('WM/ARTISTS'),
    ),
    TagMap(
        tag_name='ASIN',
        picard=TagMapInfo('asin'),
        id3v2=TagMapInfo('TXXX:ASIN'),
        vorbis=TagMapInfo('ASIN'),
        apev2=TagMapInfo('ASIN'),
        itunes=TagMapInfo('----:com.apple.iTunes:ASIN'),
        wmp=TagMapInfo('ASIN'),
        link='https://musicbrainz.org/doc/ASIN',
    ),
    TagMap(
        tag_name='Barcode',
        picard=TagMapInfo('barcode'),
        id3v2=TagMapInfo('TXXX:BARCODE'),
        vorbis=TagMapInfo('BARCODE'),
        apev2=TagMapInfo('Barcode'),
        itunes=TagMapInfo('----:com.apple.iTunes:BARCODE'),
        wmp=TagMapInfo('WM/Barcode'),
        link='https://musicbrainz.org/doc/Barcode',
    ),
    TagMap(
        tag_name='BPM',
        picard=TagMapInfo('bpm'),
        id3v2=TagMapInfo('TBPM'),
        vorbis=TagMapInfo('BPM'),
        apev2=TagMapInfo('BPM'),
        itunes=TagMapInfo('tmpo'),
        wmp=TagMapInfo('WM/BeatsPerMinute'),
        notes=4,
    ),
    TagMap(
        tag_name='Catalog Number',
        picard=TagMapInfo('catalognumber'),
        id3v2=TagMapInfo('TXXX:CATALOGNUMBER'),
        vorbis=TagMapInfo('CATALOGNUMBER'),
        apev2=TagMapInfo('CatalogNumber'),
        itunes=TagMapInfo('----:com.apple.iTunes:CATALOGNUMBER'),
        wmp=TagMapInfo('WM/CatalogNo'),
        link='https://musicbrainz.org/doc/Release_Catalog_Number',
    ),
    TagMap(
        tag_name='Comment',
        picard=TagMapInfo('comment:description'),
        id3v2=TagMapInfo('COMM:description'),
        vorbis=TagMapInfo('COMMENT'),
        apev2=TagMapInfo('Comment'),
        itunes=TagMapInfo('©cmt'),
        wmp=TagMapInfo('Description'),
        riff=TagMapInfo('ICMT'),
        notes=4,
    ),
    TagMap(
        tag_name='Compilation (iTunes)',
        picard=TagMapInfo('compilation'),
        id3v2=TagMapInfo('TCMP'),
        vorbis=TagMapInfo('COMPILATION'),
        apev2=TagMapInfo('Compilation'),
        itunes=TagMapInfo('cpil'),
        wmp=TagMapInfo('WM/IsCompilation'),
        notes=5,
    ),
    TagMap(
        tag_name='Composer',
        picard=TagMapInfo('composer'),
        id3v2=TagMapInfo('TCOM'),
        vorbis=TagMapInfo('COMPOSER'),
        apev2=TagMapInfo('Composer'),
        itunes=TagMapInfo('©wrt'),
        wmp=TagMapInfo('WM/Composer'),
        riff=TagMapInfo('IMUS'),
        link='https://musicbrainz.org/relationship/d59d99ea-23d4-4a80-b066-edca32ee158f',
    ),
    TagMap(
        tag_name='Composer Sort Order',
        picard=TagMapInfo('composersort'),
        id3v2=[
            TagMapInfo('TSOC', desc='(Picard>=1.3)'),
            TagMapInfo('TXXX:COMPOSERSORT', desc='(Picard<=1.2)'),
        ],
        vorbis=TagMapInfo('COMPOSERSORT'),
        apev2=TagMapInfo('COMPOSERSORT'),
        itunes=TagMapInfo('soco'),
        wmp=TagMapInfo('WM/ComposerSortOrder', desc='(Picard>=1.3)'),
    ),
    TagMap(
        tag_name='Conductor',
        picard=TagMapInfo('conductor'),
        id3v2=TagMapInfo('TPE3'),
        vorbis=TagMapInfo('CONDUCTOR'),
        apev2=TagMapInfo('Conductor'),
        itunes=TagMapInfo('----:com.apple.iTunes:CONDUCTOR'),
        wmp=TagMapInfo('WM/Conductor'),
        link='https://musicbrainz.org/relationship/234670ce-5f22-4fd0-921b-ef1662695c5d',
    ),
    TagMap(
        tag_name='Copyright',
        picard=TagMapInfo('copyright'),
        id3v2=TagMapInfo('TCOP'),
        vorbis=TagMapInfo('COPYRIGHT'),
        apev2=TagMapInfo('Copyright'),
        itunes=TagMapInfo('cprt'),
        wmp=TagMapInfo('Copyright'),
        riff=TagMapInfo('ICOP'),
        notes=4,
    ),
    TagMap(
        tag_name='Director',
        picard=TagMapInfo('director'),
        id3v2=TagMapInfo('TXXX:DIRECTOR'),
        vorbis=TagMapInfo('DIRECTOR'),
        apev2=TagMapInfo('Director'),
        itunes=TagMapInfo('©dir', notes=9),
        wmp=TagMapInfo('WM/Director'),
    ),
    TagMap(
        tag_name='Disc Number',
        picard=TagMapInfo('discnumber'),
        id3v2=TagMapInfo('TPOS'),
        vorbis=TagMapInfo('DISCNUMBER'),
        apev2=TagMapInfo('Disc'),
        itunes=TagMapInfo('disk'),
        wmp=TagMapInfo('WM/PartOfSet'),
    ),
    TagMap(
        tag_name='Disc Subtitle',
        picard=TagMapInfo('discsubtitle'),
        id3v2=TagMapInfo('TSST', desc='(ID3v2.4 only)'),
        vorbis=TagMapInfo('DISCSUBTITLE'),
        apev2=TagMapInfo('DiscSubtitle'),
        itunes=TagMapInfo('----:com.apple.iTunes:DISCSUBTITLE'),
        wmp=TagMapInfo('WM/SetSubTitle'),
    ),
    TagMap(
        tag_name='Encoded By',
        picard=TagMapInfo('encodedby'),
        id3v2=TagMapInfo('TENC'),
        vorbis=TagMapInfo('ENCODEDBY'),
        apev2=TagMapInfo('EncodedBy'),
        itunes=TagMapInfo('©too'),
        wmp=TagMapInfo('WM/EncodedBy'),
        riff=TagMapInfo('IENC'),
        notes=4,
    ),
    TagMap(
        tag_name='Encoder Settings',
        picard=TagMapInfo('encodersettings'),
        id3v2=TagMapInfo('TSSE'),
        vorbis=TagMapInfo('ENCODERSETTINGS'),
        apev2=TagMapInfo('EncoderSettings'),
        wmp=TagMapInfo('WM/EncodingSettings', desc='(Picard>=1.3.1)'),
        notes=4,
    ),
    TagMap(
        tag_name='Engineer',
        picard=TagMapInfo('engineer'),
        id3v2=[
            TagMapInfo('TIPL:engineer', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:engineer', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('ENGINEER'),
        apev2=TagMapInfo('Engineer'),
        itunes=TagMapInfo('----:com.apple.iTunes:ENGINEER'),
        wmp=TagMapInfo('WM/Engineer'),
        riff=TagMapInfo('IENG'),
        link='https://musicbrainz.org/relationship/5dcc52af-7064-4051-8d62-7d80f4c3c907',
    ),
    TagMap(
        tag_name='Gapless Playback',
        picard=TagMapInfo('gapless'),
        itunes=TagMapInfo('pgap'),
        notes=4,
    ),
    TagMap(
        tag_name='Genre',
        picard=TagMapInfo('genre'),
        id3v2=TagMapInfo('TCON'),
        vorbis=TagMapInfo('GENRE'),
        apev2=TagMapInfo('Genre'),
        itunes=TagMapInfo('©gen'),
        wmp=TagMapInfo('WM/Genre'),
        riff=TagMapInfo('IGNR'),
        link='https://musicbrainz.org/doc/Genre',
    ),
    TagMap(
        tag_name='Grouping',
        picard=TagMapInfo('grouping'),
        id3v2=[
            TagMapInfo('TIT1'),
            TagMapInfo('GRP1', notes=8),
        ],
        vorbis=TagMapInfo('GROUPING'),
        apev2=TagMapInfo('Grouping'),
        itunes=TagMapInfo('©grp'),
        wmp=TagMapInfo('WM/ContentGroupDescription'),
        notes=3,
    ),
    TagMap(
        tag_name='Initial Key',
        picard=TagMapInfo('key', desc='(Picard>=1.4)'),
        id3v2=TagMapInfo('TKEY'),
        vorbis=TagMapInfo('KEY'),
        apev2=TagMapInfo('KEY'),
        itunes=TagMapInfo('----:com.apple.iTunes:initialkey'),
        wmp=TagMapInfo('WM/InitialKey'),
    ),
    TagMap(
        tag_name='ISRC',
        picard=TagMapInfo('isrc'),
        id3v2=TagMapInfo('TSRC'),
        vorbis=TagMapInfo('ISRC'),
        apev2=TagMapInfo('ISRC'),
        itunes=TagMapInfo('----:com.apple.iTunes:ISRC'),
        wmp=TagMapInfo('WM/ISRC'),
        link='https://musicbrainz.org/doc/ISRC',
    ),
    TagMap(
        tag_name='iTunes CDDB 1',
        picard=TagMapInfo('itunes_cddb_1'),
        id3v2=TagMapInfo('iTunes_CDDB_1'),
        itunes=TagMapInfo('----:com.apple.iTunes:iTunes_CDDB_1'),
        notes=9,
    ),
    TagMap(
        tag_name='Language',
        picard=TagMapInfo('language'),
        id3v2=TagMapInfo('TLAN'),
        vorbis=TagMapInfo('LANGUAGE'),
        apev2=TagMapInfo('Language'),
        itunes=TagMapInfo('----:com.apple.iTunes:LANGUAGE'),
        wmp=TagMapInfo('WM/Language'),
        riff=TagMapInfo('ILNG'),
    ),
    TagMap(
        tag_name='License',
        picard=TagMapInfo('license'),
        id3v2=[
            TagMapInfo('WCOP', desc='(single URL)'),
            TagMapInfo('TXXX:LICENSE', desc='(multiple or non-URL)'),
        ],
        vorbis=TagMapInfo('LICENSE'),
        apev2=TagMapInfo('LICENSE'),
        itunes=TagMapInfo('----:com.apple.iTunes:LICENSE'),
        notes=[6, 7],
    ),
    TagMap(
        tag_name='Lyricist',
        picard=TagMapInfo('lyricist'),
        id3v2=TagMapInfo('TEXT'),
        vorbis=TagMapInfo('LYRICIST'),
        apev2=TagMapInfo('Lyricist'),
        itunes=TagMapInfo('----:com.apple.iTunes:LYRICIST'),
        wmp=TagMapInfo('WM/Writer'),
        link='https://musicbrainz.org/relationship/3e48faba-ec01-47fd-8e89-30e81161661c',
    ),
    TagMap(
        tag_name='Lyrics',
        picard=TagMapInfo('lyrics:description'),
        id3v2=TagMapInfo('USLT:description'),
        vorbis=TagMapInfo('LYRICS'),
        apev2=TagMapInfo('Lyrics'),
        itunes=TagMapInfo('©lyr'),
        wmp=TagMapInfo('WM/Lyrics'),
        notes=4,
    ),
    TagMap(
        tag_name='Media',
        picard=TagMapInfo('media'),
        id3v2=TagMapInfo('TMED'),
        vorbis=TagMapInfo('MEDIA'),
        apev2=TagMapInfo('Media'),
        itunes=TagMapInfo('----:com.apple.iTunes:MEDIA'),
        wmp=TagMapInfo('WM/Media'),
        riff=TagMapInfo('IMED'),
        link='https://musicbrainz.org/doc/Release_Format',
    ),
    TagMap(
        tag_name='Mix-DJ',
        picard=TagMapInfo('djmixer'),
        id3v2=[
            TagMapInfo('TIPL:DJ-mix', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:DJ-mix', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('DJMIXER'),
        apev2=TagMapInfo('DJMixer'),
        itunes=TagMapInfo('----:com.apple.iTunes:DJMIXER'),
        wmp=TagMapInfo('WM/DJMixer'),
        link='https://musicbrainz.org/relationship/28338ee6-d578-485a-bb53-61dbfd7c6545',
    ),
    TagMap(
        tag_name='Mixer',
        picard=TagMapInfo('mixer'),
        id3v2=[
            TagMapInfo('TIPL:mix', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:mix', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('MIXER'),
        apev2=TagMapInfo('Mixer'),
        itunes=TagMapInfo('----:com.apple.iTunes:MIXER'),
        wmp=TagMapInfo('WM/Mixer'),
        link='https://musicbrainz.org/relationship/3e3102e1-1896-4f50-b5b2-dd9824e46efe',
    ),
    TagMap(
        tag_name='Mood',
        picard=TagMapInfo('mood'),
        id3v2=TagMapInfo('TMOO', desc='(ID3v2.4 only)'),
        vorbis=TagMapInfo('MOOD'),
        apev2=TagMapInfo('Mood'),
        itunes=TagMapInfo('----:com.apple.iTunes:MOOD'),
        wmp=TagMapInfo('WM/Mood'),
        notes=3,
    ),
    TagMap(
        tag_name='Movement',
        picard=TagMapInfo('movement', desc='(Picard>=2.1)'),
        id3v2=TagMapInfo('MVNM'),
        vorbis=TagMapInfo('MOVEMENTNAME'),
        apev2=TagMapInfo('MOVEMENTNAME'),
        itunes=TagMapInfo('©mvn'),
        notes=4,
    ),
    TagMap(
        tag_name='Movement Count',
        picard=TagMapInfo('movementtotal', desc='(Picard>=2.1)'),
        id3v2=TagMapInfo('MVIN'),
        vorbis=TagMapInfo('MOVEMENTTOTAL'),
        apev2=TagMapInfo('MOVEMENTTOTAL'),
        itunes=TagMapInfo('mvc'),
        notes=4,
    ),
    TagMap(
        tag_name='Movement Number',
        picard=TagMapInfo('movementnumber', desc='(Picard>=2.1)'),
        id3v2=TagMapInfo('MVIN'),
        vorbis=TagMapInfo('MOVEMENT'),
        apev2=TagMapInfo('MOVEMENT'),
        itunes=TagMapInfo('mvi'),
        notes=4,
    ),
    TagMap(
        tag_name='MusicBrainz Artist ID',
        picard=TagMapInfo('musicbrainz_artistid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Artist Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_ARTISTID'),
        apev2=TagMapInfo('MUSICBRAINZ_ARTISTID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Artist Id'),
        wmp=TagMapInfo('MusicBrainz/Artist Id'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Composer ID',
        picard=TagMapInfo('musicbrainz_composerid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Composer Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_COMPOSERID'),
        apev2=TagMapInfo('MUSICBRAINZ_COMPOSERID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Composer Id'),
        wmp=TagMapInfo('MusicBrainz/Composer Id'),
    ),
    TagMap(
        tag_name='MusicBrainz Disc ID',
        picard=TagMapInfo('musicbrainz_discid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Disc Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_DISCID'),
        apev2=TagMapInfo('MUSICBRAINZ_DISCID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Disc Id'),
        wmp=TagMapInfo('MusicBrainz/Disc Id'),
        link='https://musicbrainz.org/doc/Disc_ID',
    ),
    TagMap(
        tag_name='MusicBrainz Original Artist ID',
        picard=TagMapInfo('musicbrainz_originalartistid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Original Artist Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_ORIGINALARTISTID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Original Artist Id', desc='(Picard>=2.1)'),
        wmp=TagMapInfo('MusicBrainz/Original Artist Id', desc='(Picard>=2.1)'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Original Release ID',
        picard=TagMapInfo('musicbrainz_originalalbumid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Original Album Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_ORIGINALALBUMID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Original Album Id', desc='(Picard>=2.1)'),
        wmp=TagMapInfo('MusicBrainz/Original Album Id', desc='(Picard>=2.1)'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Recording ID',
        picard=TagMapInfo('musicbrainz_recordingid'),
        id3v2=TagMapInfo('UFID:http://musicbrainz.org'),
        vorbis=TagMapInfo('MUSICBRAINZ_TRACKID'),
        apev2=TagMapInfo('MUSICBRAINZ_TRACKID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Track Id'),
        wmp=TagMapInfo('MusicBrainz/Track Id'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Release Artist ID',
        picard=TagMapInfo('musicbrainz_albumartistid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Album Artist Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_ALBUMARTISTID'),
        apev2=TagMapInfo('MUSICBRAINZ_ALBUMARTISTID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Album Artist Id'),
        wmp=TagMapInfo('MusicBrainz/Album Artist Id'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Release Group ID',
        picard=TagMapInfo('musicbrainz_releasegroupid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Release Group Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_RELEASEGROUPID'),
        apev2=TagMapInfo('MUSICBRAINZ_RELEASEGROUPID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Release Group Id'),
        wmp=TagMapInfo('MusicBrainz/Release Group Id'),
    ),
    TagMap(
        tag_name='MusicBrainz Release ID',
        picard=TagMapInfo('musicbrainz_albumid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Album Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_ALBUMID'),
        apev2=TagMapInfo('MUSICBRAINZ_ALBUMID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Album Id'),
        wmp=TagMapInfo('MusicBrainz/Album Id'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz Track ID',
        picard=TagMapInfo('musicbrainz_trackid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Release Track Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_RELEASETRACKID'),
        apev2=TagMapInfo('MUSICBRAINZ_RELEASETRACKID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Release Track Id'),
        wmp=TagMapInfo('MusicBrainz/Release Track Id'),
        link='https://musicbrainz.org/doc/MusicBrainz_Identifier',
    ),
    TagMap(
        tag_name='MusicBrainz TRM ID',
        picard=TagMapInfo('musicbrainz_trmid', desc='(deprecated)'),
        id3v2=TagMapInfo('TXXX:MusicBrainz TRM Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_TRMID'),
        apev2=TagMapInfo('MUSICBRAINZ_TRMID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz TRM Id'),
        wmp=TagMapInfo('MusicBrainz/TRM Id'),
        link='https://musicbrainz.org/doc/TRM',
    ),
    TagMap(
        tag_name='MusicBrainz Work ID',
        picard=TagMapInfo('musicbrainz_workid'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Work Id'),
        vorbis=TagMapInfo('MUSICBRAINZ_WORKID'),
        apev2=TagMapInfo('MUSICBRAINZ_WORKID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Work Id'),
        wmp=TagMapInfo('MusicBrainz/Work Id'),
    ),
    TagMap(
        tag_name='MusicIP Fingerprint',
        picard=TagMapInfo('musicip_fingerprint'),
        id3v2=TagMapInfo('TXXX:MusicMagic Fingerprint'),
        vorbis=TagMapInfo('FINGERPRINT=MusicMagic Fingerprint {fingerprint}'),
        itunes=TagMapInfo('----:com.apple.iTunes:fingerprint'),
    ),
    TagMap(
        tag_name='MusicIP PUID',
        picard=TagMapInfo('musicip_puid'),
        id3v2=TagMapInfo('TXXX:MusicIP PUID'),
        vorbis=TagMapInfo('MUSICIP_PUID'),
        apev2=TagMapInfo('MUSICIP_PUID'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicIP PUID'),
        wmp=TagMapInfo('MusicIP/PUID'),
        link='https://musicbrainz.org/doc/PUID',
    ),
    TagMap(
        tag_name='Original Album',
        picard=TagMapInfo('originalalbum'),
        id3v2=TagMapInfo('TOAL'),
        wmp=TagMapInfo('WM/OriginalAlbumTitle', desc='(Picard>=2.1)'),
    ),
    TagMap(
        tag_name='Original Artist',
        picard=TagMapInfo('originalartist'),
        id3v2=TagMapInfo('TOPE'),
        apev2=TagMapInfo('Original Artist', desc='(Picard>=2.1)'),
        wmp=TagMapInfo('WM/OriginalArtist', desc='(Picard>=2.1)'),
    ),
    TagMap(
        tag_name='Original Filename',
        picard=TagMapInfo('originalfilename', desc='(Picard>=2.3)'),
        id3v2=TagMapInfo('TOFN'),
        vorbis=TagMapInfo('ORIGINALFILENAME'),
        apev2=TagMapInfo('ORIGINALFILENAME'),
        wmp=TagMapInfo('WM/OriginalFilename'),
    ),
    TagMap(
        tag_name='Original Release Date',
        picard=TagMapInfo('originaldate'),
        id3v2=[
            TagMapInfo('TDOR', desc='(ID3v2.4)'),
            TagMapInfo('TORY', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('ORIGINALDATE'),
        wmp=[
            TagMapInfo('WM/OriginalReleaseTime', desc='(Picard>=1.3.1)'),
            TagMapInfo('WM/OriginalReleaseYear', desc='(Picard<=1.3.0)'),
        ],
        notes=1,
    ),
    TagMap(
        tag_name='Original Release Year',
        picard=TagMapInfo('originalyear'),
        vorbis=TagMapInfo('ORIGINALYEAR'),
        apev2=TagMapInfo('ORIGINALYEAR'),
        wmp=TagMapInfo('WM/OriginalReleaseYear', desc='(Picard>=1.3.1)'),
        notes=1,
    ),
    TagMap(
        tag_name='Performer',
        picard=TagMapInfo('performer:instrument'),
        id3v2=[
            TagMapInfo('TMCL:instrument', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:instrument', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('PERFORMER={artist} (instrument)'),
        apev2=TagMapInfo('Performer={artist} (instrument)'),
        seealso=(
            'Please refer to the following for more information:\n\n'
            '- `Relationship Types / Artist-Release / Performer <https://musicbrainz.org/relationship/888a2320-52e4-4fe8-a8a0-7a4c8dfde167>`_\n'
            '- `Relationship Types / Artist-Release / Vocal <https://musicbrainz.org/relationship/eb10f8a0-0f4c-4dce-aa47-87bcb2bc42f3>`_\n'
            '- `Relationship Types / Artist-Release / Instrument <https://musicbrainz.org/relationship/67555849-61e5-455b-96e3-29733f0115f5>`_\n'
            '- `Relationship Types / Artist-Recording / Performer <https://musicbrainz.org/relationship/628a9658-f54c-4142-b0c0-95f031b544da>`_\n'
            '- `Relationship Types / Artist-Recording / Vocal <https://musicbrainz.org/relationship/0fdbe3c6-7700-4a31-ae54-b53f06ae1cfa>`_\n'
            '- `Relationship Types / Artist-Recording / Instrument <https://musicbrainz.org/relationship/59054b12-01ac-43ee-a618-285fd397e461>`_'
        ),
    ),
    TagMap(
        tag_name='Podcast',
        picard=TagMapInfo('podcast'),
        itunes=TagMapInfo('pcst'),
        notes=4,
    ),
    TagMap(
        tag_name='Podcast URL',
        picard=TagMapInfo('podcasturl'),
        itunes=TagMapInfo('purl'),
        notes=4,
    ),
    TagMap(
        tag_name='Producer',
        picard=TagMapInfo('producer'),
        id3v2=[
            TagMapInfo('TIPL:producer', desc='(ID3v2.4)'),
            TagMapInfo('IPLS:producer', desc='(ID3v2.3)'),
        ],
        vorbis=TagMapInfo('PRODUCER'),
        apev2=TagMapInfo('Producer'),
        itunes=TagMapInfo('----:com.apple.iTunes:PRODUCER'),
        wmp=TagMapInfo('WM/Producer'),
        riff=TagMapInfo('IPRO'),
        link='https://musicbrainz.org/relationship/5c0ceac3-feb4-41f0-868d-dc06f6e27fc0',
    ),
    TagMap(
        tag_name='Rating',
        picard=TagMapInfo('_rating'),
        id3v2=TagMapInfo('POPM'),
        vorbis=TagMapInfo('RATING:user@email'),
        wmp=TagMapInfo('WM/SharedUserRating'),
        link='https://musicbrainz.org/doc/Rating_System',
    ),
    TagMap(
        tag_name='Record Label',
        picard=TagMapInfo('label'),
        id3v2=TagMapInfo('TPUB'),
        vorbis=TagMapInfo('LABEL'),
        apev2=TagMapInfo('Label'),
        itunes=TagMapInfo('----:com.apple.iTunes:LABEL'),
        wmp=TagMapInfo('WM/Publisher'),
        link='https://musicbrainz.org/doc/Label_Name',
    ),
    TagMap(
        tag_name='Release Country',
        picard=TagMapInfo('releasecountry'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Album Release Country'),
        vorbis=TagMapInfo('RELEASECOUNTRY'),
        apev2=TagMapInfo('RELEASECOUNTRY'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Album Release Country'),
        wmp=TagMapInfo('MusicBrainz/Album Release Country'),
        riff=TagMapInfo('ICNT'),
        link='https://musicbrainz.org/doc/Release_Country',
    ),
    TagMap(
        tag_name='Release Date',
        picard=TagMapInfo('date'),
        id3v2=[
            TagMapInfo('TDRC', desc='(ID3v2.4)'),
            TagMapInfo('TYER', desc='+ ``TDAT`` (ID3v2.3)'),
        ],
        vorbis=TagMapInfo('DATE'),
        apev2=TagMapInfo('Year'),
        itunes=TagMapInfo('©day'),
        wmp=TagMapInfo('WM/Year'),
        riff=TagMapInfo('ICRD'),
        link='https://musicbrainz.org/doc/Release_Date',
    ),
    TagMap(
        tag_name='Release Status',
        picard=TagMapInfo('releasestatus'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Album Status'),
        vorbis=TagMapInfo('RELEASESTATUS'),
        apev2=TagMapInfo('MUSICBRAINZ_ALBUMSTATUS'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Album Status'),
        wmp=TagMapInfo('MusicBrainz/Album Status'),
        link='https://musicbrainz.org/doc/Release_Status',
    ),
    TagMap(
        tag_name='Release Type',
        picard=TagMapInfo('releasetype'),
        id3v2=TagMapInfo('TXXX:MusicBrainz Album Type'),
        vorbis=TagMapInfo('RELEASETYPE'),
        apev2=TagMapInfo('MUSICBRAINZ_ALBUMTYPE'),
        itunes=TagMapInfo('----:com.apple.iTunes:MusicBrainz Album Type'),
        wmp=TagMapInfo('MusicBrainz/Album Type'),
        link='https://musicbrainz.org/doc/Release_Type',
    ),
    TagMap(
        tag_name='Remixer',
        picard=TagMapInfo('remixer'),
        id3v2=TagMapInfo('TPE4'),
        vorbis=TagMapInfo('REMIXER'),
        apev2=TagMapInfo('MixArtist'),
        itunes=TagMapInfo('----:com.apple.iTunes:REMIXER'),
        wmp=TagMapInfo('WM/ModifiedBy'),
        link='https://musicbrainz.org/relationship/7950be4d-13a3-48e7-906b-5af562e39544',
    ),
    TagMap(
        tag_name='ReplayGain Album Gain',
        picard=TagMapInfo('replaygain_album_gain', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_ALBUM_GAIN'),
        vorbis=TagMapInfo('REPLAYGAIN_ALBUM_GAIN'),
        apev2=TagMapInfo('REPLAYGAIN_ALBUM_GAIN'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_ALBUM_GAIN'),
        wmp=TagMapInfo('REPLAYGAIN_ALBUM_GAIN'),
    ),
    TagMap(
        tag_name='ReplayGain Album Peak',
        picard=TagMapInfo('replaygain_album_peak', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_ALBUM_PEAK'),
        vorbis=TagMapInfo('REPLAYGAIN_ALBUM_PEAK'),
        apev2=TagMapInfo('REPLAYGAIN_ALBUM_PEAK'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_ALBUM_PEAK'),
        wmp=TagMapInfo('REPLAYGAIN_ALBUM_PEAK'),
    ),
    TagMap(
        tag_name='ReplayGain Album Range',
        picard=TagMapInfo('replaygain_album_range', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_ALBUM_RANGE'),
        vorbis=TagMapInfo('REPLAYGAIN_ALBUM_RANGE'),
        apev2=TagMapInfo('REPLAYGAIN_ALBUM_RANGE'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_ALBUM_RANGE'),
        wmp=TagMapInfo('REPLAYGAIN_ALBUM_RANGE'),
    ),
    TagMap(
        tag_name='ReplayGain Reference Loudness',
        picard=TagMapInfo('replaygain_reference_loudness', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_REFERENCE_LOUDNESS'),
        vorbis=TagMapInfo('REPLAYGAIN_REFERENCE_LOUDNESS'),
        apev2=TagMapInfo('REPLAYGAIN_REFERENCE_LOUDNESS'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_REFERENCE_LOUDNESS'),
        wmp=TagMapInfo('REPLAYGAIN_REFERENCE_LOUDNESS'),
    ),
    TagMap(
        tag_name='ReplayGain Track Gain',
        picard=TagMapInfo('replaygain_track_gain', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_TRACK_GAIN'),
        vorbis=TagMapInfo('REPLAYGAIN_TRACK_GAIN'),
        apev2=TagMapInfo('REPLAYGAIN_TRACK_GAIN'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_TRACK_GAIN'),
        wmp=TagMapInfo('REPLAYGAIN_TRACK_GAIN'),
    ),
    TagMap(
        tag_name='ReplayGain Track Peak',
        picard=TagMapInfo('replaygain_track_peak', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_TRACK_PEAK'),
        vorbis=TagMapInfo('REPLAYGAIN_TRACK_PEAK'),
        apev2=TagMapInfo('REPLAYGAIN_TRACK_PEAK'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_TRACK_PEAK'),
        wmp=TagMapInfo('REPLAYGAIN_TRACK_PEAK'),
    ),
    TagMap(
        tag_name='ReplayGain Track Range',
        picard=TagMapInfo('replaygain_track_range', desc='(Picard>=2.2)'),
        id3v2=TagMapInfo('TXXX:REPLAYGAIN_TRACK_RANGE'),
        vorbis=TagMapInfo('REPLAYGAIN_TRACK_RANGE'),
        apev2=TagMapInfo('REPLAYGAIN_TRACK_RANGE'),
        itunes=TagMapInfo('----:com.apple.iTunes:REPLAYGAIN_TRACK_RANGE'),
        wmp=TagMapInfo('REPLAYGAIN_TRACK_RANGE'),
    ),
    TagMap(
        tag_name='Script',
        picard=TagMapInfo('script'),
        id3v2=TagMapInfo('TXXX:SCRIPT'),
        vorbis=TagMapInfo('SCRIPT'),
        apev2=TagMapInfo('Script'),
        itunes=TagMapInfo('----:com.apple.iTunes:SCRIPT'),
        wmp=TagMapInfo('WM/Script'),
    ),
    TagMap(
        tag_name='Show Name',
        picard=TagMapInfo('show'),
        itunes=TagMapInfo('tvsh'),
        notes=4,
    ),
    TagMap(
        tag_name='Show Name Sort Order',
        picard=TagMapInfo('showsort'),
        itunes=TagMapInfo('sosn'),
        notes=4,
    ),
    TagMap(
        tag_name='Show Work & Movement',
        picard=TagMapInfo('showmovement', desc='(Picard>=2.1)'),
        id3v2=TagMapInfo('TXXX:SHOWMOVEMENT'),
        vorbis=TagMapInfo('SHOWMOVEMENT'),
        apev2=TagMapInfo('SHOWMOVEMENT'),
        itunes=TagMapInfo('shwm'),
        notes=4,
    ),
    TagMap(
        tag_name='Subtitle',
        picard=TagMapInfo('subtitle'),
        id3v2=TagMapInfo('TIT3'),
        vorbis=TagMapInfo('SUBTITLE'),
        apev2=TagMapInfo('Subtitle'),
        itunes=TagMapInfo('----:com.apple.iTunes:SUBTITLE'),
        wmp=TagMapInfo('WM/SubTitle'),
        notes=4,
    ),
    TagMap(
        tag_name='Synced Lyrics',
        picard=TagMapInfo('syncedlyrics:language:description', notes='(Picard>=3.0)'),
        id3v2=TagMapInfo('SYLT:description'),
        wmp=TagMapInfo('WM/Lyrics_Synchronised'),
    ),
    TagMap(
        tag_name='Total Discs',
        picard=TagMapInfo('totaldiscs'),
        id3v2=TagMapInfo('TPOS'),
        vorbis=TagMapInfo('DISCTOTAL and TOTALDISCS'),
        apev2=TagMapInfo('Disc'),
        itunes=TagMapInfo('disk'),
        wmp=TagMapInfo('WM/PartOfSet', desc='(Picard>=1.3.1)'),
    ),
    TagMap(
        tag_name='Total Tracks',
        picard=TagMapInfo('totaltracks'),
        id3v2=TagMapInfo('TRCK'),
        vorbis=TagMapInfo('TRACKTOTAL', desc='and ``TOTALTRACKS``'),
        apev2=TagMapInfo('Track'),
        itunes=TagMapInfo('trkn'),
    ),
    TagMap(
        tag_name='Track Number',
        picard=TagMapInfo('tracknumber'),
        id3v2=TagMapInfo('TRCK'),
        vorbis=TagMapInfo('TRACKNUMBER'),
        apev2=TagMapInfo('Track'),
        itunes=TagMapInfo('trkn'),
        wmp=TagMapInfo('WM/TrackNumber'),
        riff=TagMapInfo('ITRK'),
    ),
    TagMap(
        tag_name='Track Title',
        picard=TagMapInfo('title'),
        id3v2=TagMapInfo('TIT2'),
        vorbis=TagMapInfo('TITLE'),
        apev2=TagMapInfo('Title'),
        itunes=TagMapInfo('©nam'),
        wmp=TagMapInfo('Title'),
        riff=TagMapInfo('INAM'),
        link='https://musicbrainz.org/doc/Track_Title',
    ),
    TagMap(
        tag_name='Track Title Sort Order',
        picard=TagMapInfo('titlesort'),
        id3v2=TagMapInfo('TSOT'),
        vorbis=TagMapInfo('TITLESORT'),
        apev2=TagMapInfo('TITLESORT'),
        itunes=TagMapInfo('sonm'),
        wmp=TagMapInfo('WM/TitleSortOrder'),
        notes=4,
    ),
    TagMap(
        tag_name='Website (official artist website)',
        picard=TagMapInfo('website'),
        id3v2=TagMapInfo('WOAR'),
        vorbis=TagMapInfo('WEBSITE'),
        apev2=TagMapInfo('Weblink'),
        wmp=TagMapInfo('WM/AuthorURL', desc='(Picard>=1.3.1)'),
    ),
    TagMap(
        tag_name='Work Title',
        picard=TagMapInfo('work', desc='(Picard>=1.3)'),
        id3v2=TagMapInfo('TXXX:WORK', desc='``TIT1``', notes=8),
        vorbis=TagMapInfo('WORK'),
        apev2=TagMapInfo('WORK'),
        itunes=TagMapInfo('©wrk', desc='(Picard>=2.1)'),
        wmp=TagMapInfo('WM/Work'),
    ),
    TagMap(
        tag_name='Writer',
        picard=TagMapInfo('writer'),
        id3v2=TagMapInfo('TXXX:Writer', desc='(Picard>=1.3)'),
        vorbis=TagMapInfo('WRITER'),
        apev2=TagMapInfo('Writer'),
        riff=TagMapInfo('IWRI'),
        notes=2,
        link='https://musicbrainz.org/relationship/a255bca1-b157-4518-9108-7b147dc3fc68',
    ),
]

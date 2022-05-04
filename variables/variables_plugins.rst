.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

:index:`Tags from Plugins <tags; plugins>`
===========================================

Plugins from Picard :doc:`Plugins </config/options_plugins>` can add more tags.  Following are some examples.

Last.fm Plugin
--------------

**genre**

   Pseudo-genre based on folksonomy tags.


Additional Artists Variables Plugin
-----------------------------------

**Album Variables**

   **_artists_album_primary_id**

      The ID of the primary / first album artist listed

   **_artists_album_primary_std**

      The primary / first album artist listed (standardized)

   **_artists_album_primary_cred**

      The primary / first album artist listed (as credited)

   **_artists_album_primary_sort**

      The primary / first album artist listed (sort name)

   **_artists_album_additional_id**

      The IDs of all album artists listed except for the primary / first artist, as a multi-value

   **_artists_album_additional_std**

      All album artists listed (standardized) except for the primary / first artist, separated by strings provided from the release entry

   **_artists_album_additional_cred**

      All album artists listed (as credited) except for the primary / first artist, separated by strings provided from the release entry

   **_artists_album_additional_sort**

      All album artists listed (sort names) except for the primary / first artist, separated by strings provided from the release entry

   **_artists_album_additional_std_multi**

      All album artists listed (standardized) except for the primary / first artist, as a multi-value

   **_artists_album_additional_cred_multi**

      All album artists listed (as credited) except for the primary / first artist, as a multi-value

   **_artists_album_all_std**

      All album artists listed (standardized), separated by strings provided from the release entry

   **_artists_album_all_cred**

      All album artists listed (as credited), separated by strings provided from the release entry

   **_artists_album_all_sort**

      All album artists listed (sort names), separated by strings provided from the release entry

   **_artists_album_all_std_multi**

      All album artists listed (standardized), as a multi-value

   **_artists_album_all_cred_multi**

      All album artists listed (as credited), as a multi-value

   **_artists_album_all_sort_primary**

      The primary / first album artist listed (sort name) followed by all additional album artists (standardized), separated by strings provided from the release entry

   **_artists_album_all_count**

      The number of artists listed as album artists


**Track Variables**

   **_artists_track_primary_id**

      The ID of the primary / first track artist listed

   **_artists_track_primary_std**

      The primary / first track artist listed (standardized)

   **_artists_track_primary_cred**

      The primary / first track artist listed (as credited)

   **_artists_track_primary_sort**

      The primary / first track artist listed (sort name)

   **_artists_track_additional_id**

      The IDs of all track artists listed except for the primary / first artist, as a multi-value

   **_artists_track_additional_std**

      All track artists listed (standardized) except for the primary / first artist, separated by strings provided from the track entry

   **_artists_track_additional_cred**

      All track artists listed (as credited) except for the primary / first artist, separated by strings provided from the track entry

   **_artists_track_additional_sort**

      All track artists listed (sort names) except for the primary / first artist, separated by strings provided from the track entry

   **_artists_track_additional_std_multi**

      All track artists listed (standardized) except for the primary / first artist, as a multi-value

   **_artists_track_additional_cred_multi**

      All track artists listed (as credited) except for the primary / first artist, as a multi-value

   **_artists_track_all_std**

      All track artists listed (standardized), separated by strings provided from the track entry

   **_artists_track_all_cred**

      All track artists listed (as credited), separated by strings provided from the track entry

   **_artists_track_all_sort**

      All track artists listed (sort names), separated by strings provided from the track entry

   **_artists_track_all_std_multi**

      All track artists listed (standardized), as a multi-value

   **_artists_track_all_cred_multi**

      All track artists listed (as credited), as a multi-value

   **_artists_track_all_sort_primary**

      The primary / first track artist listed (sort name) followed by all additional track artists (standardized), separated by strings provided from the track entry

   **_artists_track_all_count**

      The number of artists listed as track artists

.. note::

   Some plugins make a large number of web service calls to get additional track-specific data such as performer and work relationships,
   so loading a large number of albums and tracks could take a significant amount of time.  The time concern can be partially addressed by
   operating a local MusicBrainz server with the rate limiting disabled.  Please see the `MusicBrainz Server <https://github.com/metabrainz/musicbrainz-server>`_
   project on GitHub for additional information.



.. Last.fm Plus
.. ------------

.. The LastFMPlus plugin is a sophisticated plugin that tries to provide stable and meaningful genre selections from the ever-changing and
.. idiosyncratic list provided by lastFM.

.. The LastFMPlus plugin is very configurable and examples provided here are based on the default lists provided on the Tag Filter List tab
.. of the LastFMPlus options page.

.. **Comment:songs-db_Custom1**

..    The decade (e.g.: 1970s).

.. **Comment:songs-db_Custom2**

..    Category (e.g.: Female Vocalist, Singer-Songwriter).

.. **Comment:songs-db_Custom3**

..    Country (e.g.: British).

.. **Comment:songs-db_Occassion**

..    Good situations to play a track (e.g.: Driving, Love, Party).

.. **genre**

..    Specific detailed genres. For example, if the group is Rock the genre could be one of Acid rock, Acoustic rock, Alternative metal,
..    Alternative rock, Art rock, Blues rock, Boogie rock, Brit rock, Christian rock, College rock, Country rock, etc.

.. **grouping**

..    Top-level genres - default list: Audiobooks, Blues, Classic rock, Classical, Country, Dance, Electronica, Folk, Hip-hop, Indie, Jazz,
..    Kids, Metal, Pop, Punk, Reggae, Rock, Soul, Trance

.. **mood**

..    How a track "feels" (e.g.: Happy, Introspective, Drunk).

.. **Original Year**

..    The original year that the track was released, as opposed to **Original Release Date** (the earliest release date of the entire Album).

.. .. note::

..    This plugin makes a large number of web services calls to get track-specific data, so loading a large number of albums and tracks could take a significant amount of time.

.. .. .. note::
.. ..
.. ..    Original Year does not seem to be working correctly at present.

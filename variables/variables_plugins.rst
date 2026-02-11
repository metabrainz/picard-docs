.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

:index:`Tags from Plugins <tags; plugins>`
==========================================

Plugins from Picard :doc:`Plugins <../config/options_plugins>` can add more tags. Following are some examples.

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

   Some plugins make a large number of web service calls to get additional track-specific data such as performer and work relationships, so loading a large number of albums and tracks could take a significant amount of time. The time concern can be partially addressed by operating a local MusicBrainz server with the rate limiting disabled. Please see the `MusicBrainz Server <https://github.com/metabrainz/musicbrainz-server>`_ project on GitHub for additional information.

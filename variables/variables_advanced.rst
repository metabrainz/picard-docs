.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard


.. Test Release 1

.. No extra relationships specified
.. https://musicbrainz.org/ws/2/release/8c759d7a-2ade-4201-abc2-a2a7c1a6ad6c?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups&fmt=json

.. Release extra relationships specified
.. https://musicbrainz.org/ws/2/release/8c759d7a-2ade-4201-abc2-a2a7c1a6ad6c?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups+artist-rels+recording-rels+release-group-level-rels+release-rels+series-rels+url-rels+work-rels&fmt=json

.. Track extra relationships specified
.. https://musicbrainz.org/ws/2/release/8c759d7a-2ade-4201-abc2-a2a7c1a6ad6c?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups+artist-rels+recording-rels+release-group-level-rels+release-rels+series-rels+url-rels+work-rels+recording-level-rels+work-level-rels&fmt=json


.. Test Release 2

.. No extra relationships specified
.. https://musicbrainz.org/ws/2/release/59f6dc82-6e05-4d58-8fae-d93c55a250ef?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups&fmt=json

.. Release extra relationships specified
.. https://musicbrainz.org/ws/2/release/59f6dc82-6e05-4d58-8fae-d93c55a250ef?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups+artist-rels+recording-rels+release-group-level-rels+release-rels+series-rels+url-rels+work-rels&fmt=json

.. Track extra relationships specified
.. https://musicbrainz.org/ws/2/release/59f6dc82-6e05-4d58-8fae-d93c55a250ef?inc=aliases+annotation+artist-credits+artists+collections+discids+isrcs+labels+media+recordings+release-groups+artist-rels+recording-rels+release-group-level-rels+release-rels+series-rels+url-rels+work-rels+recording-level-rels+work-level-rels&fmt=json


:index:`Advanced Variables <variables; advanced>`
=================================================

You can make additional tags available by enabling the :doc:`Use track relationships <../config/options_metadata>` and/or the
:doc:`Use release relationships <../config/options_metadata>` settings in Picard.

Some variables provide the :index:`MusicBrainz Identifier (MBID) <identifier; musicbrainz, mbid>` of the entity. The MBID is a 32-character identifier assigned to an entity (e.g.: artist, album, track or work) to uniquely identify the entity. For more information about MBIDs, please see the `MusicBrainz Identifier <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_ page in the MusicBrainz documentation.

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.


Release Relationship Variables
------------------------------

If you enable tagging with :doc:`Use release relationships <../config/options_metadata>`, you get these extra variables:

**_release_series**

   A multi-value variable containing the series titles associated with the release. (*since Picard 2.9*)

**_release_seriesid**

   A multi-value variable containing the series MBIDs associated with the release. (*since Picard 2.9*)

**_release_seriescomment**

   A multi-value variable containing the series disambiguation comments associated with the release. (*since Picard 2.9*)

**_release_seriesnumber**

   If the release is part of one of more series, this multi-value variable contains the positions (numbers) of the release in those series. (*since Picard 2.9*)

**_releasegroup_series**

   A multi-value variable containing the series titles associated with the release group. (*since Picard 2.9*)

**_releasegroup_seriesid**

   A multi-value variable containing the series MBIDs associated with the release group. (*since Picard 2.9*)

**_releasegroup_seriescomment**

   A multi-value variable containing the series disambiguation comments associated with the release group. (*since Picard 2.9*)

**_releasegroup_seriesnumber**

   If the release group is part of one of more series, this multi-value variable contains the positions (numbers) of the release group in those series. (*since Picard 2.9*)


Track Relationship Variables
----------------------------

If you enable tagging with :doc:`Use track relationships <../config/options_metadata>`, you get these extra variables:

**_broadcast_date**

   The date the recording was broadcast.

**_lyricistsort**

   The sort names of the lyricists for the work. (*since Picard 2.9*)

**_performance_attributes**

   List of performance attributes for the work (e.g.: "live", "cover", "medley"). Use :ref:`func_inmulti` to check for a specific type (i.e.: ``$if($inmulti(%_performance_attributes%,medley), (Medley),)``). (*since Picard 1.3*)

**_recordingtitle**

   Recording title - normally the same as the track title, but can be different.

**_recording_series**

   A multi-value variable containing the series titles associated with the recording. (*since Picard 2.9*)

**_recording_seriesid**

   A multi-value variable containing the series MBIDs associated with the recording. (*since Picard 2.9*)

**_recording_seriescomment**

   A multi-value variable containing the series disambiguation comments associated with the recording. (*since Picard 2.9*)

**_recording_seriesnumber**

   A multi-value variable containing the series numbers associated with the recording. (*since Picard 2.9*)

**_workcomment**

   The disambiguation comment associated with the work. (*since Picard 2.7*)

**_work_series**

   A multi-value variable containing the series titles associated with the work. (*since Picard 2.9*)

**_work_seriesid**

   A multi-value variable containing the series MBIDs associated with the work. (*since Picard 2.9*)

**_work_seriescomment**

   A multi-value variable containing the series disambiguation comments associated with the work. (*since Picard 2.9*)

**_work_seriesnumber**

   A multi-value variable containing the series numbers associated with the work. (*since Picard 2.9*)

**_writersort**

   The sort names of the writers for the work. (*since Picard 2.9*)

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


:index:`Advanced Tags <tags; advanced>`
=======================================

You can make additional tags available by enabling the :doc:`Use track relationships <../config/options_metadata>` and/or the :doc:`Use genres from MusicBrainz <../config/options_genres>` settings in Picard.

Some tags provide the :index:`MusicBrainz Identifier (MBID) <identifier; musicbrainz, mbid>` of the entity. The MBID is a 32-character identifier assigned to an entity (e.g.: artist, album, track or work) to uniquely identify the entity. For more information about MBIDs, please see the `MusicBrainz Identifier <https://musicbrainz.org/doc/MusicBrainz_Identifier>`_ page in the MusicBrainz documentation.

.. note::

   Tags will not be created and will not be available as variables if there was no value retrieved for the tag from the MusicBrainz database.

   Some of these tags are only supported for certain file types or tag formats. Please see the :doc:`Picard Tag Mapping <../appendices/tag_mapping>` section for details.


.. _advanced_relationships:


Track Relationship Tags
-----------------------

If you enable "Use track relationships" in the Option settings, you get these extra tags:

**arranger**

   The names of the arrangers associated with the track. These can include the instrument and orchestra arrangers, and could be associated with the release, recording or work. (*since Picard 0.10*)

**composer**

   The names of the composers for the associated work.

**composersort**

   The sort names of the composers for the associated work.

**conductor**

   The names of the conductors associated with the track. These can include the conductor and chorus master, and could be associated with the release or recording.

**director**

   The director of a track as provided by the *Video Director* or *Audio Director* relationship in MusicBrainz. (*Since Picard 2.6, updated in Picard 2.9*)

**djmixer**

   The names of the DJ mixers for the track. (*since Picard 0.9*)

**engineer**

   The names of the engineers associated with the track.

**language**

   Work lyric language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_ if a related work exists. (*since Picard 0.10*)

**license**

   The licenses associated with the track, either through the release or recording relationships. (*since Picard 1.0*)

**lyricist**

   The names of the lyricists for the associated work.

**mixer**

   The names of the "*Mixed By*" engineers associated with the track. (*since Picard 0.9*)

**musicbrainz_workid**

   The MBID for the Work if a related work exists.

**performer:<type>**

   The names of the performers for the specified type. These types include:

   - vocals or instruments for the associated release or recording, where <type> can be "*vocal*", "*guest guitar*", "*solo violin*", etc.

   - the orchestra for the associated release or recording, where <type> is "*orchestra*"

   - the concert master for the associated release or recording, where <type> is "*concertmaster*"

**producer**

   The names of the producers for the associated release or recording.

**remixer**

   The names of the remixer engineers associated with the track.

**work**

   The name of the work associated with the track. (*since Picard 1.3*)

**writer**

   A multi-value tag containing the names of the writers associated with the related work. (*since Picard 1.0*). This is not written to most file formats automatically. You can merge this with composers with a script like:

   .. code-block:: taggerscript

      $copymerge(composer, writer)

.. note::

   Some tags such as **performer** are available as both track and release level relationships, and the values may be different depending on which relationship options are enabled.


.. _genre_settings:

:index:`Genre Tags <tags; genre>`
---------------------------------

If you enable "Use genres from MusicBrainz", you get:

**genre**

   A multi-value tag containing the specified genre information from MusicBrainz (*since Picard 2.1, earlier versions used folksonomy tags*)

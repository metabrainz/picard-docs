.. MusicBrainz Picard Documentation Project

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

:index:`Advanced Tags <tags; advanced>`
========================================

You can make additional tags available by enabling the :doc:`Use track relationships </config/options_metadata>` and the
:doc:`Use genres from MusicBrainz </config/options_genres>` settings in Picard.

.. note::

   Tags will not be created and will not be available as variables if there was no value retrieved for the tag
   from the MusicBrainz database.

.. note::

   Some of these tags are only supported for certain file types or tag formats.  Please see the :doc:`Picard Tag Mapping
   </appendices/tag_mapping>` section for details.

.. _advanced_relationships:

Track Relationship Tags
--------------------------
If you enable tagging with "Use track relationships", you get these extra tags:

**arranger**

    The names of the arrangers associated with the track.  These can include the instrument and orchestra arrangers,
    and could be associated with the release, recording or work. (*since Picard 0.10*)

**composer**

    The names of the composers for the associated work.

**composersort**

    The sort names of the composers for the associated work.

**conductor**

    Tha names of the conductors associated with the track.  These can include the conductor and chorus master, and could
    be associated with the release or recording.

**director**

   The director of a track as provided by the Video Director or Audio Director relationship in MusicBrainz.  (*Since Picard 2.6, updated in Picard 2.9*)

**djmixer**

    The names of the DJ mixers for the track. (*since Picard 0.9*)

**engineer**

    The names of the engineers associated with the track.

**license**

    The licenses associated with the track, either through the release or recording relationships. (*since Picard 1.0*)

**lyricist**

    The names of the lyricists for the associated work.

**mixer**

    The names of the "Mixed By" engineers associated with the track. (*since Picard 0.9*)

**performer:<type>**

    The names of the performers for the specified type.  These types include:

    - vocals or instruments for the associated release or recording, where <type> can be "vocal", "guest guitar", "solo violin", etc.

    - the orchestra for the associated release or recording, where <type> is "orchestra"

    - the concert master for the associated release or recording, where <type> is "concertmaster"

**producer**

    The names of the producers for the associated release or recording.

**releasedate**

    Explicit tag for the release date (*since Picard 2.9*).  This tag exists for specific use in scripts and plugins,
    but is not filled by default.  In most cases it is recommended to use the ``date`` tag instead for compatibility
    with existing software.

**remixer**

    The names of the remixer engineers associated with the track.

**work**

    The name of the work associated with the track. (*since Picard 1.3*)

**writer**

    The names of the writers associated with the related work. (*since Picard 1.0*). This is not written to most file formats automatically.
    You can merge this with composers with a script like:

    .. code-block:: taggerscript

        $copymerge(composer, writer)

.. _genre_settings:

:index:`Genre Tags <tags; genre>`
----------------------------------

If you enable "Use genres from MusicBrainz", you get:

**genre**

    Genre information from MusicBrainz (*since Picard 2.1, earlier versions used folksonomy tags*)

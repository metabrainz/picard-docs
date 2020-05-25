..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Advanced Tags
=============

.. index::
   single: tags; advanced

You can make additional tags available by enabling the :ref:`Advanced Relationships <advanced_relationships>` and the
:ref:`Use genres from MusicBrainz <genre_settings>` settings in Picard.

.. note::

   Tags will not be created and will not be available as variables if there was no value retrieved for the tag
   from the MusicBrainz database.

.. note::

   Some of these tags are only supported for certain file types or tag formats.  Please see the `Picard Tag Mapping
   <https://picard.musicbrainz.org/docs/mappings/>`_ webpage for details.

.. _advanced_relationships:

Advanced Relationship Tags
--------------------------
If you enable tagging with Advanced Relationships, you get these extra tags:

**arranger**

    Arranger Relationship Type (releases, recordings, works), Instrumentator Relationship Type, Orchestrator Relationship Type (*since Picard 0.10*)

**composer**

    Composer Relationship Type

**composersort**

    Composer Relationship Type's Sort Name

**conductor**

    Conductor Relationship Type (releases, recordings), Chorus Master Relationship Type (releases, recordings)

**djmixer**

    Mix-DJ Relationship Type (*since Picard 0.9*)

**engineer**

    Engineer Relationship Type

**license**

    License Relationship Type (releases, recordings) (*since Picard 1.0*)

**lyricist**

    Lyricist Relationship Type

**mixer**

    Engineer Relationship Type ("Mixed By") (*since Picard 0.9*)

**performer:<type>**

    Performer Relationship Type (releases - vocals/instruments, recordings - vocals/instruments), <type> can be "vocal", "guest guitar", "solo violin", …

    Orchestra Relationship Type (releases, recordings), <type> is "orchestra"

    Concertmaster Relationship Type (releases, recordings), <type> is "concertmaster"

**producer**

    Producer Relationship Type

**remixer**

    Remixer Relationship Type

**work**

    Work Name (*since Picard 1.3*)

**writer**

    Writer Relationship Type (*since Picard 1.0*). Not written to most file formats automatically.
    You can merge this with composers with a script like::

        $copymerge(composer, writer)

.. _genre_settings:

.. index::
   single: tags; genre

Genre Tags
----------
If you enable Use genres from MusicBrainz, you get:

**genre**

    Genre information from MusicBrainz (*since Picard 2.1, earlier versions used folksonomy tags*)

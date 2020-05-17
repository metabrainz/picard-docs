..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

Tags from Plugins
=================

Plugins from Picard :doc:`Plugins <../config/options_plugins>` can add more tags.  Following are two popular examples.

Last.fm
-------

**genre**

   Pseudo-genre based on folksonomy tags.


Last.fm Plus
------------

The LastFMPlus plugin is a sophisticated plugin that tries to provide stable and meaningful genre selections from the ever-changing and
idiosyncratic list provided by lastFM.

The LastFMPlus plugin is very configurable and examples provided here are based on the default lists provided on the Tag Filter List tab
of the LastFMPlus options page.

**Comment:songs-db_Custom1**

   The decade (e.g.: 1970s).

**Comment:songs-db_Custom2**

   Category (e.g.: Female Vocalist, Singer-Songwriter).

**Comment:songs-db_Custom3**

   Country (e.g.: British).

**Comment:songs-db_Occassion**

   Good situations to play a track (e.g.: Driving, Love, Party).

**genre**

   Specific detailed genres. For example, if the group is Rock the genre could be one of Acid rock, Acoustic rock, Alternative metal,
   Alternative rock, Art rock, Blues rock, Boogie rock, Brit rock, Christian rock, College rock, Country rock, etc.

**grouping**

   Top-level genres - default list: Audiobooks, Blues, Classic rock, Classical, Country, Dance, Electronica, Folk, Hip-hop, Indie, Jazz,
   Kids, Metal, Pop, Punk, Reggae, Rock, Soul, Trance

**mood**

   How a track "feels" (e.g.: Happy, Introspective, Drunk).

**Original Year**

   The original year that the track was released, as opposed to **Original Release Date** (the earliest release date of the entire Album).

.. note::

   This plugin makes a large number of web services calls to get track-specific data, so loading a large number of albums and tracks could take a significant amount of time.

.. .. note::
..
..    Original Year does not seem to be working correctly at present.

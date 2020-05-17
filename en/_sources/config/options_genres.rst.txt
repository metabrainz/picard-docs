..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Genres
======

.. image:: ../images/options-metadata-genres.png
   :width: 100 %

**Use genres from MusicBrainz**

   Use genres provided by MusicBrainz and save them to the genre tag.

**Fall back on album's artists genres if no genres are found for the release or release group**

   If there is no genre set for the release or release group on MusicBrainz, use the genre of the album artist instead.

**Only use my genres**

   When enabled, Picard will only write genres you personally have submitted to MusicBrainz. You'll need to set your username
   and password to use this feature.

**Use folksonomy tags as genres**

   Check to use all folksonomy tags to set the genre. Otherwise only the tags considered by MusicBrainz to be proper genres
   will be used.

**Minimal genre usage**

   Choose how popular the genre must be before it is written by Picard. Default: 90%. Lowering the value here will lead to
   more, but possibly less relevant, genres in your files.

**Maximum number of genres**

   Choose how many genres to use. Default: 5. If you only want a single genre, set this to 1.

**Join multiple genres with**

   Select which character should be used to separate multiple genres.

**Genres or folksonomy tags to include or exclude**

   One expression per line, case-insensitive. You can use the "Playground" text field to enter some genres and test the rules
   you have setup. Genres that will be excluded will be marked red, included genres will be marked green.

   * **Comments**: Lines not starting with '-' or '+' are ignored. (e.g.: ``#comment``, ``!comment`` or ``comment``)

   * **Strict filtering**: Exclude exact word by prefixing it with '-' (e.g.: ``-word``).  Include exact word, even if another
     rule would exclude it, by prefixing it with '+' (e.g.: ``+word``).

   * **Wildcard filtering**: Exclude all genres ending with "word" (e.g.: ``-*word``).  Include all genres starting with "word"
     (e.g.: ``+word*``).  Exclude all genres starting with 'w' and ending with "rd" (e.g.: ``-w*rd``).

   * **Regular expressions filtering (Python "re" syntax)**: Exclude genres starting with 'w' followed by any character, then
     'r' followed by at least one 'd' (e.g.: ``-/^w.rd+/``).

**Playground for genres or folksonomy tags filters:**

   This area allows you to enter genre tags, one per line, to test your filters.  If a tag is marked in red, it will be filtered
   out.  A tag marked green will be allowed.

   .. note::

      This list of test tags will be cleared when you exit the configuration section.

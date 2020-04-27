..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Metadata Options
================

**Translate artist names to this locale where possible**

   When checked, Picard will see whether an artist has an alias for the selected locale. If it does, Picard will use that
   alias instead of the artist name when tagging. When "English" is the selected locale, the artist sort name (which is,
   by Style Guideline, stored in Latin script) is used as a fallback if there is no English alias.

**Use standardized artist names**

   Check to only use standard Artist names, rather than Artist Credits which may differ slightly across tracks and releases.

   Note: If the "Translate artist names" option above is also checked, it will override this option if a suitable alias is found.

**Use standardized instrument and vocal credits**

   Check to only use standard names for instruments and vocals in performer relationships. Uncheck to use the instruments
   and vocals as credited in the relationship.

**Convert Unicode punctuation characters to ASCII**

   Converts Unicode punctuation characters in MusicBrainz data to ASCII for consistent use of punctuation in tags. For example,
   right single quotation marks are converted to ASCII apostrophes ('), and horizontal ellipses are converted to three
   full stops (...).

**Use release relationships**

   Check to retrieve and write release-level relationships (e.g.: URLs, composer, lyricist, performer, conductor, or DJ mixer)
   to your files. You must have this enabled to use Picard to retrieve cover art.

**Use track relationships**

   Check to write track-level relationships (e.g.: composer, lyricist, performer, or remixer) to your files.

**Various artists**

   Choose how you want the "Various Artists" artist spelled.

**Non-album tracks**

   Choose how you want "non-album tracks" to be grouped.


Preferred Releases
------------------

**Preferred release types**

   Adjust the sliders for various release types to tweak how likely Picard is to match a file or cluster to releases of various
   types. For example, you can use this to decrease the likelihood of Picard matching a file or album to a Compilation or Live
   version.

**Preferred release countries**

   Add one or more countries into the list to make Picard prefer matching clusters or files to releases from the chosen countries.
   This list is also used to prioritize files in the "Other Releases" context menu.

**Preferred release formats**

   Add one or more formats into the list to make Picard prefer matching clusters or files to releases of the specified format.
   This list is also used to prioritize files in the "Other Releases" context menu.


Genres
------

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


Ratings
-------

**Enable track ratings**

   Check to write track ratings to your files.

**E-mail**

   The email address used when submitting ratings to MusicBrainz.  This identifies the user that provided the rating.

**Submit ratings to MusicBrainz**

   Check to submit ratings to MusicBrainz. The tracks will be rated with your account.

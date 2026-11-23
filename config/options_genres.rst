.. MusicBrainz Picard Documentation Project

:index:`Genres <configuration; genres>`
=======================================

.. only:: not latex

   .. image:: images/options-metadata-genres.png
      :align: center

.. only:: latex

   .. image:: images/options-metadata-genres.png
      :width: 70%
      :align: center

.. _opt_genres_use_genres_from_musicbrainz:

**Use genres from MusicBrainz**

   Use genres provided by MusicBrainz and save them to the genre tag.

.. _opt_genres_only_use_my_genres:

**Only use my genres**

   When enabled, Picard will only write genres you personally have submitted to MusicBrainz. You'll need to set your username and password to use this feature.

.. _opt_genres_fall_back_to_album_artists_genres:

**Fall back to album's artists genres**

   If there is no genre set for the release or release group on MusicBrainz, use the genre of the album artist instead.

.. _opt_genres_use_folksonomy_tags_as_genre:

**Use folksonomy tags as genre**

   Check to use all folksonomy tags to set the genre. Otherwise only the tags considered by MusicBrainz to be proper genres will be used.

.. _opt_genres_minimal_genre_usage:

**Minimal genre usage**

   Choose how popular the genre must be before it is written by Picard. Default: 90%. Lowering the value here will lead to more, but possibly less relevant, genres in your files.

.. _opt_genres_maximum_number_of_genres:

**Maximum number of genres**

   Choose how many genres to use. Default: 5. If you only want a single genre, set this to 1.

.. _opt_genres_join_multiple_genres_with:

**Join multiple genres with**

   Select which character should be used to separate multiple genres.

.. _opt_genres_genres_or_folksonomy_tags_to_include:

**Genres or folksonomy tags to include or exclude**

   One expression per line, case-insensitive. You can use the "Playground" text field to enter some genres and test the rules you have setup. Genres that will be excluded will be marked red, included genres will be marked green.

   * **Comments**: Lines not starting with '-' or '+' are ignored. (e.g.: ``#comment``, ``!comment`` or ``comment``)

   * **Strict filtering**: Exclude exact word by prefixing it with '-' (e.g.: ``-word``). Include exact word, even if another rule would exclude it, by prefixing it with '+' (e.g.: ``+word``).

   * **Wildcard filtering**: Exclude all genres ending with "word" (e.g.: ``-*word``). Include all genres starting with "word" (e.g.: ``+word*``). Exclude all genres starting with 'w' and ending with "rd" (e.g.: ``-w*rd``).

   * **Regular expressions filtering (Python "re" syntax)**: Exclude genres starting with 'w' followed by any character, then 'r' followed by at least one 'd' (e.g.: ``-/^w.rd+/``).

**Playground for genres or folksonomy tags filters:**

   This area allows you to enter genre tags, one per line, to test your filters. If a tag is marked in red, it will be filtered out. A tag marked green will be allowed.

   .. note::

      This list of test tags will be cleared when you exit the configuration section.

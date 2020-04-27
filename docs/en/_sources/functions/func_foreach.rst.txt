..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$foreach
========

| Usage: **$foreach(name,code,separator="; ")**
| Category: loop
| Implemented: Picard 2.3

**Description:**

Iterates over each element found in the multi-value variable ``name``, executing ``code`` during
each iteration. Before each iteration, the element value is first stored in the variable
``_loop_value`` and the count is stored in the variable ``_loop_count``. This allows the element
or count value to be accessed within the code script.

A literal value representing a multi-value can be substituted for ``name``, using the ``separator``
(or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued
variable.


**Example:**

The following statements will perform the processing indicated::

    $noop( Mark all listed tags for deletion from the files. )
    $foreach(genre; comment; year,$delete(%_loop_value%))

    $noop( Create an 'artist_count' tag with a count of all artists
           listed for the track. )
    $foreach(%artists%,$set(artist_count,%_loop_count%))

    $noop( Create a separate tag for each artist listed for the
           track as 'artist_1', 'artist_2', etc. )
    $foreach(%artists%,$set(artist_%_loop_count%,%_loop_value%))

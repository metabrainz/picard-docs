..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$firstwords
===========

| Usage: **$firstwords(text,length)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Truncate ``text`` to ``length``, only returning the complete words from ``text`` which fit
within ``length`` characters.  If ``length`` is less than 0, then the value used is the number
of characters in ``text`` plus ``length`` (e.g.: ``$firstwords(one two three,-3)`` is the same
as ``$firstwords(one two three,10)``).  If ``length`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $firstwords(Once upon a time,)     ==>  ""
    $firstwords(Once upon a time,0)    ==>  ""
    $firstwords(Once upon a time,3)    ==>  ""
    $firstwords(Once upon a time,7)    ==>  "Once"
    $firstwords(Once upon a time,-3)   ==>  "Once upon a"
    $firstwords(Once upon a time,-30)  ==>  ""

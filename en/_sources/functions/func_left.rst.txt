..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$left
=====

| Usage: **$left(text,num)**
| Category: text

**Description:**

Returns the first ``num`` characters from ``text``.  If ``num`` is less than 0, then the
value used is the number of characters in ``text`` plus ``num`` (e.g.: ``$right(abcd,-1)``
is the same as ``$right(abcd,3)``).  If ``num`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $left(,)       ==>  ""
    $left(ABC,)    ==>  ""
    $left(ABC,0)   ==>  ""
    $left(ABC,2)   ==>  "AB"
    $left(ABC,4)   ==>  "ABC"
    $left(ABC,-2)  ==>  "A"
    $left(ABC,-4)  ==>  ""

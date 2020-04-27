..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$truncate
=========

| Usage: **$truncate(text,length)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Truncate ``text`` to ``length``.  If ``length`` is less than 0, then the value used
is the number of characters in ``text`` plus ``length`` (e.g.: ``$truncate(abcd,-1)``
is the same as ``$truncate(abcd,3)``).  If ``length`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $truncate(Once upon a time,)     ==>  ""
    $truncate(Once upon a time,0)    ==>  ""
    $truncate(Once upon a time,3)    ==>  "Onc"
    $truncate(Once upon a time,-3)   ==>  "Once upon a t"
    $truncate(Once upon a time,-30)  ==>  ""

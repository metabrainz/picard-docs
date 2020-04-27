..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$gte
====

| Usage: **$gte(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` is greater than or equal to ``y``.  If an argument is missing or is
not an integer, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $gte(-1,0)   ==>  ""   (False)
    $gte(0,0)    ==>  "1"  (True)
    $gte(1,0)    ==>  "1"  (True)
    $gte(,)      ==>  ""   (False)
    $gte(,0)     ==>  ""   (False)
    $gte(0,)     ==>  ""   (False)
    $gte(a,1)    ==>  ""   (False)
    $gte(1,a)    ==>  ""   (False)
    $gte(1,1.5)  ==>  ""   (False)

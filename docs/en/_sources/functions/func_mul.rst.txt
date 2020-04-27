..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$mul
====

| Usage: **$mul(x,y,\*args)**
| Category: mathematical

**Description:**

Multiplies x by y. Can be used with an arbitrary number of arguments (i.e.:
``$mul(x,y,z)`` = (x \* y) \* z). If an argument is empty or not an integer,
the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $mul(1,2)      ==> "2"
    $mul(1,2,3)    ==> "6"
    $mul(1,2,0)    ==> "0"
    $mul(1,-2,3)   ==> "-6"
    $mul(-1,2,-3)  ==> "6"
    $mul(1,2,)     ==> ""
    $mul(1,2,x)    ==> ""
    $mul(1,2.5)    ==> ""

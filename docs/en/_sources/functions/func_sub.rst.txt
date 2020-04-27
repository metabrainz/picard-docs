..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$sub
====

| Usage: **$sub(x,y,\*args)**
| Category: mathematical

**Description:**

Subtracts ``y`` from ``x``. Can be used with an arbitrary number of arguments (i.e.: ``$sub(x,y,z)`` = (x - y) - z).
Returns an empty string if an argument is missing or not an integer.


**Example:**

The following statements will return the values indicated::

    $sub(20,15)      ==>  "5"
    $sub(20,-15)     ==>  "35"
    $sub(20,14,1)    ==>  "5"
    $sub(20,10,3,2)  ==>  "5"
    $sub(20,10,3,)   ==>  ""
    $sub(20,10,3,a)  ==>  ""
    $sub(20,10,3.5)  ==>  ""

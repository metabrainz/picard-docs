..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$or
===

| Usage: **$or(x,y,\*args)**
| Category: conditional

**Description:**

Returns true if either ``x`` or ``y`` is not empty. Can be used with an arbitrary number
of arguments. The result is true if **ANY** of the arguments is not empty.


**Example:**

The following statements will return the values indicated::

    $or(,)          ==>  ""   (False)
    $or(,1)         ==>  "1"  (True)
    $or(,A)         ==>  "1"  (True)
    $or(,$gt(4,5))  ==>  ""   (False)
    $or(,$lt(4,5))  ==>  "1"  (True)
    $or(,,)         ==>  ""   (False)
    $or(,,0)        ==>  "1"  (True)
    $or(,, )        ==>  "1"  (True)

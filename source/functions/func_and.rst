..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$and
====

| Usage: **$and(x,y,\*args)**
| Category: conditional

**Description:**

Returns true if both ``x`` and ``y`` are not empty. Can be used with an arbitrary number
of arguments. The result is true if **ALL** of the arguments are not empty.


**Example:**

The following statements will return the values indicated::

    $set(test,x)
    $and(%test%,)          ==>  ""   (False)
    $and(%test%,1)         ==>  "1"  (True)
    $and(%test%,A)         ==>  "1"  (True)
    $and(%test%,$gt(4,5))  ==>  ""   (False)
    $and(%test%,$lt(4,5))  ==>  "1"  (True)
    $and(%test%,,)         ==>  ""   (False)
    $and(%test%,,0)        ==>  ""   (False)
    $and(%test%,, )        ==>  ""   (False)
    $and(%test%, , )       ==>  "1"  (True)

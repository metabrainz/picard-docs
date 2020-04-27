..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$eq
===

| Usage: **$eq(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` equals ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $eq(,a)   ==>  ""   (False)
    $eq(a,)   ==>  ""   (False)
    $eq(a,A)  ==>  ""   (False)
    $eq(a,a)  ==>  "1"  (True)

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$ne
===

| Usage: **$ne(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $ne(,a)   ==>  "1"  (True)
    $ne(a,)   ==>  "1"  (True)
    $ne(a,A)  ==>  "1"  (True)
    $ne(a,a)  ==>  ""   (False)

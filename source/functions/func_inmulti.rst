..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$inmulti
========

| Usage: **$inmulti(%x%,y)**
| Category: conditional
| Implemented: Picard 1.0

**Description:**

Returns true if multi-value variable ``x`` contains exactly ``y`` as one of its values.
Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $setmulti(foo,One; Two; Three)
    $set(bar,Two)
    $inmulti(%foo%,%bar%)  ==>  "1"  (True)
    $inmulti(%foo%,Two)    ==>  "1"  (True)
    $inmulti(%foo%,two)    ==>  ""   (False)
    $inmulti(%foo%,Once)   ==>  ""   (False)
    $inmulti(%foo%,w)      ==>  ""   (False)
    $inmulti(%foo%,)       ==>  ""   (False)

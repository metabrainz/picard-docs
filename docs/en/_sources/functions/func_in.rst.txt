..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$in
===

| Usage: **$in(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true, if ``x`` contains ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $set(foo,ABCDEFG)
    $set(bar,CDE)
    $in(%foo%,%bar%)  ==>  "1"  (True)
    $in(ABCDE,CDE)    ==>  "1"  (True)
    $in(ABCDE,CE)     ==>  ""   (False)
    $in(ABCDE,cde)    ==>  ""   (False)
    $in(ABCDE,)       ==>  "1"  (True)
    $in(,)            ==>  "1"  (True)

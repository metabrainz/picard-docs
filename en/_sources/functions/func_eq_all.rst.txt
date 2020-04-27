..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$eq_all
=======

| Usage: **$eq_all(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` equals ``a1`` and ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$and($eq(x,a1),$eq(x,a2) ...)``.


**Example:**

The following statements will return the values indicated::

    $eq_all(A,A,B,C)    ==>  ""   (False)
    $eq_all(A,a,A,A)    ==>  ""   (False)
    $eq_all(A,A,A,A)    ==>  "1"  (True)
    $eq_all(,,,)        ==>  "1"  (True)
    $eq_all(,a,)        ==>  ""   (False)

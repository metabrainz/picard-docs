..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$ne_any
=======

| Usage: **$ne_any(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``a1`` or ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$or($ne(x,a1),$ne(x,a2) ...)``.


**Example:**

The following statements will return the values indicated::

    $ne_any(A,A,B,C)    ==>  "1"  (True)
    $ne_any(A,a,A,A)    ==>  "1"  (True)
    $ne_any(A,A,A,A)    ==>  ""   (False)
    $ne_any(,,,)        ==>  ""   (False)
    $ne_any(,a,,)       ==>  "1"  (True)

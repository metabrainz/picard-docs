..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$getmulti
=========

| Usage: **$getmulti(name,index[,separator])**
| Category: multi-value
| Implemented: Picard 2.3

**Description:**

Gets the element at ``index`` from the multi-value variable ``name``. A literal value
representing a multi-value can be substituted for ``name``, using the ``separator``
(or a semicolon followed by a space "; " if not passed) to coerce the value into a
proper multi-value variable.

The ``index`` is zero based.   If ``index`` is less than 0, then the
value used is the number of elements in ``name`` plus ``index`` (e.g.: ``$getmulti(%abcd%,-1)``
is the same as ``$getmulti(%abcd%,3)`` if ``%abcd%`` is a multi-value variable with four
elements).  If ``index`` is missing, not an integer, a number greater than or equal to the
number of elements in ``name``, or a negative number greater than the number of elements in
``name``, then the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $set(foo,A; B; C)
    $setmulti(bar,A; B; C)
    $set(baz,1)
    $getmulti(%foo%,%baz%)        ==>  ""
    $getmulti(%foo%,0)            ==>  "A; B; C"
    $getmulti(%foo%,-1)           ==>  "A; B; C"
    $getmulti(%foo%,-%baz%)       ==>  "A; B; C"
    $getmulti(%bar%,%baz%)        ==>  "B"
    $getmulti(%bar%,0)            ==>  "A"
    $getmulti(%bar%,-1)           ==>  "C"
    $getmulti(%bar%,-%baz%)       ==>  "C"

    $getmulti(A:1; B:2; C:3,1)    ==>  "B:2"
    $getmulti(A:1; B:2; C:3,1,:)  ==>  "1; B"
    $getmulti(A:1; B:2; C:3,10)   ==>  ""
    $getmulti(A:1; B:2; C:3,-10)  ==>  ""
    $getmulti(A:1; B:2; C:3,1.5)  ==>  ""
    $getmulti(A:1; B:2; C:3,a)    ==>  ""

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$join
=====

| Usage: **$join(name,text[,separator])**
| Category: multi-value
| Implemented: Picard 2.3

**Description:**

Joins all elements in the multi-value variable ``name``, placing ``text`` between each
element, and returns the result as a string.   A literal value representing a multi-value
can be substituted for ``name``, using the ``separator`` (or a semicolon followed by a
space "; " if not passed) to coerce the value into a proper multi-valued variable.


**Example:**

The following statements will return the values indicated::

    $set(foo,First:A; Second:B)
    $join(%foo%, >> )                     ==>  "First:A; Second:B"
    $join(%foo%, >> ,:)                   ==>  "First >> A; Second >> B"

    $setmulti(bar,First:A; Second:B)
    $join(%bar%, >> )                     ==>  "First:A >> Second:B"
    $join(%bar%, >> ,:)                   ==>  "First >> A; Second >> B"

    $join(First:A; Second:B,)             ==>  "First:ASecond:B"
    $join(First:A; Second:B, >> )         ==>  "First:A >> Second:B"
    $join(First:A; Second:B, >> ,:)       ==>  "First >> A; Second >> B"

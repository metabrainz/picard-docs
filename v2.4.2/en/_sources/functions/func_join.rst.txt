.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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

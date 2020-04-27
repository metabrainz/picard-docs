..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$firstalphachar
===============

| Usage: **$firstalphachar(text[,nonalpha])**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of ``text`` in upper case. If ``text`` does not begin with an
alphabetic character, then ``nonalpha`` is returned instead.  If ``nonalpha`` is not specified,
the default value "#" will be used.


**Example:**

The following statements will return the values indicated::

    $firstalphachar(abc)             ==>  "A"
    $firstalphachar(123)             ==>  "#"
    $firstalphachar(***)             ==>  "#"
    $firstalphachar(***,)            ==>  ""
    $firstalphachar(***,^)           ==>  "^"
    $firstalphachar(***,non-alpha)   ==>  "non-alpha"

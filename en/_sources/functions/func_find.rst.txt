..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$find
=====

| Usage: **$find(haystack,needle)**
| Category: text
| Implemented: Picard 2.3

**Description:**

Returns the zero-based index of the first occurrance of ``needle`` in ``haystack``, or
an empty string if ``needle`` was not found.  The comparisons are case-sensitive. If ``needle`` is
blank, it will match the begging of ``haystack`` and return "0". The function does not
support wildcards.

Note that prior to Picard 2.3.2 ``$find`` returned "-1" if ``needle`` was not found.


**Example:**

The following statements will return the values indicated::

    $find(abcdef,a)     ==>  "0"
    $find(abcdef,c)     ==>  "2"
    $find(abcdef,cd)    ==>  "2"
    $find(abcdef,g)     ==>  ""
    $find(abcdef,B)     ==>  ""
    $find(,a)           ==>  ""
    $find(abcdef,)      ==>  "1"

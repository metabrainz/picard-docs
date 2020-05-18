..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$swapprefix
===========

| Usage: **$swapprefix(text[,prefixes])**
| Category: text
| Implemented: Picard 1.3 (*previously as a plugin since Picard 0.13*)

**Description:**

Moves the specified ``prefixes`` from the beginning to the end of ``text``. Any number of ``prefixes``
can be specified, separated by commas. If no prefix is specified "A" and "The" are used by default.
Note that the matching is case-sensitive.


**Example:**

If the ``albumartist`` is "Le Butcherettes", the following statements will return the values indicated::

    $swapprefix(%albumartist%)               ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,le)            ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,L)             ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,A,An,The,Le)   ==>  "Butcherettes, Le"

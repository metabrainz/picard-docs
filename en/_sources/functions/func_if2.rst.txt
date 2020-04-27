..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$if2
====

| Usage: **$if2(a1,a2,a3,...)**
| Category: conditional

**Description:**

Returns the first non empty argument.  Can be used with an arbitrary number of arguments.


**Example:**

The following statements will return the values indicated::

    $set(foo,)
    $set(bar,Something)
    $if2(%foo%,%bar%,Three)    ==>  "Something"
    $if2(,%bar%,Three)         ==>  "Something"
    $if2(,%foo%,%bar%,Three)   ==>  "Something"
    $if2(%foo%, ,%bar%,Three)  ==>  " "
    $if2(%foo%.,%bar%,Three)   ==>  "."
    $if2(%foo%,,Three)         ==>  "Three"
    $if2(%foo%,,,)             ==>  ""

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$num
====

| Usage: **$num(num,len)**
| Category: text

**Description:**

Returns ``num`` formatted to ``len`` digits, where ``num`` and ``len`` are integers and
``len`` cannot be greater than 20.


**Example:**

The following statements will return the values indicated::

    $num(,)        ==>  ""
    $num(,1)       ==>  "0"
    $num(a,)       ==>  ""
    $num(a,5)      ==>  "00000"
    $num(123,5)    ==>  "00123"
    $num(1.23,5)   ==>  "00000"
    $num(123,)     ==>  ""
    $num(123,0)    ==>  "123"
    $num(123,1)    ==>  "123"
    $num(123,20)   ==>  "00000000000000000123"
    $num(123,50)   ==>  "00000000000000000123"
    $num(123,5.5)  ==>  ""
    $num(1.23,10)  ==>  "0000000000"

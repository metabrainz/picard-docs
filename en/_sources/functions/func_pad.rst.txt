..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$pad
====

| Usage: **$pad(text,length,char)**
| Category: text

**Description:**

Pads the ``text`` to the ``length`` provided by adding as many copies of ``char`` as needed to
the beginning of the string.  For the padded length to be correct, ``char`` must be exactly one
character in length.  If ``length`` is less than the number of characters in ``text``, the
function will return ``text``.  If ``length`` is missing or is not a number, the function will
return an empty string.


**Example:**

The following statements will return the values indicated::

    $pad(abc,5,+)   ==>  "++abc"
    $pad(abc,0,+)   ==>  "abc"
    $pad(abc,5,)    ==>  "abc"
    $pad(abc,5,XY)  ==>  "XYXYabc"  (note final length is incorrect)
    $pad(abc,,+)    ==>  ""
    $pad(abc,x,+)   ==>  ""

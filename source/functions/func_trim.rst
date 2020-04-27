..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$trim
=====

| Usage: **$trim(text[,char])**
| Category: text

**Description:**

Trims all leading and trailing whitespaces from ``text``. The optional second parameter ``char``
specifies the character to trim.  If multiple characters are provided in ``char``, each character
will be applied separately to the function.


**Examples:**

The following statements will return the values indicated::

    $trim(  Trimmed  )       ==>  "Trimmed"
    $trim(__Trimmed__,_)     ==>  "Trimmed"
    $trim(x__Trimmed__y,_x)  ==>  "Trimmed__y"

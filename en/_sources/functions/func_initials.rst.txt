..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$initials
=========

| Usage: **$initials(text)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of each word in ``text``, if it is an alphabetic character.


**Example:**

The following statements will return the values indicated::

    $set(foo,This is a test)
    $initials(%foo%)               ==>  "Tiat"
    $initials(This is a test)      ==>  "Tiat"
    $initials(This is a 123 test)  ==>  "Tiat"

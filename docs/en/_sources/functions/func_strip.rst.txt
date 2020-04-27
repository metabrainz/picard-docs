..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$strip
======

| Usage: **$strip(text)**
| Category: text

**Description:**

Replaces all whitespace in ``text`` with a single space, and removes leading and trailing spaces.
Whitespace characters include multiple consecutive spaces, and various other unicode characters.
Characters such as newlines '\\n', tabs '\\t' and returns '\\r' are treated as spaces.


**Example:**

The following statements will each return "This text has been stripped."::

    $strip(This text has been stripped.)
    $strip(This text has been stripped.  )
    $strip(  This text has been stripped.  )
    $strip(  This  text has been stripped.)
    $strip(  This  text has been stripped.  )
    $strip(This  text  has  been  stripped.)
    $strip(This  text\rhas\nbeen\tstripped.)

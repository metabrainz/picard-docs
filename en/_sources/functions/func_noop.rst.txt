..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$noop
=====

| Usage: **$noop(...)**
| Category: miscellaneous

**Description:**

Does nothing and always returns an empty string.  This is useful for comments or disabling a block of code.


**Example:**

The following statements will return the values indicated::

    $noop( A comment. )          ==>  ""
    $noop($set(foo,Testing...))  ==>  "" (and "foo" is not set)

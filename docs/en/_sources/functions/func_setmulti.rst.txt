..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$setmulti
=========

| Usage: **$setmulti(name,value[,separator])**
| Category: assignment
| Implemented: Picard 1.0

**Description:**

Sets the variable ``name`` to ``value``, using the ``separator`` (or a semicolon
followed by a space "; " if not passed) to coerce the ``value`` back into a proper
multi-valued variable. This can be used to operate on multi-valued variables as a string,
and then set them back as proper multi-valued variable.


**Example:**

The following statements will return the values indicated::

    $setmulti(genre,$lower(%genre%))  ==>  all "genre" elements in lower case
    $setmulti(alpha,A; B; C)          ==>  3 elements ("A", "B" and "C")
    $setmulti(mixed,A:A; B:B,:)       ==>  3 elements ("A", "A; B" and "B")

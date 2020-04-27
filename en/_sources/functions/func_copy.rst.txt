..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$copy
=====

| Usage: **$copy(target,source)**
| Category: assignment
| Implemented: Picard 0.9

**Description:**

Copies metadata from variable ``source`` to ``target``. The difference from ``$set(target,%source%)`` is
that ``$copy(target,source)`` copies multi-value variables without flattening them.

Note that if the variable ``target`` already exists, it will be overwritten by ``source``.


**Example:**

The following statements will yield the values for ``target`` as indicated::

    $set(source,)
    $set(target,This will be overwritten)
    $copy(target,source)                   ==>  ""

    $set(source,one)
    $copy(target,source)                   ==>  "one"

    $setmulti(source,one)
    $copy(target,source)                   ==>  "one"

    $setmulti(source,one; two)
    $copy(target,source)                   ==>  "one; two"

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$copymerge
==========

| Usage: **$copymerge(target,source)**
| Category: assignment
| Implemented: Picard 1.0

**Description:**

Merges metadata from variable ``source`` into ``target``, removing duplicates and appending to the end,
so retaining the original ordering. Like ``$copy``, this will also copy multi-valued variables
without flattening them.  Following the operation, ``target`` will be a multi-value variable.

Note that the variable names for ``target`` and ``source`` are passed directly without enclosing them
in percent signs '%'.


**Example:**

The following statements will yield the values for ``target`` as indicated::

    $set(target,)
    $set(source,one)
    $copymerge(target,source)     ==>  "one"

    $set(target,zero)
    $set(source,one)
    $copymerge(target,source)     ==>  "zero; one"

    $set(target,zero)
    $setmulti(source,one; two)
    $copymerge(target,source)     ==>  "zero; one; two"

    $setmulti(target,zero; two)
    $setmulti(source,one; two)
    $copymerge(target,source)     ==>  "zero; two; one"

    $set(target,zero; one; zero)
    $set(source,one; two; three)
    $copymerge(target,source)     ==>  "zero, one; two; three"

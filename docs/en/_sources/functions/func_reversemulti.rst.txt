..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$reversemulti
=============

| Usage: **$reversemulti(name[,separator])**
| Category: multi-value
| Implemented: Picard 2.3.1

**Description:**

Returns a copy of the multi-value variable ``name`` with the elements in reverse order. A literal
value representing a multi-value can be substituted for ``name``, using the ``separator`` (or a
semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued
variable.

This function can be used in conjunction with the ``$sortmulti`` function to sort in descending order.


**Example:**

The following statements will return the values indicated::

    $set(foo,A; B; C; D; E)
    $reversemulti(%foo%)            ==>  "A; B; C; D; E"

    $setmulti(bar,A; B; C; D; E)
    $reversemulti(%bar%)            ==>  "E; D; C; B; A"

    $setmulti(baz,A:A; B:B; C:C,:)
    $reversemulti(%baz%)            ==>  "C; B; C; A; B; A"

    $reversemulti(A; B; C; D; E)    ==>  "E; D; C; B; A"
    $reversemulti(A:A; B:B; C:C,:)  ==>  "C:B; C:A; B:A"

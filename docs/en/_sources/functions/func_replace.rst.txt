..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$replace
========

| Usage: **$replace(text,search,replace)**
| Category: text

**Description:**

Replaces occurrences of ``search`` in ``text`` with ``replace`` and returns the resulting string.


**Example:**

The following statements will return the values indicated::

    $set(foo,I like cats the best)
    $replace(%foo%,cat,dog)                 ==>  "I like dogs the best"

    $set(foo,I like cats the best)
    $set(bar,cat)
    $replace(%foo%,%bar%,dog)               ==>  "I like dogs the best"

    $set(foo,I like cats the best)
    $set(bar,cat)
    $set(baz,dog)
    $replace(%foo%,%bar%,%baz%)             ==>  "I like dogs the best"

    $replace(I like cats the best,cat,dog)  ==>  "I like dogs the best"
    $replace(I like cats the best,pig,dog)  ==>  "I like cats the best"
    $replace(I like cats the best,cat,)     ==>  "I like s the best"
    $replace(Bad replace,,_)                ==>  "_B_a_d_ _r_e_p_l_a_c_e_"

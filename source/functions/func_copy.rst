.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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

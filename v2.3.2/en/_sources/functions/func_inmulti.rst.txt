.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$inmulti
========

| Usage: **$inmulti(%x%,y)**
| Category: conditional
| Implemented: Picard 1.0

**Description:**

Returns true if multi-value variable ``x`` contains exactly ``y`` as one of its values.
Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $setmulti(foo,One; Two; Three)
    $set(bar,Two)
    $inmulti(%foo%,%bar%)  ==>  "1"  (True)
    $inmulti(%foo%,Two)    ==>  "1"  (True)
    $inmulti(%foo%,two)    ==>  ""   (False)
    $inmulti(%foo%,Once)   ==>  ""   (False)
    $inmulti(%foo%,w)      ==>  ""   (False)
    $inmulti(%foo%,)       ==>  ""   (False)

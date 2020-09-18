.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$eq
===

| Usage: **$eq(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` equals ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $eq(,a)   ==>  ""   (False)
    $eq(a,)   ==>  ""   (False)
    $eq(a,A)  ==>  ""   (False)
    $eq(a,a)  ==>  "1"  (True)

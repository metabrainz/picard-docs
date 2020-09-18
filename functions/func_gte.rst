.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$gte
====

| Usage: **$gte(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` is greater than or equal to ``y``.  If an argument is missing or is
not an integer, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $gte(-1,0)   ==>  ""   (False)
    $gte(0,0)    ==>  "1"  (True)
    $gte(1,0)    ==>  "1"  (True)
    $gte(,)      ==>  ""   (False)
    $gte(,0)     ==>  ""   (False)
    $gte(0,)     ==>  ""   (False)
    $gte(a,1)    ==>  ""   (False)
    $gte(1,a)    ==>  ""   (False)
    $gte(1,1.5)  ==>  ""   (False)

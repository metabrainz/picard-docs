.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$gt
===

| Usage: **$gt(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` is greater than ``y``.  If an argument is missing or is
not an integer, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $gt(-1,0)   ==>  ""   (False)
    $gt(0,0)    ==>  ""   (False)
    $gt(1,0)    ==>  "1"  (True)
    $gt(,)      ==>  ""   (False)
    $gt(,0)     ==>  ""   (False)
    $gt(0,)     ==>  ""   (False)
    $gt(a,1)    ==>  ""   (False)
    $gt(1,a)    ==>  ""   (False)
    $gt(1,1.5)  ==>  ""   (False)

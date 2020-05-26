.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$lt
===

| Usage: **$lt(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` is less than ``y``.  If an argument is missing or is
not an integer, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $lte(-1,0)   ==>  "1"  (True)
    $lte(0,0)    ==>  ""   (False)
    $lte(1,0)    ==>  ""   (False)
    $lte(,)      ==>  ""   (False)
    $lte(,0)     ==>  ""   (False)
    $lte(0,)     ==>  ""   (False)
    $lte(a,1)    ==>  ""   (False)
    $lte(1,a)    ==>  ""   (False)
    $lte(1,1.5)  ==>  ""   (False)

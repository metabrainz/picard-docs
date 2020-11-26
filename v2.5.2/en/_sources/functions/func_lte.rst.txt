.. MusicBrainz Picard Documentation Project

$lte
====

| Usage: **$lte(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` is less than or equal to ``y``.  If an argument is missing or is
not an integer, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $lte(-1,0)   ==>  "1"  (True)
    $lte(0,0)    ==>  "1"  (True)
    $lte(1,0)    ==>  ""   (False)
    $lte(,)      ==>  ""   (False)
    $lte(,0)     ==>  ""   (False)
    $lte(0,)     ==>  ""   (False)
    $lte(a,1)    ==>  ""   (False)
    $lte(1,a)    ==>  ""   (False)
    $lte(1,1.5)  ==>  ""   (False)

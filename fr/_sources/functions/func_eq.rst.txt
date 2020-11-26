.. MusicBrainz Picard Documentation Project

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

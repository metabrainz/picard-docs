.. MusicBrainz Picard Documentation Project

$ne
===

| Usage: **$ne(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $ne(,a)   ==>  "1"  (True)
    $ne(a,)   ==>  "1"  (True)
    $ne(a,A)  ==>  "1"  (True)
    $ne(a,a)  ==>  ""   (False)

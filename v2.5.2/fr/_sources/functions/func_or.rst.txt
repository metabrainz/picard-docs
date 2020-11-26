.. MusicBrainz Picard Documentation Project

$or
===

| Usage: **$or(x,y,\*args)**
| Category: conditional

**Description:**

Returns true if either ``x`` or ``y`` is not empty. Can be used with an arbitrary number
of arguments. The result is true if **ANY** of the arguments is not empty.


**Example:**

The following statements will return the values indicated::

    $or(,)          ==>  ""   (False)
    $or(,1)         ==>  "1"  (True)
    $or(,A)         ==>  "1"  (True)
    $or(,$gt(4,5))  ==>  ""   (False)
    $or(,$lt(4,5))  ==>  "1"  (True)
    $or(,,)         ==>  ""   (False)
    $or(,,0)        ==>  "1"  (True)
    $or(,, )        ==>  "1"  (True)

.. MusicBrainz Picard Documentation Project

$and
====

| Usage: **$and(x,y,\*args)**
| Category: conditional

**Description:**

Returns true if both ``x`` and ``y`` are not empty. Can be used with an arbitrary number
of arguments. The result is true if **ALL** of the arguments are not empty.


**Example:**

The following statements will return the values indicated::

    $set(test,x)
    $and(%test%,)          ==>  ""   (False)
    $and(%test%,1)         ==>  "1"  (True)
    $and(%test%,A)         ==>  "1"  (True)
    $and(%test%,$gt(4,5))  ==>  ""   (False)
    $and(%test%,$lt(4,5))  ==>  "1"  (True)
    $and(%test%,,)         ==>  ""   (False)
    $and(%test%,,0)        ==>  ""   (False)
    $and(%test%,, )        ==>  ""   (False)
    $and(%test%, , )       ==>  "1"  (True)

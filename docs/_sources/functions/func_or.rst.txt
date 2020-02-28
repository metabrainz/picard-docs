.. Picard Function

$or
===

| Usage: **$or(x,y,\*args)**
| Category: conditional

**Description:**

Returns true if either ``x`` or ``y`` is not empty. Can be used with an arbitrary number
of arguments. The result is true if **ANY** of the arguments is not empty.


**Example:**

The following statements will return the values indicated::

    $or(,)          ==>  ""
    $or(,1)         ==>  "1"
    $or(,A)         ==>  "1"
    $or(,$gt(4,5))  ==>  ""
    $or(,$lt(4,5))  ==>  "1"
    $or(,,)         ==>  ""
    $or(,,0)        ==>  "1"
    $or(,, )        ==>  "1"

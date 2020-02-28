.. Picard Function

$gt
===

| Usage: **$gt(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` is greater than ``y``.  If an argument is missing or is
not an integer, the function will return "".


**Example:**

The following statements will return the values indicated::

    $gt(-1,0)   ==>  ""
    $gt(0,0)    ==>  ""
    $gt(1,0)    ==>  "1"
    $gt(,)      ==>  ""
    $gt(,0)     ==>  ""
    $gt(0,)     ==>  ""
    $gt(a,1)    ==>  ""
    $gt(1,a)    ==>  ""
    $gt(1,1.5)  ==>  ""

.. Picard Function

$gte
====

| Usage: **$gte(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` is greater than or equal to ``y``.  If an argument is missing or is
not an integer, the function will return "".


**Example:**

The following statements will return the values indicated::

    $gte(-1,0)   ==>  ""
    $gte(0,0)    ==>  "1"
    $gte(1,0)    ==>  "1"
    $gte(,)      ==>  ""
    $gte(,0)     ==>  ""
    $gte(0,)     ==>  ""
    $gte(a,1)    ==>  ""
    $gte(1,a)    ==>  ""
    $gte(1,1.5)  ==>  ""

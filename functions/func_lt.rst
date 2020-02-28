.. Picard Function

$lt
===

| Usage: **$lt(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` is less than ``y``.  If an argument is missing or is
not an integer, the function will return "".


**Example:**

The following statements will return the values indicated::

    $lte(-1,0)   ==>  "1"
    $lte(0,0)    ==>  ""
    $lte(1,0)    ==>  ""
    $lte(,)      ==>  ""
    $lte(,0)     ==>  ""
    $lte(0,)     ==>  ""
    $lte(a,1)    ==>  ""
    $lte(1,a)    ==>  ""
    $lte(1,1.5)  ==>  ""

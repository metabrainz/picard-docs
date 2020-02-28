.. Picard Function

$add
====

| Usage: **$add(x,y,\*args)**
| Category: mathematical

**Description:**

Adds ``y`` to ``x``.  Can be used with an arbitrary number of arguments (i.e. ``$add(x,y,z)`` = (x + y) + z).
Returns "" if an argument is missing or not an integer.

**Example:**

The following statements will return the values indicated::

    $add(20,15)      ==>  "45"
    $add(20,-15)     ==>  "5"
    $add(20,14,1)    ==>  "35"
    $add(20,10,3,2)  ==>  "35"
    $add(20,10,3,)   ==>  ""
    $add(20,10,3,a)  ==>  ""
    $add(20,10,3.5)  ==>  ""

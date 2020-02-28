.. Picard Function

$mod
====

| Usage: **$mod(x,y,\*args)**
| Category: mathematical

**Description:**

Returns the remainder of ``x`` divided by ``y``. Can be used with an arbitrary number of
arguments (i.e. ``$mod(x,y,z)`` = (x % y) % z). If an argument is empty or not an integer,
the function will return "".  If the second or any subsequent argument is zero, the
function will return "".


**Example:**

The following statements will return the values indicated::

    $mod(0,3)      ==>  "0"
    $mod(10,3)     ==>  "1"
    $mod(10,-3)    ==>  "-2"
    $mod(-13,10)    ==>  "7"
    $mod(13,-10)   ==>  "-7"
    $mod(10,3,1)   ==>  "0"
    $mod(50,17,9)  ==>  "7"
    $mod(51,3,0)   ==>  ""
    $mod(51,a)     ==>  ""
    $mod(a,10)     ==>  ""
    $mod(,10)      ==>  ""
    $mod(10,)      ==>  ""
    $mod(10,3.5)   ==>  ""

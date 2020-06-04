.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$mod
====

| Usage: **$mod(x,y,\*args)**
| Category: mathematical

**Description:**

Returns the remainder of ``x`` divided by ``y``. Can be used with an arbitrary number of
arguments (i.e.: ``$mod(x,y,z)`` = (x % y) % z). If an argument is empty or not an integer,
the function will return an empty string.  If the second or any subsequent argument is zero,
the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $mod(0,3)      ==>  "0"
    $mod(10,3)     ==>  "1"
    $mod(10,-3)    ==>  "-2"
    $mod(-13,10)   ==>  "7"
    $mod(13,-10)   ==>  "-7"
    $mod(10,3,1)   ==>  "0"
    $mod(50,17,9)  ==>  "7"
    $mod(51,3,0)   ==>  ""
    $mod(51,a)     ==>  ""
    $mod(a,10)     ==>  ""
    $mod(,10)      ==>  ""
    $mod(10,)      ==>  ""
    $mod(10,3.5)   ==>  ""

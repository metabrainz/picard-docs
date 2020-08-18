.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$sub
====

| Usage: **$sub(x,y,\*args)**
| Category: mathematical

**Description:**

Subtracts ``y`` from ``x``. Can be used with an arbitrary number of arguments (i.e.: ``$sub(x,y,z)`` = (x - y) - z).
Returns an empty string if an argument is missing or not an integer.


**Example:**

The following statements will return the values indicated::

    $sub(20,15)      ==>  "5"
    $sub(20,-15)     ==>  "35"
    $sub(20,14,1)    ==>  "5"
    $sub(20,10,3,2)  ==>  "5"
    $sub(20,10,3,)   ==>  ""
    $sub(20,10,3,a)  ==>  ""
    $sub(20,10,3.5)  ==>  ""

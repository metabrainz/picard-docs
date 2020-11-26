.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$mul
====

| Usage: **$mul(x,y,\*args)**
| Category: mathematical

**Description:**

Multiplies x by y. Can be used with an arbitrary number of arguments (i.e.:
``$mul(x,y,z)`` = (x \* y) \* z). If an argument is empty or not an integer,
the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $mul(1,2)      ==> "2"
    $mul(1,2,3)    ==> "6"
    $mul(1,2,0)    ==> "0"
    $mul(1,-2,3)   ==> "-6"
    $mul(-1,2,-3)  ==> "6"
    $mul(1,2,)     ==> ""
    $mul(1,2,x)    ==> ""
    $mul(1,2.5)    ==> ""

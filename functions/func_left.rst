.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$left
=====

| Usage: **$left(text,number)**
| Category: text

**Description:**

Returns the first ``number`` characters from ``text``.  If ``number`` is less than 0, then the
value used is the number of characters in ``text`` plus ``number`` (e.g.: ``$right(abcd,-1)``
is the same as ``$right(abcd,3)``).  If ``number`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $left(,)       ==>  ""
    $left(ABC,)    ==>  ""
    $left(ABC,0)   ==>  ""
    $left(ABC,2)   ==>  "AB"
    $left(ABC,4)   ==>  "ABC"
    $left(ABC,-2)  ==>  "A"
    $left(ABC,-4)  ==>  ""

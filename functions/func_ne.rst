.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$ne
===

| Usage: **$ne(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $ne(,a)   ==>  "1"  (True)
    $ne(a,)   ==>  "1"  (True)
    $ne(a,A)  ==>  "1"  (True)
    $ne(a,a)  ==>  ""   (False)

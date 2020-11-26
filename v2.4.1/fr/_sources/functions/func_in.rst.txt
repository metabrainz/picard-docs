.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$in
===

| Usage: **$in(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true, if ``x`` contains ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $set(foo,ABCDEFG)
    $set(bar,CDE)
    $in(%foo%,%bar%)  ==>  "1"  (True)
    $in(ABCDE,CDE)    ==>  "1"  (True)
    $in(ABCDE,CE)     ==>  ""   (False)
    $in(ABCDE,cde)    ==>  ""   (False)
    $in(ABCDE,)       ==>  "1"  (True)
    $in(,)            ==>  "1"  (True)

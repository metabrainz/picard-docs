.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$eq_all
=======

| Usage: **$eq_all(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` equals ``a1`` and ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$and($eq(x,a1),$eq(x,a2) ...)``.


**Example:**

The following statements will return the values indicated::

    $eq_all(A,A,B,C)    ==>  ""   (False)
    $eq_all(A,a,A,A)    ==>  ""   (False)
    $eq_all(A,A,A,A)    ==>  "1"  (True)
    $eq_all(,,,)        ==>  "1"  (True)
    $eq_all(,a,)        ==>  ""   (False)

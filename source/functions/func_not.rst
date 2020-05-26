.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$not
====

| Usage: **$not(x)**
| Category: conditional

**Description:**

Returns true if ``x`` is empty.


**Example:**

The following statements will return the values indicated::

    $set(foo,)
    $not(%foo%)  ==>  "1"  (False)

    $not(x)      ==>  ""  (True)
    $not( )      ==>  ""  (True)
    $not()       ==>  Error

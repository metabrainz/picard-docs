.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$reverse
========

| Usage: **$reverse(text)**
| Category: text

**Description:**

Returns ``text`` in reverse order.


**Example:**

The following statements will return the values indicated::

    $set(foo,abcde)
    $reverse(%foo%)  ==>  "edcba"

    $reverse(abcde)  ==>  "edcba"

.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$len
====

| Usage: **$len(text)**
| Category: text

**Description:**

Returns the number of characters in ``text``.


**Example:**

The following statements will return the values indicated::

    $set(foo,)
    $len(%foo%)    ==>  "0"

    $set(foo,ABC)
    $len(%foo%)    ==>  "3"

    $len()         ==>  "0"
    $len(ABC)      ==>  "3"

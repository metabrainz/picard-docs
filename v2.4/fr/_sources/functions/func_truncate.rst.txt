.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$truncate
=========

| Usage: **$truncate(text,length)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Truncate ``text`` to ``length``.  If ``length`` is less than 0, then the value used
is the number of characters in ``text`` plus ``length`` (e.g.: ``$truncate(abcd,-1)``
is the same as ``$truncate(abcd,3)``).  If ``length`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated::

    $truncate(Once upon a time,)     ==>  ""
    $truncate(Once upon a time,0)    ==>  ""
    $truncate(Once upon a time,3)    ==>  "Onc"
    $truncate(Once upon a time,-3)   ==>  "Once upon a t"
    $truncate(Once upon a time,-30)  ==>  ""

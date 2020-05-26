.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$endswith
=========

| Usage: **$endswith(text,suffix)**
| Category: conditional
| Implemented: Picard 1.4

**Description:**

Returns true if ``text`` ends with ``suffix``.  Note that the comparison is case-sensitive.


**Example:**

The statements below return the values indicated::

    $endswith(The time is now,is now)  ==>  "1"  (True)
    $endswith(The time is now,is NOW)  ==>  ""   (False)
    $endswith(The time is now,)        ==>  "1"  (True)
    $endswith(,)                       ==>  "1"  (True)
    $endswith(,now)                    ==>  ""   (False)

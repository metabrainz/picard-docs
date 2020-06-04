.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$initials
=========

| Usage: **$initials(text)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of each word in ``text``, if it is an alphabetic character.


**Example:**

The following statements will return the values indicated::

    $set(foo,This is a test)
    $initials(%foo%)               ==>  "Tiat"
    $initials(This is a test)      ==>  "Tiat"
    $initials(This is a 123 test)  ==>  "Tiat"

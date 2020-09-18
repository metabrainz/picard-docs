.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$firstalphachar
===============

| Usage: **$firstalphachar(text[,nonalpha])**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of ``text`` in upper case. If ``text`` does not begin with an
alphabetic character, then ``nonalpha`` is returned instead.  If ``nonalpha`` is not specified,
the default value "#" will be used.


**Example:**

The following statements will return the values indicated::

    $firstalphachar(abc)             ==>  "A"
    $firstalphachar(123)             ==>  "#"
    $firstalphachar(***)             ==>  "#"
    $firstalphachar(***,)            ==>  ""
    $firstalphachar(***,^)           ==>  "^"
    $firstalphachar(***,non-alpha)   ==>  "non-alpha"

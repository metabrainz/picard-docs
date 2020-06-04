.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$trim
=====

| Usage: **$trim(text[,char])**
| Category: text

**Description:**

Trims all leading and trailing whitespaces from ``text``. The optional second parameter ``char``
specifies the character to trim.  If multiple characters are provided in ``char``, each character
will be applied separately to the function.


**Examples:**

The following statements will return the values indicated::

    $trim(  Trimmed  )       ==>  "Trimmed"
    $trim(__Trimmed__,_)     ==>  "Trimmed"
    $trim(x__Trimmed__y,_x)  ==>  "Trimmed__y"

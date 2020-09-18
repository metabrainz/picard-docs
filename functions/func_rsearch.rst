.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$rsearch
========

| Usage: **$rsearch(text,pattern)**
| Category: text

**Description:**

Regular expression search. This function will return the first matching group specified by
``pattern`` from ``text``.  For more information about regular expressions, please see the
`article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.


**Example:**

The following statements will return the values indicated::

    $rsearch(test \(disc 1\),\\\(disc \(\\d+\)\\\))  ==>  "1"
    $rsearch(test \(disc 1\),\\\(disc \\d+\\\))      ==>  "(disc 1)"
    $rsearch(test,x)                                 ==>  ""

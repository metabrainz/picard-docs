.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$rreplace
=========

| Usage: **$rreplace(text,pattern,replace)**
| Category: text

**Description:**

Regular expression replace. This function will replace the matching group specified by
``pattern`` with ``replace`` in ``text``.  For more information about regular expressions,
please see the `article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.



**Example:**

The following statements will return the values indicated::

    $rreplace(test \(disc 1\),\\s\\\(disc \\d+\\\),)  ==>  "test"
    $rreplace(test,[t,)                               ==>  "test"

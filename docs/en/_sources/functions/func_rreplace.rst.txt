..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

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

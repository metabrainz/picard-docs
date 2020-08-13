.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$setmulti
=========

| Usage: **$setmulti(name,value[,separator])**
| Category: assignment
| Implemented: Picard 1.0

**Description:**

Sets the variable ``name`` to ``value``, using the ``separator`` (or a semicolon
followed by a space "; " if not passed) to coerce the ``value`` back into a proper
multi-valued variable. This can be used to operate on multi-valued variables as a string,
and then set them back as proper multi-valued variable.


**Example:**

The following statements will return the values indicated::

    $setmulti(genre,$lower(%genre%))  ==>  all "genre" elements in lower case
    $setmulti(alpha,A; B; C)          ==>  3 elements ("A", "B" and "C")
    $setmulti(mixed,A:A; B:B,:)       ==>  3 elements ("A", "A; B" and "B")

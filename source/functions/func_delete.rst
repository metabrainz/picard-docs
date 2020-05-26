.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$delete
=======

| Usage: **$delete(name)**
| Category: assignment
| Implemented: Picard 2.1

**Description:**

Unsets the variable ``name`` and marks the tag for deletion.

This is similar to ``$unset(name)`` but also marks the tag for deletion. For example,
running ``$delete(genre)`` will actually remove the "genre" tag from a file when saving.


**Example:**

The following statements will perform the actions indicated::

    $delete(genre)  ==>  Remove the "genre" tag from a file when saving

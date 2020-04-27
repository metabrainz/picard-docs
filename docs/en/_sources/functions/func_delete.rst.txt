..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

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

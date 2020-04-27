..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$is_complete
============

| Usage: **$is_complete()**
| Category: conditional

**Description:**

Returns true if every track in the album is matched to a single file.

Note that this only works in File Naming scripts.


**Example:**

The following statements will return the values indicated::

    $is_complete()  ==>  "1"  (True, if all tracks have been matched)
    $is_complete()  ==>  ""   (False, if not all tracks have been matched)

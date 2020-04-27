..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$unset
======

| Usage: **$unset(name)**
| Category: assignment

**Description:**

Unsets the variable ``name``.  The function allows for wildcards to unset certain tags
(works with 'performer:\*', 'comment:\*', and 'lyrics:\*').


**Example:**

The following would unset all performer tags::

    $unset(performer:*)

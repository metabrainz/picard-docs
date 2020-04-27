..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$while
======

| Usage: **$while(condition,code)**
| Category: loop
| Implemented: Picard 2.3

**Description:**

Executes ``code`` repeatedly until ``condition`` no longer evaluates to True. For each loop,
the count is stored in the variable ``_loop_count``. This allows the count value to be accessed
within the ``code`` script.

Note that the function limits the maximum number of iterations to 1000 as a safeguard against
accidentally creating an infinite loop.


**Example:**

The following statement will set ``return`` to "Echo... echo... echo..."::

    $set(return,Echo...)$while($lt(%_loop_count%,2),$set(return,%return% echo...))

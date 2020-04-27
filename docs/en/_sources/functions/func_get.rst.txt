..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$get
====

| Usage: **$get(name)**
| Category: text

**Description:**

Returns the variable ``name`` (equivalent to ``%name%``) or an empty string if ``name`` has not
been set.  If ``name`` is another variable (e.g. ``%indirect%``) the value of the
variable will be used as ``name``.  This allows the retrieval of dynamically named
variables.


**Example:**

The following statements will return the values indicated::

    $set(foo,This is foo)
    $set(bar,foo)
    $get(foo)              ==>  "This is foo"
    $get(bar)              ==>  "foo"
    $get(%bar%)            ==>  "This is foo"
    $get(baz)              ==>  "" ('baz' has not been set to a value)

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$if
===

| Usage: **$if(condition,then[,else])**
| Category: conditional

**Description:**

If ``condition`` is not empty it returns ``then``, otherwise it returns ``else``.  If ``else``
is not provided, it will be assumed to be an empty string.  In addition to (or instead of) returning values,
``then`` and ``else`` can be used to conditionally execute other functions.


**Example:**

The following statements will return the values indicated::

    $set(foo,This is foo)
    $set(bar,)
    $if(%foo%,%foo%,No foo)                   ==>  "This is foo"
    $if(%bar%,%bar%,No bar)                   ==>  "No bar"
    $if(%bar%,This is bar,No bar)             ==>  "No bar"
    $if(%bar%,This is bar,)                   ==>  ""
    $if(%bar%,This is bar)                    ==>  ""
    $if(,True,False)                          ==>  "False"
    $if( ,True,False)                         ==>  "True"
    $if(,$set(value,True),$set(value,False))  ==>  Sets "value" to "False"
    $set(value,$if(%bar%,True,False))         ==>  Sets "value" to "False"

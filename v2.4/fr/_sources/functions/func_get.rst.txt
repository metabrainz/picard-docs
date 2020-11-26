.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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

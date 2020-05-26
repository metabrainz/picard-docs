.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$noop
=====

| Usage: **$noop(...)**
| Category: miscellaneous

**Description:**

Does nothing and always returns an empty string.  This is useful for comments or disabling a block of code.


**Example:**

The following statements will return the values indicated::

    $noop( A comment. )          ==>  ""
    $noop($set(foo,Testing...))  ==>  "" (and "foo" is not set)

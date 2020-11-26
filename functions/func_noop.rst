.. MusicBrainz Picard Documentation Project

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

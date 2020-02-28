.. Picard Function

$noop
=====

| Usage: **$noop(...)**
| Category: miscellaneous

**Description:**

Does nothing and always returns "".  This is useful for comments or disabling a block of code.


**Example:**

The following statements will return the values indicated::

    $noop( A comment. )          ==>  ""
    $noop($set(foo,Testing...))  ==>  "" (and `foo` is not set)

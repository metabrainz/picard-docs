.. Picard Function

$not
====

| Usage: **$not(x)**
| Category: conditional

**Description:**

Returns true if ``x`` is empty.


**Example:**

The following statements will return the values indicated::

    $set(foo,)
    $not(%foo%)  ==>  "1"

    $not(x)      ==>  ""
    $not( )      ==>  ""
    $not()       ==>  Error

.. Picard Function

$reverse
========

| Usage: **$reverse(text)**
| Category: text

**Description:**

Returns ``text`` in reverse order.


**Example:**

The following statements will return the values indicated::

    $set(foo,abcde)
    $reverse(%foo%)  ==>  "edcba"

    $reverse(abcde)  ==>  "edcba"

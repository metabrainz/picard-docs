.. Picard Function

$right
======

| Usage: **$right(text,num)**
| Category: text

**Description:**

Returns the last ``num`` characters from ``text``.  If ``num`` is less than 1, then the
value used is the number of characters in ``text`` plus ``num`` (e.g. ``$right(abcd,0)``
is the same as ``$right(abcd,4)``).  If ``num`` is missing or a negative number greater
than the number of characters in ``text``, the function will return "".


**Example:**

The following statements will return the values indicated::

    $right(abcd,2)   ==>  "cd"
    $right(abcd,0)   ==>  "cd"
    $right(abcd,-1)  ==>  "bcd"
    $right(abcd,)    ==>  ""
    $right(abcd,-5)  ==>  ""

.. Picard Function

$left
=====

| Usage: **$left(text,num)**
| Category: text

**Description:**

Returns the first ``num`` characters from ``text``.  If ``num`` is less than 0, then the
value used is the number of characters in ``text`` plus ``num`` (e.g. ``$right(abcd,-1)``
is the same as ``$right(abcd,3)``).  If ``num`` is missing or a negative number greater
than the number of characters in ``text``, the function will return "".


**Example:**

The following statements will return the values indicated::

    $left(,)       ==>  ""
    $left(ABC,)    ==>  ""
    $left(ABC,0)   ==>  ""
    $left(ABC,2)   ==>  "AB"
    $left(ABC,4)   ==>  "ABC"
    $left(ABC,-2)  ==>  "A"
    $left(ABC,-4)  ==>  ""

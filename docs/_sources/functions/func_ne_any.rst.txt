.. Picard Function

$ne_any
=======

| Usage: **$ne_any(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``a1`` or ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$or($ne(x,a1),$ne(x,a2) ...)``.


**Example:**

The following statements will return the values indicated::

    $ne_any(A,A,B,C)    ==>  "1"
    $ne_any(A,a,A,A)    ==>  "1"
    $ne_any(A,A,A,A)    ==>  ""
    $ne_any(,,,)        ==>  ""
    $ne_any(,a,,)       ==>  "1"

.. Picard Function

$ne_all
=======

| Usage: **$ne_all(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``a1`` and ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$and($ne(x,a1),$ne(x,a2) ...)``.


**Example:**

The following statements will return the values indicated::

    $ne_all(A,A,B,C)    ==>  ""
    $ne_all(A,a,A,A)    ==>  ""
    $ne_all(A,a,a,a)    ==>  "1"
    $ne_all(,,,)        ==>  ""
    $ne_all(,a,a)       ==>  "1"

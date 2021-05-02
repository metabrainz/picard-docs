.. MusicBrainz Picard Documentation Project

$ne_any
=======

| Usage: **$ne_any(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``a1`` or ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$or($ne(x,a1),$ne(x,a2) ...)``.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $ne_any(A,A,B,C)    ==>  "1"  (True)
    $ne_any(A,a,A,A)    ==>  "1"  (True)
    $ne_any(A,A,A,A)    ==>  ""   (False)
    $ne_any(,,,)        ==>  ""   (False)
    $ne_any(,a,,)       ==>  "1"  (True)

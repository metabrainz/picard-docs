.. MusicBrainz Picard Documentation Project

.. _func_ne_all:

$ne_all
=======

| Usage: **$ne_all(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``a1`` and ``a2``, etc.  Can be used with an arbitrary
number of arguments.  Note that comparisons are case-sensitive.

Functionally equivalent to ``$and($ne(x,a1),$ne(x,a2) ...)``.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $ne_all(A,A,B,C)    ==>  ""   (False)
    $ne_all(A,a,A,A)    ==>  ""   (False)
    $ne_all(A,a,a,a)    ==>  "1"  (True)
    $ne_all(,,,)        ==>  ""   (False)
    $ne_all(,a,a)       ==>  "1"  (True)

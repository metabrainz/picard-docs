.. MusicBrainz Picard Documentation Project

.. _func_eq_any:

$eq_any
=======

| Usage: **$eq_any(x,a1,a2,\*args)**
| Category: conditional

**Description:**

Returns true if ``x`` equals ``a1`` or ``a2``, etc. Can be used with an arbitrary number of arguments. Note that comparisons are case-sensitive.

Functionally equivalent to ``$or($eq(x,a1),$eq(x,a2) ...)``.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $eq_any(A,A,B,C)  ==>  "1"  (True)
   $eq_any(A,a,A,A)  ==>  "1"  (True)
   $eq_any(A,a,b,c)  ==>  ""   (False)
   $eq_any(,,,)      ==>  "1"  (True)
   $eq_any(,a,b,c)   ==>  ""   (False)

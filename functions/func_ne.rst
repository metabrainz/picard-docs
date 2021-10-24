.. MusicBrainz Picard Documentation Project

.. _func_ne:

$ne
===

| Usage: **$ne(x,y)**
| Category: conditional

**Description:**

Returns true if ``x`` does not equal ``y``.  Note that comparisons are case-sensitive.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $ne(,a)   ==>  "1"  (True)
    $ne(a,)   ==>  "1"  (True)
    $ne(a,A)  ==>  "1"  (True)
    $ne(a,a)  ==>  ""   (False)

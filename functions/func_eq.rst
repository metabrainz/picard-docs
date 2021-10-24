.. MusicBrainz Picard Documentation Project

.. _func_eq:

$eq
===

| Usage: **$eq(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` equals ``y``.  Note that comparisons are case-sensitive.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $eq(,a)   ==>  ""   (False)
    $eq(a,)   ==>  ""   (False)
    $eq(a,A)  ==>  ""   (False)
    $eq(a,a)  ==>  "1"  (True)

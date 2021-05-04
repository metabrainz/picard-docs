.. MusicBrainz Picard Documentation Project

.. _func_eq:

$eq
===

| Usage: **$eq(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true if ``x`` equals ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $eq(,a)   ==>  ""   (False)
    $eq(a,)   ==>  ""   (False)
    $eq(a,A)  ==>  ""   (False)
    $eq(a,a)  ==>  "1"  (True)

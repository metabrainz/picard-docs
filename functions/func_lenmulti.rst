.. MusicBrainz Picard Documentation Project

.. _func_lenmulti:

$lenmulti
=========

| Usage: **$lenmulti(name[,separator])**
| Category: multi-value

**Description:**

Returns the number of elements in the multi-value variable ``name``. A literal value
representing a multi-value can be substituted for ``name``, using the ``separator``
(or a semicolon followed by a space "; " if not passed) to coerce the value into a
proper multi-valued variable.  If ``name`` is missing :ref:`func_lenmulti` will return "0".  If
``separator`` is specified but left blank (e.g. ``$setmulti(A; B; C,)``) the function
will return "1".


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,)
    $lenmulti(%foo%)            ==>  "0"

    $set(foo,A; B; C)
    $lenmulti(%foo%)            ==>  "1"

    $setmulti(foo,A; B; C)
    $lenmulti(%foo%)            ==>  "3"

    $lenmulti(A; B; C)          ==>  "3"
    $lenmulti(A:A; B:B; C:C,:)  ==>  "4"
    $lenmulti(,)                ==>  "0"
    $lenmulti(,:)               ==>  "0"
    $lenmulti(A; B; C,)         ==>  "1"

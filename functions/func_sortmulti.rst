.. MusicBrainz Picard Documentation Project

.. _func_sortmulti:

$sortmulti
==========

| Usage: **$sortmulti(name[,separator])**
| Category: multi-value
| Implemented: Picard 2.3.1

**Description:**

Returns a copy of the multi-value variable ``name`` with the elements sorted in ascending order. A literal value representing a multi-value can be substituted for ``name``, using the ``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued variable. If ``name`` is missing ``$sortmulti`` will return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,B; C; E; D; A)
   $sortmulti(%foo%)                       ==>  "B; C; E; D; A"

   $setmulti(foo,B; C; E; D; A)
   $sortmulti(%foo%)                       ==>  "A; B; C; D; E"

   $sortmulti(B; D; E; A; C)               ==>  "A; B; C; D; E"
   $sortmulti(B:AB; D:C; E:D; A:A; C:X,:)  ==>  "A; C:AB; D:B:C; E:D; A:X"
   $sortmulti(,)                           ==>  ""
   $sortmulti(,:)                          ==>  ""

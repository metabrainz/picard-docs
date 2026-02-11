.. MusicBrainz Picard Documentation Project

.. _func_setmulti:

$setmulti
=========

| Usage: **$setmulti(name,value[,separator])**
| Category: assignment
| Implemented: Picard 1.0

**Description:**

Sets the variable ``name`` to ``value``, using the ``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the ``value`` back into a proper multi-valued variable. This can be used to operate on multi-valued variables as a string, and then set them back as proper multi-valued variable.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(genre,$lower(%genre%))  ==>  all "genre" elements in lower case
   $setmulti(alpha,A; B; C)          ==>  3 elements ("A", "B" and "C")
   $setmulti(mixed,A:A; B:B,:)       ==>  3 elements ("A", "A; B" and "B")

.. MusicBrainz Picard Documentation Project

.. _func_copymerge:

$copymerge
==========

| Usage: **$copymerge(new,old[,keep_duplicates])**
| Category: assignment
| Implemented: Picard 1.0

**Description:**

Merges metadata from variable ``old`` into ``new``, removing duplicates and appending to the end, so retaining the original ordering. Like :ref:`func_copy`, this will also copy multi-valued variables without flattening them. Following the operation, ``new`` will be a multi-value variable.

If ``keep_duplicates`` is set, then the duplicates will not be removed from the result.

.. note::

   Unlike most functions, in this case ``new`` and ``old`` are specified **without** enclosing them with percent signs (%).


**Example:**

The following statements will yield the values for ``target`` as indicated:

.. code-block:: taggerscript

   $set(target,)
   $set(source,one)
   $copymerge(target,source)     ==>  "one"

   $set(target,zero)
   $set(source,one)
   $copymerge(target,source)     ==>  "zero; one"

   $set(target,zero)
   $setmulti(source,one; two)
   $copymerge(target,source)     ==>  "zero; one; two"

   $setmulti(target,zero; two)
   $setmulti(source,one; two)
   $copymerge(target,source)     ==>  "zero; two; one"

   $set(target,zero; one; zero)
   $set(source,one; two; three)
   $copymerge(target,source)     ==>  "zero, one; two; three"

   $setmulti(target,zero; two)
   $setmulti(source,one; two)
   $copymerge(target,source,1)   ==>  "zero; two; one; two"

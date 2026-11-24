.. MusicBrainz Picard Documentation Project

.. _func_copy:

$copy
=====

| Usage: **$copy(new,old)**
| Category: assignment
| Implemented: Picard 0.9

**Description:**

Copies metadata from variable ``old`` to ``new``. The difference from ``$set(new,%old%)`` is that ``$copy(new,old)`` copies multi-value variables without flattening them.

.. note::

   Unlike most functions, in this case ``new`` and ``old`` are specified **without** enclosing them with percent signs (%).

.. warning::

   If the variable ``new`` already exists, it will be overwritten by ``old``.

**Example:**

The following statements will yield the values for ``target`` as indicated:

.. code-block:: taggerscript

   $set(source,)
   $set(target,This will be overwritten)
   $copy(target,source)                   ==>  ""

   $set(source,one)
   $copy(target,source)                   ==>  "one"

   $setmulti(source,one)
   $copy(target,source)                   ==>  "one"

   $setmulti(source,one; two)
   $copy(target,source)                   ==>  "one; two"

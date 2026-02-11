.. MusicBrainz Picard Documentation Project

.. _func_copy:

$copy
=====

| Usage: **$copy(target,source)**
| Category: assignment
| Implemented: Picard 0.9

**Description:**

Copies metadata from variable ``source`` to ``target``. The difference from ``$set(target,%source%)`` is that ``$copy(target,source)`` copies multi-value variables without flattening them.

.. note::

   Unlike most functions, in this case the ``source`` is specified **without** enclosing it with percent signs (%).

.. warning::

   If the variable ``target`` already exists, it will be overwritten by ``source``.

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

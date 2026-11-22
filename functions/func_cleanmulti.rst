.. MusicBrainz Picard Documentation Project

.. _func_cleanmulti:

$cleanmulti
===========

| Usage: **$cleanmulti(name)**
| Category: multi-value
| Implemented: Picard 2.8

**Description:**

Permanently removes all empty elements from the multi-value variable ``name``, and returns an empty string.

.. note::

   Unlike most functions, in this case ``name`` is specified **without** enclosing it with percent signs (%).

.. warning::

   The variable will modified and its original contents will no longer be available. Use :doc:`$removemulti() <func_removemulti>` to get a copy without empty elements and leave the original variable unchanged.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(test,One; ; Two; Three)
   %test%                               ==>  "One; ; Two; Three"
   $cleanmulti(test)
   %test%                               ==>  "One; Two; Three"

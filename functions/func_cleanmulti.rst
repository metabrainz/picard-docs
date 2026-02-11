.. MusicBrainz Picard Documentation Project

.. _func_cleanmulti:

$cleanmulti
===========

| Usage: **$cleanmulti(name)**
| Category: multi-value
| Implemented: Picard 2.8

**Description:**

Removes all empty elements from the multi-value variable ``name``.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(test,One; ; Two; Three)
   %test%                               ==>  "One; ; Two; Three"
   $cleanmulti(test)
   %test%                               ==>  "One; Two; Three"

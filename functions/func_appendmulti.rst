.. MusicBrainz Picard Documentation Project

.. _func_appendmulti:

$appendmulti
=============

| Usage: **$appendmulti(name,value,\*args)**
| Category: multi-value
| Implemented: Picard 2.8

**Description:**

Appends ``value`` to the multi-value variable ``name``.  Any number of values can be included.

.. note::

   The multi-value must exist before the values can be appended. This can be checked using the ``$if()``
   function such as:

   .. code-block:: taggerscript

      $if(%multi%,$appendmulti(%multi%,value),$setmulti(multi,value))


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(test,One; Two)
   $appendmulti(test,Three)
   %test%                                                         ==>  "One; Two; Three"

   $noop( %test% not existing - not checked )
   $setmulti(test,)
   $appendmulti(test,Three)
   %test%                                                         ==>  "" (Not appended)

   $noop( %test% not existing - checked )
   $setmulti(test,)
   $if(%test%,$appendmulti(%test%,Three),$setmulti(test,Three))
   %test%                                                         ==>  "Three"

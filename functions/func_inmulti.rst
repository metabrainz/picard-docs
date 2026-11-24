.. MusicBrainz Picard Documentation Project

.. _func_inmulti:

$inmulti
========

| Usage: **$inmulti(multi,value[,separator])**
| Category: conditional
| Implemented: Picard 1.0

**Description:**

Returns true if the multi-value variable ``multi`` contains exactly ``value`` as one of its values. Note that comparisons are case-sensitive.

A literal value representing a multi-value can be substituted for ``multi``, using the ``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued variable.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(foo,One; Two; Three)
   $set(bar,Two)
   $inmulti(%foo%,%bar%)  ==>  "1"  (True)
   $inmulti(%foo%,Two)    ==>  "1"  (True)
   $inmulti(%foo%,two)    ==>  ""   (False)
   $inmulti(%foo%,Once)   ==>  ""   (False)
   $inmulti(%foo%,w)      ==>  ""   (False)
   $inmulti(%foo%,)       ==>  ""   (False)

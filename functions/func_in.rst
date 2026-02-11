.. MusicBrainz Picard Documentation Project

.. _func_in:

$in
===

| Usage: **$in(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true, if ``x`` contains ``y``. Note that comparisons are case-sensitive.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,ABCDEFG)
   $set(bar,CDE)
   $in(%foo%,%bar%)  ==>  "1"  (True)
   $in(ABCDE,CDE)    ==>  "1"  (True)
   $in(ABCDE,CE)     ==>  ""   (False)
   $in(ABCDE,cde)    ==>  ""   (False)
   $in(ABCDE,)       ==>  "1"  (True)
   $in(,)            ==>  "1"  (True)

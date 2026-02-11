.. MusicBrainz Picard Documentation Project

.. _func_is_multi:

$is_multi
=========

| Usage: **$is_multi(x)**
| Category: conditional
| Implemented: Picard 2.7

**Description:**

Returns true, if the argument is a multi-value tag and there is more than one element.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,a; b; c)
   $is_multi(%foo%)        ==>  "" (False)

   $set(bar,)
   $is_multi(%bar%)        ==>  "" (False)

   $setmulti(baz,a; b; c)
   $is_multi(%baz%)        ==>  "1" (True)

   $is_multi(a; b; c)      ==>  "1" (True)
   $is_multi(a)            ==>  "" (False)

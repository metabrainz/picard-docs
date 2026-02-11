.. MusicBrainz Picard Documentation Project

.. _func_replacemulti:

$replacemulti
=============

| Usage: **$replacemulti(name,search,replace[,separator])**
| Category: multi-value
| Implemented: Picard 2.6.1

**Description:**

Replaces occurrences of ``search`` with ``replace`` in the multi-value variable ``name`` and returns the resulting multi-value variable string with the elements separated by ``separator`` (or the default separator of a semicolon followed by a space "; " if not passed).

Empty elements are automatically removed from the output.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(foo,Electronic; Idm; Techno)
   $replacemulti(%foo%,Idm,IDM)                ==>  "Electronic; IDM; Techno"

   $setmulti(foo,Electronic; Jungle; Bardcore)
   $replacemulti(%foo%,Bardcore,Hardcore)      ==>  "Electronic; Jungle; Hardcore"

   $setmulti(foo,One; Two; Three)
   $replacemulti(%foo%,Four,Five)              ==>  "One; Two; Three"

   $setmulti(foo,Four; Five; Six)
   $replacemulti(%foo%,Five,)                  ==>  "Four; Six"

.. MusicBrainz Picard Documentation Project

.. _func_firstalphachar:

$firstalphachar
===============

| Usage: **$firstalphachar(text[,nonalpha])**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of ``text`` in upper case. If ``text`` does not begin with an alphabetic character, then ``nonalpha`` is returned instead. If ``nonalpha`` is not specified, the default value "#" will be used.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $firstalphachar(abc)             ==>  "A"
   $firstalphachar(123)             ==>  "#"
   $firstalphachar(***)             ==>  "#"
   $firstalphachar(***,)            ==>  ""
   $firstalphachar(***,^)           ==>  "^"
   $firstalphachar(***,non-alpha)   ==>  "non-alpha"

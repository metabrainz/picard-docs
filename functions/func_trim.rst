.. MusicBrainz Picard Documentation Project

.. _func_trim:

$trim
=====

| Usage: **$trim(text[,characters])**
| Category: text

**Description:**

Trims all leading and trailing whitespaces from ``text``. The optional second parameter ``characters`` specifies the characters to trim instead of whitespace. Each of the characters provided in ``characters`` is removed from both ends of ``text``, whatever their order.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $trim(  Trimmed  )       ==>  "Trimmed"
   $trim(__Trimmed__,_)     ==>  "Trimmed"
   $trim(x__Trimmed__y,_x)  ==>  "Trimmed__y"

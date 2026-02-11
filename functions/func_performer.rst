.. MusicBrainz Picard Documentation Project

.. _func_performer:

$performer
==========

| Usage: **$performer(pattern[,separator])**
| Category: multi-value
| Implemented: Picard 0.10

**Description:**

Returns the performers where the performance type matches ``pattern`` separated by ``separator`` (or a comma followed by a space ", " if not passed). If ``pattern`` is blank, then all performers will be returned. Note that by default the ``pattern`` to be matched is case-sensitive and can appear anywhere in the tag.

As of version 2.7, you can explicitly define a regular expression in the form /pattern/flags. The only supported flag is "i" (ignore case). For more information about regular expressions, please see the `article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.

.. note::

   When entering regular expressions into Picard scripts you have to escape a backslash "\\", dollar sign "$", comma "," and the left and right parentheses "(" and ")" in order to force Picard to not interpret them as part of the script command. This is done by inserting a backslash before the character to be escaped. For example, the regular expression ``^\s*([0-9,\.]*)$`` would have to be entered as ``^\\s*\([0-9\,\\.]*\)\$``.

**Example:**

With the performer tags as ``performer:guitar`` = "Ann", ``performer:rhythm-guitar`` = "Bob" and ``performer:drums (drum kit)`` = "Cindy", the following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,guitar)
   $performer(%foo%)          ==>  "Ann, Bob"

   $performer(guitar)         ==>  "Ann, Bob"
   $performer(Guitar)         ==>  ""
   $performer(rhythm-guitar)  ==>  "Bob"
   $performer(/Guitar/i)      ==>  "Ann, Bob"
   $performer(/Guitar/)       ==>  ""
   $performer(/^guitar/)      ==>  "Ann"
   $performer(/^Guitar/i)     ==>  "Ann"
   $performer(drums \()       ==>  "Cindy"
   $performer(\(drum kit\))   ==>  "Cindy"
   $performer()               ==>  "Ann, Bob, Cindy"
   $performer(, / )           ==>  "Ann / Bob / Cindy"

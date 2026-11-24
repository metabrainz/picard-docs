.. MusicBrainz Picard Documentation Project

.. _func_removemulti:

$removemulti
============

| Usage: **$removemulti(multi[,pattern[,separator=; ]])**
| Category: multi-value
| Implemented: Picard 3.1

**Description:**

Returns a copy of the multi-value tag ``multi`` without the elements matching the `regular expression <https://docs.python.org/3/library/re.html#regular-expression-syntax>`_ ``pattern``. If ``pattern`` is omitted or empty, the empty elements are removed.

A literal value representing a multi-value can be substituted for ``multi``, using the ``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued variable.

The pattern can match anywhere in an element. Use ``^`` and ``\$`` to match the start and end of the element respectively. Include ``\(?i\)`` at the start of the pattern for a case-insensitive match. An invalid pattern removes nothing.

Unlike the :doc:`$cleanmulti() <func_cleanmulti>` function, the original variable is not updated.

**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(test,One; ; Two; Three)
   $removemulti(%test%)                 ==>  "One; Two; Three"
   $removemulti(%test%,)                ==>  "One; Two; Three"
   $removemulti(%test%,hre)             ==>  "One; ; Two"
   $removemulti(%test%,^hre)            ==>  "One; ; Two; Three"
   $removemulti(%test%,hre\$)           ==>  "One; ; Two; Three"
   $removemulti(%test%,o)               ==>  "One; ; Three"
   $removemulti(%test%,\(?i\)o)         ==>  "; ; Three"
   $removemulti(%test%,\()              ==>  "One; ; Two; Three"

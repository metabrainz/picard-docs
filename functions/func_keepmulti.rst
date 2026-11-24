.. MusicBrainz Picard Documentation Project

.. _func_keepmulti:

$keepmulti
==========

| Usage: **$keepmulti(multi[,pattern[,separator=; ]])**
| Category: multi-value
| Implemented: Picard 3.1

**Description:**

Returns a copy of the multi-value tag ``multi`` with only the elements matching the `regular expression <https://docs.python.org/3/library/re.html#regular-expression-syntax>`_ ``pattern``. If ``pattern`` is omitted or empty, all elements are kept.

A literal value representing a multi-value can be substituted for ``multi``, using the ``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued variable.

The pattern can match anywhere in an element. Use ``^`` and ``\$`` to match the start and end of the element respectively. Include ``\(?i\)`` at the start of the pattern for a case-insensitive match. An invalid pattern keeps everything.

Unlike the :doc:`$cleanmulti() <func_cleanmulti>` function, the original variable is not updated.

**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $setmulti(test,One; ; Two; Three)
   $keepmulti(%test%)                 ==>  "One; ; Two; Three"
   $keepmulti(%test%,)                ==>  "One; ; Two; Three"
   $keepmulti(%test%,hre)             ==>  "Three"
   $keepmulti(%test%,^hre)            ==>  ""
   $keepmulti(%test%,hre\$)           ==>  ""
   $keepmulti(%test%,o)               ==>  "Two"
   $keepmulti(%test%,\(?i\)o)         ==>  "One; Two"
   $keepmulti(%test%,\()              ==>  "One; ; Two; Three"

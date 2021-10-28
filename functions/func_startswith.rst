.. MusicBrainz Picard Documentation Project

.. _func_startswith:

$startswith
===========

| Usage: **$startswith(text,prefix)**
| Category: conditional
| Implemented: Picard 1.4

**Description:**

Returns true if ``text`` starts with ``prefix``.  Note that the comparison is case-sensitive.

.. only:: html

   .. warning::

      Formatting the code using characters such as spaces, tabs or newlines can affect the result of the function.

**Example:**

The statements below return the values indicated:

.. code-block:: taggerscript

    $startswith(The time is now.,The time)  ==>  "1"  (True)
    $startswith(The time is now.,The TIME)  ==>  ""   (False)
    $startswith(The time is now.,)          ==>  "1"  (True)
    $startswith(,The)                       ==>  ""   (False)
    $startswith(,)                          ==>  "1"  (True)

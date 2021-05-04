.. MusicBrainz Picard Documentation Project

.. _func_endswith:

$endswith
=========

| Usage: **$endswith(text,suffix)**
| Category: conditional
| Implemented: Picard 1.4

**Description:**

Returns true if ``text`` ends with ``suffix``.  Note that the comparison is case-sensitive.


**Example:**

The statements below return the values indicated:

.. code-block:: taggerscript

    $endswith(The time is now,is now)  ==>  "1"  (True)
    $endswith(The time is now,is NOW)  ==>  ""   (False)
    $endswith(The time is now,)        ==>  "1"  (True)
    $endswith(,)                       ==>  "1"  (True)
    $endswith(,now)                    ==>  ""   (False)

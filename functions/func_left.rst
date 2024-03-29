.. MusicBrainz Picard Documentation Project

.. _func_left:

$left
=====

| Usage: **$left(text,number)**
| Category: text

**Description:**

Returns the first ``number`` characters from ``text``.  If ``number`` is less than 0, then the
value used is the number of characters in ``text`` plus ``number`` (e.g.: ``$left(abcd,-1)``
is the same as ``$left(abcd,3)``).  If ``number`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $left(,)       ==>  ""
    $left(ABC,)    ==>  ""
    $left(ABC,0)   ==>  ""
    $left(ABC,2)   ==>  "AB"
    $left(ABC,4)   ==>  "ABC"
    $left(ABC,-2)  ==>  "A"
    $left(ABC,-4)  ==>  ""

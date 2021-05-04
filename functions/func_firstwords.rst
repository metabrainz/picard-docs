.. MusicBrainz Picard Documentation Project

.. _func_firstwords:

$firstwords
===========

| Usage: **$firstwords(text,length)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Truncate ``text`` to ``length``, only returning the complete words from ``text`` which fit
within ``length`` characters.  If ``length`` is less than 0, then the value used is the number
of characters in ``text`` plus ``length`` (e.g.: ``$firstwords(one two three,-3)`` is the same
as ``$firstwords(one two three,10)``).  If ``length`` is missing or a negative number greater
than the number of characters in ``text``, the function will return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $firstwords(Once upon a time,)     ==>  ""
    $firstwords(Once upon a time,0)    ==>  ""
    $firstwords(Once upon a time,3)    ==>  ""
    $firstwords(Once upon a time,7)    ==>  "Once"
    $firstwords(Once upon a time,-3)   ==>  "Once upon a"
    $firstwords(Once upon a time,-30)  ==>  ""

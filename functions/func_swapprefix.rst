.. MusicBrainz Picard Documentation Project

.. _func_swapprefix:

$swapprefix
===========

| Usage: **$swapprefix(text[,prefixes])**
| Category: text
| Implemented: Picard 1.3 (*previously as a plugin since Picard 0.13*)

**Description:**

Moves the specified ``prefixes`` from the beginning to the end of ``text``. Any number of ``prefixes``
can be specified, separated by commas. If no prefix is specified "A" and "The" are used by default.
Note that the matching is case-sensitive.


**Example:**

If the ``albumartist`` is "Le Butcherettes", the following statements will return the values indicated:

.. code-block:: taggerscript

    $swapprefix(%albumartist%)               ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,le)            ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,L)             ==>  "Le Butcherettes"
    $swapprefix(%albumartist%,A,An,The,Le)   ==>  "Butcherettes, Le"

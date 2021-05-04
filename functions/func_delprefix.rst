.. MusicBrainz Picard Documentation Project

.. _func_delprefix:

$delprefix
==========

| Usage: **$delprefix(text[,prefixes])**
| Category: text
| Implemented: Picard 1.3

**Description:**

Deletes the specified ``prefixes`` from the beginning of ``text``. Any number of ``prefixes``
can be specified, separated by commas. If no prefix is specified "A" and "The" are used by
default. Note that the matching is case-sensitive.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $delprefix(The Beatles)       ==>  "Beatles"
    $delprefix(The Beatles,)      ==>  "The Beatles"
    $delprefix(THE Beatles)       ==>  "THE Beatles"
    $delprefix(THE Beatles,THE)   ==>  "Beatles"
    $delprefix(The Beatles,A,An)  ==>  "The Beatles"

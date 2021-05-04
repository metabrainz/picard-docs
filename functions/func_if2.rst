.. MusicBrainz Picard Documentation Project

.. _func_if2:

$if2
====

| Usage: **$if2(a1,a2,a3,...)**
| Category: conditional

**Description:**

Returns the first non empty argument.  Can be used with an arbitrary number of arguments.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,)
    $set(bar,Something)
    $if2(%foo%,%bar%,Three)    ==>  "Something"
    $if2(,%bar%,Three)         ==>  "Something"
    $if2(,%foo%,%bar%,Three)   ==>  "Something"
    $if2(%foo%, ,%bar%,Three)  ==>  " "
    $if2(%foo%.,%bar%,Three)   ==>  "."
    $if2(%foo%,,Three)         ==>  "Three"
    $if2(%foo%,,,)             ==>  ""

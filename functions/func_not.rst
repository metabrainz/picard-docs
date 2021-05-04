.. MusicBrainz Picard Documentation Project

.. _func_not:

$not
====

| Usage: **$not(x)**
| Category: conditional

**Description:**

Returns true if ``x`` is empty.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,)
    $not(%foo%)  ==>  "1"   (False)

    $not(x)      ==>  ""    (True)
    $not( )      ==>  ""    (True)
    $not()       ==>  Error

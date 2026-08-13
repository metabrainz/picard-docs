.. MusicBrainz Picard Documentation Project

.. _func_get_original:

$get_original
=============

| Usage: **$get_original(name)**
| Category: text
| Implemented: Picard 3.0

**Description:**

Returns the value from original metadata only for the variable ``name`` or an empty string if ``name`` has not been set. If ``name`` is another variable (e.g. ``%indirect%``) the value of the variable will be used as ``name``. This allows the retrieval of dynamically named variables.

.. note::

   Usually you can access the values of a tag by the proper variable name. For example, if your tag is called "rerecorded" you can use ``%rerecorded%``. But the hyphen is not a valid character for a script variable, so ``%re-recorded%`` gives a syntax error. In cases like this you need to use ``$get_original(re-recorded)``.

**Example:**

Assuming that the original value of the tag `foo` is "bar" and the new value is "baz", the following statements will return the values indicated:

.. code-block:: taggerscript

   $get_new(foo)          ==>  "baz"
   $get_original(foo)     ==>  "bar"

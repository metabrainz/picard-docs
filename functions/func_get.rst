.. MusicBrainz Picard Documentation Project

.. _func_get:

$get
====

| Usage: **$get(name)**
| Category: text

**Description:**

Returns the variable ``name`` (equivalent to ``%name%``) or an empty string if ``name`` has not
been set.  If ``name`` is another variable (e.g. ``%indirect%``) the value of the
variable will be used as ``name``.  This allows the retrieval of dynamically named
variables.

.. note::

   Usually you can access the values of a tag by the proper variable name. For example, if your tag
   is called "rerecorded" you can use ``%rerecorded%``. But the hyphen is not a valid character for a
   script variable, so ``%re-recorded%`` gives a syntax error. In cases like this you need to use
   ``$get(re-recorded)``.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,This is foo)
    $set(bar,foo)
    $get(foo)              ==>  "This is foo"
    $get(bar)              ==>  "foo"
    $get(%bar%)            ==>  "This is foo"
    $get(baz)              ==>  "" ('baz' has not been set to a value)

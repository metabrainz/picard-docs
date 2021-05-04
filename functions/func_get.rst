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


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,This is foo)
    $set(bar,foo)
    $get(foo)              ==>  "This is foo"
    $get(bar)              ==>  "foo"
    $get(%bar%)            ==>  "This is foo"
    $get(baz)              ==>  "" ('baz' has not been set to a value)

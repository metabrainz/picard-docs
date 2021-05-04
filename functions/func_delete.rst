.. MusicBrainz Picard Documentation Project

.. _func_delete:

$delete
=======

| Usage: **$delete(name)**
| Category: assignment
| Implemented: Picard 2.1

**Description:**

Unsets the variable ``name`` and marks the tag for deletion.

This is similar to ``$unset(name)`` but also marks the tag for deletion. For example,
running ``$delete(genre)`` will actually remove the "genre" tag from a file when saving.


**Example:**

The following statements will perform the actions indicated:

.. code-block:: taggerscript

    $delete(genre)  ==>  Remove the "genre" tag from a file when saving

.. MusicBrainz Picard Documentation Project

.. _func_unset:

$unset
======

| Usage: **$unset(name)**
| Category: assignment

**Description:**

Unsets the variable ``name``.  The function allows for wildcards to unset certain tags
(works with 'performer:\*', 'comment:\*', and 'lyrics:\*').


**Example:**

The following would unset all performer tags:

.. code-block:: taggerscript

    $unset(performer:*)

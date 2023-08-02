.. MusicBrainz Picard Documentation Project

.. _func_foreach:

$foreach
========

| Usage: **$foreach(name,code,separator="; ")**
| Category: loop
| Implemented: Picard 2.3

**Description:**

Iterates over each element found in the multi-value variable ``name``, executing ``code`` during
each iteration. Before each iteration, the element value is first stored in the variable
``_loop_value`` and the count is stored in the variable ``_loop_count``. This allows the element
or count value to be accessed within the code script.

A literal value representing a multi-value can be substituted for ``name``, using the ``separator``
(or a semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued
variable.

.. note::

   Due to the way that the function parses the ``code`` parameter, multi-value functions that accept the name of the multi-value variable directly (without it being enclosed in percent signs) will not work as expected. To use these functions, the multi-value variable must be expanded by enclosing it with percent signs and re-split by adding "; " (semicolon and single space) as the separator parameter. For example, where you would normally use ``$getmulti(variable,0)`` you have to replace it with ``$getmulti(%variable%,0,; )``.


**Example:**

The following statements will perform the processing indicated:

.. code-block:: taggerscript

    $noop( Mark all listed tags for deletion from the files. )
    $foreach(genre; comment; year,$delete(%_loop_value%))

    $noop( Create an 'artist_count' tag with a count of all artists
           listed for the track. )
    $foreach(%artists%,$set(artist_count,%_loop_count%))

    $noop( Create a separate tag for each artist listed for the
           track as 'artist_1', 'artist_2', etc. )
    $foreach(%artists%,$set(artist_%_loop_count%,%_loop_value%))

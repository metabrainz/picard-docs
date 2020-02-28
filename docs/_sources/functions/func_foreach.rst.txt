.. Picard Function

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


**Example:**

The following statements will perform the processing indicated::

    $foreach(genre; comment; year,$delete(%_loop_value%))
            ==>  Mark all listed tags for deletion from the files.

    $foreach(%artists%,$set(artist_count,%_loop_count%))
            ==>  Create an 'artist_count' tag with a count of all artists listed for the track.

    $foreach(%artists%,$set(artist_%_loop_count%,%_loop_value%))
            ==>  Create a separate tag for each artist listed for the track as 'artist_1', 'artist_2', etc.

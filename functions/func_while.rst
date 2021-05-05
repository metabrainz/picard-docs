.. MusicBrainz Picard Documentation Project

.. _func_while:

$while
======

| Usage: **$while(condition,code)**
| Category: loop
| Implemented: Picard 2.3

**Description:**

Executes ``code`` repeatedly until ``condition`` no longer evaluates to True. For each loop,
the count is stored in the variable ``_loop_count``. This allows the count value to be accessed
within the ``code`` script.

.. note::

    The function limits the maximum number of iterations to 1000 as a safeguard against
    accidentally creating an infinite loop.


**Example:**

The following statement will set ``return`` to "Echo... echo... echo...":

.. code-block:: taggerscript

    $set(return,Echo...)$while($lt(%_loop_count%,2),$set(return,%return% echo...))

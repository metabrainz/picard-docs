.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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

The following statement will set ``return`` to "Echo... echo... echo..."::

    $set(return,Echo...)$while($lt(%_loop_count%,2),$set(return,%return% echo...))

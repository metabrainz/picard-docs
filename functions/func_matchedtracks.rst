.. MusicBrainz Picard Documentation Project

.. _func_matchedtracks:

$matchedtracks
==============

| Usage: **$matchedtracks()**
| Category: information
| Implemented: Picard 0.12

**Description:**

Returns the number of matched tracks within a release.

.. note::

   This function only works in File Naming scripts.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $matchedtracks()  ==>  "3" (if three of the tracks were matched)

.. MusicBrainz Picard Documentation Project

.. _func_is_complete:

$is_complete
============

| Usage: **$is_complete()**
| Category: conditional

**Description:**

Returns true if every track in the album is matched to a single file.

.. note::

   This function only works in File Naming scripts.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $is_complete()  ==>  "1"  (True, if all tracks have been matched)
   $is_complete()  ==>  ""   (False, if not all tracks have been matched)

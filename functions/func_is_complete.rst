.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$is_complete
============

| Usage: **$is_complete()**
| Category: conditional

**Description:**

Returns true if every track in the album is matched to a single file.

.. note::

    This function only works in File Naming scripts.


**Example:**

The following statements will return the values indicated::

    $is_complete()  ==>  "1"  (True, if all tracks have been matched)
    $is_complete()  ==>  ""   (False, if not all tracks have been matched)

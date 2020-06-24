.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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

The following statements will return the values indicated::

    $matchedtracks()  ==>  "3" (if three of the tracks were matched)

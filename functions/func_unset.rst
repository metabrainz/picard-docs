.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$unset
======

| Usage: **$unset(name)**
| Category: assignment

**Description:**

Unsets the variable ``name``.  The function allows for wildcards to unset certain tags
(works with 'performer:\*', 'comment:\*', and 'lyrics:\*').


**Example:**

The following would unset all performer tags::

    $unset(performer:*)

.. Picard Function

$is_complete
============

| Usage: **$is_complete()**
| Category: conditional

**Description:**

Returns true if every track in the album is matched to a single file.

Note that this only works in File Naming scripts.


**Example:**

The following statements will return the values indicated::

    $is_complete()  ==>  "1" (if all tracks have been matched)
    $is_complete()  ==>  ""  (if not all tracks have been matched)

.. MusicBrainz Picard Documentation Project

$startswith
===========

| Usage: **$startswith(text,prefix)**
| Category: conditional
| Implemented: Picard 1.4

**Description:**

Returns true if ``text`` starts with ``prefix``.  Note that the comparison is case-sensitive.


**Example:**

The statements below return the values indicated::

    $startswith(The time is now.,The time)  ==>  "1"  (True)
    $startswith(The time is now.,The TIME)  ==>  ""   (False)
    $startswith(The time is now.,)          ==>  "1"  (True)
    $startswith(,The)                       ==>  ""   (False)
    $startswith(,)                          ==>  "1"  (True)

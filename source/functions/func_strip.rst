.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$strip
======

| Usage: **$strip(text)**
| Category: text

**Description:**

Replaces all whitespace in ``text`` with a single space, and removes leading and trailing spaces.
Whitespace characters include multiple consecutive spaces, and various other unicode characters.
Characters such as newlines '\\n', tabs '\\t' and returns '\\r' are treated as spaces.


**Example:**

The following statements will each return "This text has been stripped."::

    $strip(This text has been stripped.)
    $strip(This text has been stripped.  )
    $strip(  This text has been stripped.  )
    $strip(  This  text has been stripped.)
    $strip(  This  text has been stripped.  )
    $strip(This  text  has  been  stripped.)
    $strip(This  text\rhas\nbeen\tstripped.)

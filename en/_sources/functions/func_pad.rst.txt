.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

$pad
====

| Usage: **$pad(text,length,char)**
| Category: text

**Description:**

Pads the ``text`` to the ``length`` provided by adding as many copies of ``char`` as needed to
the beginning of the string.  For the padded length to be correct, ``char`` must be exactly one
character in length.  If ``length`` is less than the number of characters in ``text``, the
function will return ``text``.  If ``length`` is missing or is not a number, the function will
return an empty string.


**Example:**

The following statements will return the values indicated::

    $pad(abc,5,+)   ==>  "++abc"
    $pad(abc,0,+)   ==>  "abc"
    $pad(abc,5,)    ==>  "abc"
    $pad(abc,5,XY)  ==>  "XYXYabc"  (note final length is incorrect)
    $pad(abc,,+)    ==>  ""
    $pad(abc,x,+)   ==>  ""

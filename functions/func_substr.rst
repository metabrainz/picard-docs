.. MusicBrainz Picard Documentation Project

.. _func_substr:

$substr
=======

| Usage: **$substr(text,start,end)**
| Category: text
| Implemented: Picard 2.3

**Description:**

Returns the substring of ``text`` beginning with the character at the ``start``
index, up to (but not including) the character at the ``end`` index. Indexes are
zero-based. Negative numbers will be counted back from the end of the string. If
the start or end indexes are left blank, they will default to the start and end
of the string respectively.  If the ``start`` index evaluates to a negative
number (e.g.: ``text`` is "abc" and ``start`` is -10), it will default to the
start of the string.  Similarly, if ``end`` index is a number greater than the
number of characters in the string, it will default to the end of the string.
Invalid index values (e.g.: ``start`` greater than ``end``) will return an empty
string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $substr(abcdefg)        ==>  "abcdefg"
    $substr(abcdefg,3)      ==>  "defg"
    $substr(abcdefg,,3)     ==>  "abc"
    $substr(abcdefg,0,3)    ==>  "abc"
    $substr(abcdefg,-3)     ==>  "efg"
    $substr(abcdefg,-6,3)   ==>  "bc"
    $substr(abcdefg,-10,3)  ==>  "abc"
    $substr(abcdefg,3,1)    ==>  ""

.. Picard Function

$find
=====

| Usage: **$find(haystack,needle)**
| Category: text
| Implemented: Picard 2.3

**Description:**

Returns the zero-based index of the first occurrance of ``needle`` in ``haystack``, or
"-1" if ``needle`` was not found.  The comparisons are case-sensitive. If ``needle`` is
blank, it will match the begging of ``haystack`` and return "0". The function does not
support wildcards.


**Example:**

The following statements will return the values indicated::

    $find(abcdef,a)     ==>  "0"
    $find(abcdef,c)     ==>  "2"
    $find(abcdef,cd)    ==>  "2"
    $find(abcdef,g)     ==>  "-1"
    $find(abcdef,B)     ==>  "-1"
    $find(,a)           ==>  "-1"
    $find(abcdef,)      ==>  "1"

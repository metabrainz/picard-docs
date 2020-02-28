.. Picard Function

$pad
====

| Usage: **$pad(text,length,char)**
| Category: text

**Description:**

Pads the ``text`` to the ``length`` provided by adding as many copies of ``char`` as needed to
the beginning of the string.  For the padded length to be correct, ``char`` must be exactly one
character in length.  If ``length`` is less than the number of characters in ``text``, the
function will return ``text``.  If ``length`` is missing or is not a number, the function will
return "".


**Example:**

The following statements will return the values indicated::

    $pad(abc,5,+)   ==>  "++abc"
    $pad(abc,0,+)   ==>  "abc"
    $pad(abc,5,)    ==>  "abc"
    $pad(abc,5,[])  ==>  "[][]abc"
    $pad(abc,,+)    ==>  ""
    $pad(abc,x,+)   ==>  ""

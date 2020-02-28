.. Picard Function

$join
=====

| Usage: **$join(name,text[,separator])**
| Category: multi-value
| Implemented: Picard 2.3

**Description:**

Joins all elements in the multi-value variable ``name``, placing ``text`` between each
element, and returns the result as a string.   A literal value representing a multi-value
can be substituted for ``name``, using the ``separator`` (or a semicolon followed by a
space "; " if not passed) to coerce the value into a proper multi-valued variable.


**Example:**

The following statements will return the values indicated::

    $set(foo,First:A; Second:B; Third:C)
    $join(%foo%, >> )                          ==>  "First:A; Second:B; Third:C"
    $join(%foo%, >> ,:)                        ==>  "First:A; Second:B; Third:C"

    $setmulti(bar,First:A; Second:B; Third:C)
    $join(%bar%, >> )                          ==>  "First:A >> Second:B >> Third:C"
    $join(%bar%, >> ,:)                        ==>  "First >> A; Second >> B; Third >> C"

    $join(First:A; Second:B; Third:C,)         ==>  "First:ASecond:BThird:C"
    $join(First:A; Second:B; Third:C, >> )     ==>  "First:A >> Second:B >> Third:C"
    $join(First:A; Second:B; Third:C, >> ,:)   ==>  "First >> A; Second >> B; Third >> C"

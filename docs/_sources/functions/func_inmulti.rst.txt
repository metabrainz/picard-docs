.. Picard Function

$inmulti
========

| Usage: **$inmulti(%x%,y)**
| Category: conditional
| Implemented: Picard 1.0

**Description:**

Returns true if multi-value variable ``x`` contains exactly ``y`` as one of its values.

Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $setmulti(foo,One; Two; Three)
    $set(bar,Two)
    $inmulti(%foo%,%bar%)  ==>  "1"
    $inmulti(%foo%,Two)    ==>  "1"
    $inmulti(%foo%,two)    ==>  ""
    $inmulti(%foo%,Once)   ==>  ""
    $inmulti(%foo%,w)      ==>  ""
    $inmulti(%foo%,)       ==>  ""

.. Picard Function

$in
===

| Usage: **$in(x,y)**
| Category: conditional
| Implemented: Picard

**Description:**

Returns true, if ``x`` contains ``y``.  Note that comparisons are case-sensitive.


**Example:**

The following statements will return the values indicated::

    $set(foo,ABCDEFG)
    $set(bar,CDE)
    $in(%foo%,%bar%)  ==>  "1"
    $in(ABCDE,CDE)    ==>  "1"
    $in(ABCDE,CE)     ==>  ""
    $in(ABCDE,cde)    ==>  ""
    $in(ABCDE,)       ==>  "1"
    $in(,)            ==>  "1"

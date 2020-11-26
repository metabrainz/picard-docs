.. MusicBrainz Picard Documentation Project

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
    $in(%foo%,%bar%)  ==>  "1"  (True)
    $in(ABCDE,CDE)    ==>  "1"  (True)
    $in(ABCDE,CE)     ==>  ""   (False)
    $in(ABCDE,cde)    ==>  ""   (False)
    $in(ABCDE,)       ==>  "1"  (True)
    $in(,)            ==>  "1"  (True)

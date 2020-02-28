.. Picard Function

$slice
======

| Usage: **$slice(name,start,end[,separator])**
| Category: multi-value
| Implemented: Picard 2.3

**Description:**

Returns a multi-value variable containing the elements between the ``start`` and
``end`` indexes from the multi-value variable ``name``. A literal value representing a
multi-value can be substituted for ``name``, using the ``separator`` (or a
semicolon followed by a space "; " if not passed) to coerce the value into a
proper multi-valued variable.

Indexes are zero based. Negative numbers will be counted
back from the end of the list. If the ``start`` or ``end`` indexes are left blank,
they will default to the start and end of the list respectively.

A typical use might be to create a multi-value variable with all artists in
``%artists%`` except the first, which can be used to create a "feat." list.  This
would look something like ``$setmulti(supporting_artists,$slice(%artists%,1,))``.


**Example:**

The following statements will return the values indicated::

    $set(foo,A; B; C; D; E)
    $slice(%foo%,1)                        ==>  ""

    $setmulti(foo,A; B; C; D; E)
    $slice(%foo%,1)                        ==>  "B; C; D; E"

    $slice(A; B; C; D; E,1)                ==>  "B; C; D; E"
    $slice(A; B; C; D; E,1,3)              ==>  "B; C"
    $slice(A; B; C; D; E,,3)               ==>  "A; B; C"
    $slice(A; B; C; D; E,1,3)              ==>  "B; C"
    $slice(A; B; C; D; E,1,-1)             ==>  "B; C; D"
    $slice(A; B; C; D; E,-4,4)             ==>  "B; C; D"
    $slice(A:A; B:B; C:C; D:D; E:E,,1,:)   ==>  "A"
    $slice(A:A; B:B; C:C; D:D; E:E,-2,,:)  ==>  "D; E:E"
    $slice(A:A; B:B; C:C; D:D; E:E,2,4,:)  ==>  "B; C:C; D"

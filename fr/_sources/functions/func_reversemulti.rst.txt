.. MusicBrainz Picard Documentation Project

$reversemulti
=============

| Usage: **$reversemulti(name[,separator])**
| Category: multi-value
| Implemented: Picard 2.3.1

**Description:**

Returns a copy of the multi-value variable ``name`` with the elements in reverse order. A literal
value representing a multi-value can be substituted for ``name``, using the ``separator`` (or a
semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued
variable.

This function can be used in conjunction with the ``$sortmulti`` function to sort in descending order.


**Example:**

The following statements will return the values indicated::

    $set(foo,A; B; C; D; E)
    $reversemulti(%foo%)            ==>  "A; B; C; D; E"

    $setmulti(bar,A; B; C; D; E)
    $reversemulti(%bar%)            ==>  "E; D; C; B; A"

    $setmulti(baz,A:A; B:B; C:C,:)
    $reversemulti(%baz%)            ==>  "C; B; C; A; B; A"

    $reversemulti(A; B; C; D; E)    ==>  "E; D; C; B; A"
    $reversemulti(A:A; B:B; C:C,:)  ==>  "C:B; C:A; B:A"

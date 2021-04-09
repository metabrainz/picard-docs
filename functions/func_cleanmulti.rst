.. MusicBrainz Picard Documentation Project

$cleanmulti
=============

| Usage: **$cleanmulti(name[,separator])**
| Category: multi-value
| Implemented: Picard 2.7

**Description:**

Returns a copy of the multi-value variable ``name`` with all empty elements removed. A literal
value representing a multi-value can be substituted for ``name``, using the ``separator`` (or a
semicolon followed by a space "; " if not passed) to coerce the value into a proper multi-valued
variable.

The function will return an empty string if ``name`` is missing or if ``separator`` is specified
as an empty string.

**Example:**

The following statements will return the values indicated::

    $setmulti(foo,A; B; C; ; D)
    $cleanmulti(%foo%)            ==>  "A; B; C; D"

    $setmulti(bar,A; B; C; D)
    $cleanmulti(%bar%)            ==>  "A; B; C; D"

    $cleanmulti(A; B; C; ; D)     ==>  "A; B; C; D"
    $cleanmulti(A; B; C; ; D,)    ==>  ""
    $cleanmulti(A; B; C; ; D,:)   ==>  "A; B; C; ; D"

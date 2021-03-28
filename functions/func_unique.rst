.. MusicBrainz Picard Documentation Project

$unique
==========

| Usage: **$unique(name[,case_sensitive[,separator]])**
| Category: multi-value
| Implemented: Picard 2.6

**Description:**

Returns a sorted copy of the multi-value variable ``name`` with duplicate elements removed.
By default, the comparison ignores the case of the elements; however, this can be changed by
setting ``case_sensitive`` to a non-empty value. A literal value representing a multi-value
can be substituted for ``name``, using the ``separator`` (or a semicolon followed by a space
"; " if not passed) to coerce the value into a proper multi-valued variable.  If ``name`` is
missing ``$unique`` will return an empty string.

.. note::

    When performing a (default) case-insensitive comparison, the last matching element will
    be used in the result.  For example, if the multi-value variable contained 'abc', 'Abc',
    'ABc' and 'ABC' in that order, then the element 'ABC' would be included in the output.

**Example:**

The following statements will return the values indicated::

    $setmulti(foo,a; A; B; b; cd; Cd; cD; CD; a; A; b)
    $set(bar,a; A; B; b; cd; Cd; cD; CD; a; A; b)

    $unique(%foo%)     ==>  "A; CD; b"
    $unique(%bar%)     ==>  "a; A; B; b; cd; Cd; cD; CD; a; A; b"
    $unique(%foo%,1)   ==>  "A; B; CD; Cd; a; b; cD; cd"

    $unique(a; A; B; b; cd; Cd; cD; CD; a; A; b)  ==>  "A; CD; b"

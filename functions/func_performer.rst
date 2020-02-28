.. Picard Function

$performer
==========

| Usage: **$performer(pattern[,separator])**
| Category: multi-value
| Implemented: Picard 0.10

**Description:**

Returns the performers where the performance type matches ``pattern`` separated by
``separator`` (or a comma followed by a space ", " if not passed).  If ``pattern``
is blank, then all performers will be returned.  Note that the ``pattern`` to be
matched is case-sensitive.


**Example:**

With the performer tags as 'performer:guitar' = 'Ann', 'performer:rhythm-guitar' =
'Bob' and 'performer:drums' = 'Cindy', the following statements will return the
values indicated::

    $set(foo,guitar)
    $performer(%foo%)          ==>  "Ann, Bob"

    $performer(guitar)         ==>  "Ann, Bob"
    $performer(Guitar)         ==>  ""
    $performer(rhythm-guitar)  ==>  "Bob"
    $performer()               ==>  "Ann, Bob, Cindy"
    $performer(, / )           ==>  "Ann / Bob / Cindy"

.. Picard Function

$endswith
=========

| Usage: **$endswith(text,suffix)**
| Category: conditional
| Implemented: Picard 1.4

**Description:**

Returns true if ``text`` starts with ``suffix``.  Note that the comparison is case-sensitive.


**Example:**

The statements below return the values indicated::

    $endswith(The time is now,is now)  ==>  "1" (True)
    $endswith(The time is now,is NOW)  ==>  "" (False)
    $endswith(The time is now,)        ==>  "1" (True)
    $endswith(,)                       ==>  "1" (True)
    $endswith(,now)                    ==>  "" (False)

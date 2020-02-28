.. Picard Function

$unset
======

| Usage: **$unset(name)**
| Category: assignment

**Description:**

Unsets the variable ``name``.  The function allows for wildcards to unset certain tags
(works with 'performer:\*', 'comment:\*', and 'lyrics:\*').


**Example:**

The following would unset all performer tags::

    $unset(performer:\*)

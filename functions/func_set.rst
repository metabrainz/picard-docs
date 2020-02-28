.. Picard Function

$set
====

| Usage: **$set(name,value)**
| Category: assignment

**Description:**

Sets the variable ``name`` to ``value``.  The value of a variable is available to
other script functions if it is enclosed between '%' characters (e.g. ``%name%``).
If ``name`` is another variable (e.g. ``%indirect%``) the value of the variable
will be used as ``name``.  This allows the creation of dynamically named variables.

Note: To create a variable which can be used for the file naming string, but
which will not be written as a tag in the file, prefix the variable name with
an underscore. ``%something%`` will create a "something" tag; ``%_something%``
will not.


**Example:**

The following statements will return the values indicated::

    $set(comment,Testing)  ==>  'Testing' will be written to the 'comment' tag
    $set(_hidden,Testing)  ==>  '_hidden' variable will not be written

    $set(_base,redirect)
    $set(%_base%,Testing)  ==>  'Testing' will be written to the 'redirect' tag

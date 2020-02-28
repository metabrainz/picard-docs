.. Picard Function

$rreplace
=========

| Usage: **$rreplace(text,pattern,replace)**
| Category: text

**Description:**

Regular expression replace. This function will replace the matching group specified by
``pattern`` with ``replace`` in ``text``.  For more information about regular expressions,
please see the `article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.



**Example:**

The following statements will return the values indicated::

    $rreplace(test \(disc 1\),\\s\\\(disc \\d+\\\),)  ==>  "test"
    $rreplace(test,[t,)                               ==>  "test"

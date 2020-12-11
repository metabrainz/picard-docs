.. MusicBrainz Picard Documentation Project

$rsearch
========

| Usage: **$rsearch(text,pattern)**
| Category: text

**Description:**

Regular expression search. This function will return the first matching group specified by
``pattern`` from ``text``.  For more information about regular expressions, please see the
`article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.

.. note::

   When entering regular expressions into Picard scripts you have to escape a backslash "\\",
   dollar sign "$", comma "," and the left and right parentheses "(" and ")" in order to force
   Picard to not interpret them as part of the script command.  This is done by inserting
   a backslash before the character to be escaped.  For example, the regular expression
   ``^\s*([0-9,\.]*)$`` would have to be entered as ``^\\s*\([0-9\,\\.]*\)\$``.

**Example:**

The following statements will return the values indicated::

    $rsearch(test \(disc 1\),\\\(disc \(\\d+\)\\\))  ==>  "1"
    $rsearch(test \(disc 1\),\\\(disc \\d+\\\))      ==>  "(disc 1)"
    $rsearch(test,x)                                 ==>  ""

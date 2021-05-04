.. MusicBrainz Picard Documentation Project

.. _func_rreplace:

$rreplace
=========

| Usage: **$rreplace(text,pattern,replace)**
| Category: text

**Description:**

Regular expression replace. This function will replace the matching group specified by
``pattern`` with ``replace`` in ``text``.  For more information about regular expressions,
please see the `article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.

.. note::

   When entering regular expressions into Picard scripts you have to escape a backslash "\\",
   dollar sign "$", comma "," and the left and right parentheses "(" and ")" in order to force
   Picard to not interpret them as part of the script command.  This is done by inserting
   a backslash before the character to be escaped.  For example, the regular expression
   ``^\s*([0-9,\.]*)$`` would have to be entered as ``^\\s*\([0-9\,\\.]*\)\$``.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $rreplace(test \(disc 1\),\\s\\\(disc \\d+\\\),)  ==>  "test"
    $rreplace(test,[t,)                               ==>  "test"

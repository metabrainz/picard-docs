.. MusicBrainz Picard Documentation Project

.. _func_rsearch:

$rsearch
========

| Usage: **$rsearch(text,pattern[,group])**
| Category: text

**Description:**

Regular expression search. This function will return the first matching group specified by ``pattern`` from ``text``. For more information about regular expressions, please see the `article on Wikipedia <https://wikipedia.org/wiki/Regular_expression>`_.

If a marked subexpression is defined using parentheses within the search pattern, only the pattern captured by the subexpression will be returned. If more than one marked subexpression is defined and matched, only the pattern captured by the first subexpression will be returned. If more than one marked subexpression is defined and not all are matched, an empty string will be returned. If no subexpression is specified, then the pattern captured by the whole search expression will be returned.

If the optional ``group`` parameter is not provided or is empty, return the first capture group which matched something (including the empty string) or the entire match.

If ``group`` is an integer, return the capture group in the position matching this integer. Otherwise, return the capture group named ``group``, sans surrounding whitespace.

.. note::

   When entering regular expressions into Picard scripts you have to escape a backslash "\\", dollar sign "$", comma "," and the left and right parentheses "(" and ")" in order to force Picard to not interpret them as part of the script command. This is done by inserting a backslash before the character to be escaped. For example, the regular expression ``^\s*([0-9,\.]*)$`` would have to be entered as ``^\\s*\([0-9\,\\.]*\)\$``.

.. note::

   The ``group`` argument was added in Picard v2.14.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $rsearch(test \(disc 1\),\\\(disc \(\\d+\)\\\))  ==>  "1"
   $rsearch(test \(disc 1\),\\\(disc \\d+\\\))      ==>  "(disc 1)"
   $rsearch(test,x)                                 ==>  ""
   $rsearch(test,t)                                 ==>  "t"
   $rsearch(test,s)                                 ==>  "s"
   $rsearch(test,\(e\).*s)                          ==>  "e"
   $rsearch(test,\(e\).*\(s\))                      ==>  "e"
   $rsearch(test,\(e\).*x)                          ==>  ""
   $rsearch(test,\(e\).*\(x\))                      ==>  ""
   $rsearch(disc: 3,\(\\w+\): \(\\d+\),1)           ==>  "disc"
   $rsearch(disc: 3,\(\\w+\): \(\\d+\),2)           ==>  "3"

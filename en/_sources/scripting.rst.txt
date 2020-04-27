..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Scripting
=========

Syntax
------

The syntax is derived from `Foobar2000's titleformat
<https://wiki.hydrogenaud.io/index.php?title=Foobar2000:Titleformat_Reference>`_.
There are three base elements: text, variable and function. Variables consist of
alphanumeric characters enclosed in percent signs (e.g.: ``%artist%``). Functions
start with a dollar sign and end with an argument list enclosed in parentheses (e.g.:
``$lower(...)``).

To use parentheses or commas as-is inside a function call, you must escape them with
a backslash.

Metadata Variables
------------------

See :doc:`variables/variables` for the list of the variables provided by Picard.

Picard's variables can be either simple variables containing a single text
string, or multi-value variables containing multiple text strings. In scripts, multi-value
variables are automatically converted to a single text string by joining the values with a
semicolon ";", except when used with special multi-value functions.

Scripting Functions
-------------------

.. only:: html

   The full list of available scripting functions is available, either
   :doc:`sorted alphabetically <functions/list_by_name>` or
   :doc:`grouped by function type <functions/list_by_type>`.

.. only:: latex

    The full list of available scripting functions is covered in the following chapter.

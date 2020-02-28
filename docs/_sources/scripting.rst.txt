.. Picard Scripting Overview

Scripting
=========

This page describes the simple scripting language implemented in MusicBrainz Picard.


Syntax
------

The syntax is derived from Foobar2000's titleformat. There are three base elements:
text, variable and function. Variables consist of alpha-numeric characters enclosed
in percent signs (e.g. ``%artist%``). Functions start with a dollar sign and end with
an argument list enclosed in parentheses (e.g. ``$lower(...)``).

To use parentheses or commas as-is inside a function call, you must escape them with
a backslash.

Metadata Variables
------------------

See :doc:`variables/variables` for the list of standard variables provided by Picard.

Picard's standard variables can be either simple variables containing a single text
string, or multi-value variables containing multiple text strings. In scripts, multi-value
variables are automatically converted to a single text string by joining the values with a
semicolon ";", except when used with special multi-value functions.

Scripting Functions
-------------------

The full list of available scripting functions is available, either
:doc:`sorted alphabetically <functions/_list_by_name>` or
:doc:`grouped by function type <functions/_list_by_type>`.

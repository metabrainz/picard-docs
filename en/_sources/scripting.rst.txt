.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Scripting
=========

.. index::
   single: scripts

Scripts are used to control some aspects of the operation of Picard.

There are two types of scripts used in Picard: the file naming script and tagging scripts.
These are managed from the "File Naming" and "Scripting" sections of the
:menuselection:`"Options --> Options..."` menu.

Scripts are often discussed in the `MetaBrainz Community Forum <https://community.metabrainz.org/>`_,
and there is a thread specific to `file naming and script snippets
<https://community.metabrainz.org/t/repository-for-neat-file-name-string-patterns-and-tagger-script-snippets/2786/>`_.

.. seealso::

   Please refer to the section on :doc:`Scripts <extending/scripts>` in :doc:`Extending Picard <extending/extending>`
   for additional details about the two types of scripts, including how and when each of the scripts are executed.

.. index::
   single: scripts; syntax

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

.. only:: html

   Scripting Functions
   -------------------

   The full list of available scripting functions is available, either
   :doc:`sorted alphabetically <functions/list_by_name>` or
   :doc:`grouped by function type <functions/list_by_type>`.

.. only:: latex

   .. note::

      The full list of available scripting functions is covered in the following chapter.

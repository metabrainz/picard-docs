..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Tags & Variables
================

This describes both Tags which are saved inside your music files and can be read by your
music player, and Picard variables which can be used in Picard scripts for tagging, file
renaming, and in several other more minor settings.

All tags are also available as variables, but additional variables which start with an underscore
'_' are not saved as Tags within your music files (e.g. ``_my_tag_not_saved``).

Variables are used in scripts by wrapping the name between percent '%' characters (e.g. ``%title%``).

Some variables can contain more than one value (e.g. ``musicbrainz_artistid``), and if you
want to use only one of the values then you will need to use special script functions to access or
set them. To access all the multiple values at once, use the variable normally and Picard will
combine them into a single string separated by a semicolon and space (e.g.: "Item 1; Item 2; Item 3").

If a tag description indicates a later version of Picard than the current official version on the
downloads page, then the tag is beta functionality which will be available in the next official
release. A description of how to gain access to these beta versions for testing can be found on the
`Picard downloads page <https://picard.musicbrainz.org/downloads/>`_ on the website.

.. only:: html

   .. seealso::

      Details:
      :doc:`tags_basic` /
      :doc:`tags_advanced` /
      :doc:`variables_basic` /
      :doc:`variables_advanced` /
      :doc:`variables_classical` /
      :doc:`variables_plugins` /
      :doc:`variables_other_information`

   .. toctree::
      :hidden:

      tags_basic
      tags_advanced
      variables_basic
      variables_advanced
      variables_classical
      variables_plugins
      variables_other_information

.. only:: latex

   .. toctree::

      tags_basic
      tags_advanced
      variables_basic
      variables_advanced
      variables_classical
      variables_plugins
      variables_other_information

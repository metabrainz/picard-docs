.. MusicBrainz Picard Documentation Project


:index:`Tags & Variables <scripts; tags, scripts; variables>`
==============================================================

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

.. only:: html and not epub

   .. seealso::

      Details:
      :doc:`tags_basic` /
      :doc:`tags_advanced` /
      :doc:`variables_basic` /
      :doc:`variables_file` /
      :doc:`variables_advanced` /
      :doc:`variables_classical` /
      :doc:`variables_plugins` /
      :doc:`variables_other_information`

.. toctree::
   :hidden:

   tags_basic
   tags_advanced
   variables_basic
   variables_file
   variables_advanced
   variables_classical
   variables_plugins
   variables_other_information

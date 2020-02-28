..  Picard Scripting Variables

Tags & Variables
================

This page describes both Tags which are saved inside your music files and can be read by your
music player, and Picard variables which can be used in Picard scripts (for tagging, for file
renaming and in several other more minor settings).

All tags are also available as variables, but additional variables which start with an underscore
"_" are not saved as Tags within your music files (for example, ``_my_tag_not_saved``).

Variable are used in scripts by wrapping the name between percent "%" characters (e.g. ``%title%``).

Some variables can contain more than one value (for example, ``musicbrainz_artistid``), and if you
want to use only one of the values then you will need to use special script functions to access /
set them. To access all the multiple values at once, use the variable normally and Picard will
combine them into a single string separated by a semicolon and space "; ".

If a later version of Picard is shown here than the current official version on the downloads page,
then these are beta functionality which will be available in the next official release. A
description of how to gain access to these beta versions for testing can also be found on the
downloads page.


.. References:
.. -----------

Additional information is available for:

* :doc:`tags_basic`
* :doc:`tags_advanced`
* :doc:`variables_basic`
* :doc:`variables_advanced`

.. .. toctree::
..    :maxdepth: 0
..    :caption: References:

..    tags_basic
..    tags_advanced
..    variables_basic
..    variables_advanced

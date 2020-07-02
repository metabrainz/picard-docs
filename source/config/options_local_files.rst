.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


.. _ref-local-files:

Local Files
===========

.. index::
   single: configuration; local files

.. image:: ../images/options-cover-local.png
   :width: 100 %

In this section you can configure the file names to be used by the Local Files cover art provider. If you are trying to collect
more than one image, the naming is important.

The file names are defined using a regular expression. The default is ``^(?:cover|folder|albumart)(.*)\.(?:jpe?g|png|gif|tiff?)$``
which will load files with the name "cover", "folder" or "albumart" and the file extension "jpg", "png", "gif" or "tiff" (e.g.:
"folder.jpg" or "cover.png").

The first part of the regular expression is a non-capture group: ``(?:cover|folder|albumart)``.  Items listed in this group will
not get captured and the default (Front) type will apply.

The second part of the regular expression is a group: ``(.*)``. This is the real capture, so if the file names match any of the
cover art types, they will be tagged as such.

.. note::

   A common mistake is to add all the types into the first (non-capture) group. This means that all the regular file names would be
   thrown into the Front type and cause unexpected results.

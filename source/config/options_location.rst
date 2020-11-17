.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`Location <configuration; cover art location, cover art; location to save>`
====================================================================================

.. only:: html

   .. image:: ../images/options-cover.png
      :width: 100 %

**Embed cover images into tags**

   Enables images to be embedded directly into your music files. While this will use more storage space
   than storing it as a separate image file in the same directory, some music players will only display
   embedded images and don't find the separate files.

**Only embed a front image**

   Embeds only a front image into your music files. Many music players will only display a single embedded
   image, so embedding additional images may not add any functionality.

.. _ref-local-images:

**Save cover images as separate files**

   In the file name mask you can use any variable or function from :doc:`Picard Tags <../variables/variables>`
   and :doc:`Picard Scripting Functions <../functions/list_by_type>`. The mask should not contain a file extension; this is
   added automatically based on the actual image type. The default value is "cover". If you change this to
   "folder", Windows will use it to preview the containing directory.

   In addition to scripting variables already available for a track you can use the following cover art
   specific variables:

   * ``coverart_maintype``: The primary type (e.g.: front, medium, booklet). For front images this will always be "front".
   * ``coverart_types``: Full list of all types assigned to this image.
   * ``coverart_comment``: The cover art comment.

**Overwrite the file if it already exists**

   Check this to replace existing files. This is especially recommended if trying to write "folder" previews
   for Windows.

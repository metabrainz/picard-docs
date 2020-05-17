..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Location
========

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

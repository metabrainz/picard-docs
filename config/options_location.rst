.. MusicBrainz Picard Documentation Project

:index:`Location <configuration; cover art location, cover art; location to save>`
===================================================================================

.. only:: html

   .. image:: images/options-cover.png
      :width: 100 %

**Embed cover images into tags**

   Enables images to be embedded directly into your music files. While this will use more storage space
   than storing it as a separate image file in the same directory, some music players will only display
   embedded images and don't find the separate files.

**Embed only a single front image**

   Embeds only a single front image into your music files.  No other images, regardless of their type,
   will be embedded. Many music players will only display a single embedded image, so embedding additional
   images may not add any functionality.

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

**Save only a single front image as separate file**

   This tells Picard to only save the first "front" image to a separate file with the release.  No other "front"
   images or images of any other type will be saved.  If left unchecked, all "front" images will be saved as separate
   files, along with any other specified image types to be downloaded.

**Always use the primary image type as the file name for non-front images**

   This setting changes how Picard names image files **other than front images**.

   When checked, Picard will use the type of the image (e.g.: back, booklet, etc.) as the filename when saving, as long as
   the type is not front. If the image has been assigned multiple types, then the first type will be used. For example,
   if the image is of types "back" and "raw", then "back" will be used for the filename. If unchecked or if the image is
   of type "front", Picard will use the file name specified in the "Use the following file name for images" setting.

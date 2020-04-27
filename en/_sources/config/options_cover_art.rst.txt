..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Cover Art Options
=================

Note that you must enable :menuselection:`"Options --> Metadata --> Use release relationships"` for Picard to be able
to download cover art from MusicBrainz cover art relationships.

Location
--------

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


Cover Art Providers
-------------------

Picard can download Cover Art from a number of sources, and you can choose which sources you want Picard to
use. You can activate more than one provider and choose the order in which the providers
are queried. Picard will try the providers from top to bottom until an image is returned.

**Cover Art Archive**

   The Cover Art Archive (CAA) is the MusicBrainz archive of cover art in cooperation with the `Internet
   Archive <https://archive.org>`_. The Cover Art Archive is the most comprehensive database of cover art
   (e.g.: front covers, back covers, booklets, CDs).

**CAA Release Group**

   This provider uses the Cover Art Archive cover image assigned to the release group. This is usually the
   image that best describes the release group as a whole or the image with the best visual quality, but is
   not necessarily the exact cover of the release you are tagging. This provider is a good choice if you
   care more about visual quality then having an exact representation of your release. It is also a good
   fallback for the Cover Art Archive provider.

**Sites on the whitelist**

   This will use images provided from whitelisted sites. See `Cover art whitelist
   <https://wiki.musicbrainz.org/History:Style/Relationships/URLs/Cover_art_whitelist>`_ in the Style Guide
   for more information.

   Note: CD Baby and other whitelist sites are no longer being used by MusicBrainz for new Cover Art.

**Local Files**

   Load cover art from local files. The file names to load can be configured in the :ref:`ref-local-files` provider options.

In addition to the built-in cover art providers described above, additional cover art providers can be installed as `plugins
<https://picard.musicbrainz.org/plugins/>`_.

   * **Amazon**: Amazon often has cover art when other sites don't, however while this art is almost always for the correct
     Artist and Album, it may not be the absolute correct cover art for the specific Release with which you have tagged your music.
     *Note: The Amazon cover art provider was built-in in Picard 2.1.3 and earlier versions. For later versions it needs to be
     installed as a separate plugin.*

   * **fanart.tv**: Uses cover art from `fanart.tv <https://fanart.tv/>`_, which focuses on cover art with high visual quality.
     This provider provides cover art representative for the release group and not the individual release.

   * **TheAudioDB**: Uses cover art from `TheAudioDB <https://www.theaudiodb.com/>`_, which focuses on cover art with high visual
     quality. This provider provides cover art representative for the release group and not the individual release.


Cover Art Archive
-----------------
In this section you can decide which types of cover art you would like to download from the Cover Art Archive,
and what quality (size) you want to download. Obviously, the better the quality, the larger the size of the files.

**Download Types**

   When selecting the cover art image types, you can select the types to both include and exclude from the download list.
   CAA images with an image type found in the "Include" list will be downloaded and used unless they also have an image type
   found in the "Exclude" list. Images with types found in the "Exclude" list will never be used. Image types not appearing
   in either the "Include" or "Exclude" lists will not be considered when determining whether or not to download and use a
   CAA image.

   Most music players will display only one piece of cover art for the album, and most people select Front (cover) for that.

**Image Size**

   This identifies what size of image to download from the CAA.  The options are 250px, 500px, 1200px amd full size.  The
   fixed sizes are generated automatically from the full size image, provided that it is greater than or equal to the fixed
   size being generated.  The generated images are square and padded as required if the original image is not square.

**Save only one front image**

   This tells Picard to only save the first "front" image to a separate file with the release.  If left unchecked, all "front"
   images will be saved as separate files.

**Download only approved images**

   When checked, Picard will only download images that have been approved (i.e.: the edit to add the image has been accepted
   and applied).  To allow using images from pending edits, leave this option unchecked.

**Use the first image type as the filename**

   When checked, Picard will use the type of the first image retrieved as the filename when saving all images.  If left
   unchecked, each file will be named according to its image type.

   Note that this will not change the name used for "front" images that has been specified in the :ref:`Save cover images
   <ref-local-images>` section of the general :menuselection:`"Cover Art Options"`.

Since Picard 1.3, you can also decide whether or not to use the image from the release group (if any) if no front image is
found for the release. In this case, the cover may not match the exact release you are tagging (eg.: a 1979 vinyl front cover
may be used in place of the Deluxe 2010 CD reissue).

.. _ref-local-files:

Local Files
-----------
In this section you can configure the file names to be used by the Local Files cover art provider. The file names are defined
using a regular expression. The default is to load files with the name "cover", "folder" or "albumart" and the file extension
"jpg", "png", "gif" or "tiff" (e.g.: "folder.jpg" or "cover.png").

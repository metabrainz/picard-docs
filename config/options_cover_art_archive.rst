.. MusicBrainz Picard Documentation Project

:index:`Cover Art Archive <pair: configuration; cover art archive>`
===================================================================

.. image:: images/options-cover-caa.png
   :width: 100 %

In this section you can decide which types of cover art you would like to download from the Cover Art Archive, and what quality (size) you want to download. Obviously, the better the quality, the larger the size of the files.

**Download only cover art images matching the selected types**

   When selecting the cover art image types, you can select the types to both include and exclude from the download list. CAA images with an image type found in the "Include" list will be downloaded and used unless they also have an image type found in the "Exclude" list. Images with types found in the "Exclude" list will never be used. Image types not appearing in either the "Include" or "Exclude" lists will not be considered when determining whether or not to download and use a CAA image.

   Most music players will display only one piece of cover art for the album, and most people select Front (cover) for that.

**Only use images of the following size**

   This identifies what size of image to download from the CAA. The options are 250px, 500px, 1200px amd full size. The fixed sizes are generated automatically from the full size image, provided that it is greater than or equal to the fixed size being generated. The generated images are square and padded as required if the original image is not square.

   .. note::

      If the selected size is not available, then Picard will use the largest available size below the selected size.

**Download only approved images**

   When checked, Picard will only download images that have been approved (i.e.: the edit to add the image has been accepted and applied). To allow using images from pending edits, leave this option unchecked.

.. note::

   Since Picard 1.3, you can also decide whether or not to use the image from the release group (if any) if no front image is found for the release. In this case, the cover may not match the exact release you are tagging (eg.: a 1979 vinyl front cover may be used in place of the Deluxe 2010 CD reissue).

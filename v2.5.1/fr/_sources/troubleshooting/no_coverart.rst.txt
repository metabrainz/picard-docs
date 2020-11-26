.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


There is no coverart
====================

There are two different problems that often fall under this topic:

.. index::
   single: troubleshooting; no cover art downloaded

Picard isn't finding and downloading any cover art
--------------------------------------------------

**No cover art providers have been enabled in the configuration settings**

   Confirm that the :menuselection:`"Options --> Options... --> Cover Art"` settings have at least one cover
   art provider enabled.  Please see the :doc:`../config/options_cover_art_providers` section for more information.

**There is no cover art available from the selected providers**

   It's possible that the selected release does not have any cover art available from the enabled cover art
   providers. If a cover art image is displayed for the release on the MusicBrainz website, it is possible that
   the image for the release group is being displayed, or it is being provided through a third-party provider
   agreement.  Sometimes this can be addressed by enabling the "CAA Release Group" and "Allowed cover art URLs"
   provider options.

**The selected provider is not currently available**

   On occasion, the server providing the cover art (e.g.: archive.org) is not available, or mirror servers have
   not yet been synchronized with the latest updates.  In this case, you may have to wait for a few minutes before
   retrying your request. Reviewing the details in Picard's log often provides some insight into whether or not
   this is the issue.

**The cover art is still a pending edit**

   If the cover art was recently added, the edit adding the image may not have been accepted and applied yet. You
   can have Picard use the cover art from pending edits by disabling the "Download only approved images" option in
   the Cover Art Archives subsection of the :menuselection:`"Options --> Options... --> Cover Art"` settings.  Please
   see the :doc:`../config/options_cover_art_archive` section for more information.


.. index::
   single: troubleshooting; no cover art displayed

Coverart that is saved with the files isn't displayed
-----------------------------------------------------

**Player doesn't support embedded cover art**

   Check to confirm that your player supports embedded cover art images.  That support is not universal among all
   players.  Some players support embedded images, some support images stored as files in the directory (e.g.:
   "cover.jpg" or "folder.jpg"), and some support both. Picard allows you to specify how the cover art images should
   be saved.  Please see the :doc:`../config/options_location` section of the Coverart options for details.

   You should also confirm that your player supports the version of the tags being written.

   .. seealso::

      For more information please see:
      :doc:`../config/options_tags_compatibility_aac` /
      :doc:`../config/options_tags_compatibility_ac3` /
      :doc:`../config/options_tags_compatibility_id3` /
      :doc:`../config/options_tags_compatibility_wave`

**Embedded cover image too large**

   Even if your cover art image has been properly embedded in the file, it's possible that your player has trouble
   dealing with embedded images over a certain size.  If all else fails, you might try using an image with a smaller
   file size.

..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


There is no coverart
====================

There are two different problems that often fall under this topic:

1. Picard isn't finding and downloading any cover art.
2. Coverart that is saved with the files isn't displayed.

Each of these is addressed below.


Picard isn't finding and downloading any cover art
--------------------------------------------------

**No cover art providers have been enabled in the configuration settings**

   Confirm that the :menuselection:`"Options --> Options... --> Cover Art"` settings have at least one cover
   art provider enabled.  Please see the :doc:`../config/options_cover_art_providers` section for more information.

**There is no cover art available from the selected providers**

   It's possible that the selected release does not have any cover art available from the enabled cover art
   providers. If a cover art image is displayed for the release on the MusicBrainz website, it is possible that
   the image for the release group is being displayed, or it is being provided through a third-party provider
   agreement.  Sometimes this can be addressed by enabling the "CAA Release Group" and "Whitelist" provider
   options.

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


Coverart that is saved with the files isn't displayed
-----------------------------------------------------

**Player doesn't support embedded cover art**

   Check to confirm that your player supports embedded cover art images.  That support is not universal among all
   players.  Some players support embedded images, some support images stored as files in the directory (e.g.:
   "cover.jpg" or "folder.jpg"), and some support both. Picard allows you to specify how the cover art images should
   be saved.  Please see the :doc:`../config/options_location` section of the Coverart options for details.

   You should also confirm that your player supports the version of the tags being written.  Please see the
   :doc:`../config/options_tag_compatibility` section for more information.

**Embedded cover image too large**

   Even if your cover art image has been properly embedded in the file, it's possible that your player has trouble
   dealing with embedded images over a certain size.  If all else fails, you might try using an image with a smaller
   file size.

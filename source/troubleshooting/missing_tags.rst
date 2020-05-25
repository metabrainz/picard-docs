..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


.. index::
   single: troubleshooting; tags not saved

Tags are not updated or saved
=============================

There are typically four reasons that tags may not be written or updated when files are saved:

**Saving tags has not been enabled in the configuration settings**

   Confirm that the :menuselection:`"Options --> Save tags"` setting has been enabled.  See
   :ref:`action_options` for more information.


**Tags are being set in the file naming script**

   Tags created or updated in the file naming script will not be written to the output files. This script is
   only used for developing the file name and directory structure for the output.  If you want to set or
   update a tag value in a script, it must be in a tagging script.  Please see the :doc:`../extending/scripts`
   section for more information about the different types of scripts.


**The tags begin with an underscore**

   Tags whose names begin with an underscore, regardless of how they are created, will not be written to the
   output files.  These are considered variables for use within Picard rather than tags.  Please see the
   :doc:`../variables/variables` section for more information regarding the difference between tags and variables.


**The file type does not support writing tags**

   Confirm that the file type that you are writing actually supports the tags that are to be written.  For example,
   WAV files cannot be tagged due to the lack of a standard for doing so.  Please see the
   :doc:`../config/options_tag_compatibility` section for additional information.

.. MusicBrainz Picard Documentation Project

:index:`Tags are not updated or saved <troubleshooting; tags not saved>`
========================================================================

There are typically four reasons that tags may not be written or updated when files are saved:

**Saving tags has not been enabled in the configuration settings**

   Confirm that the :menuselection:`"Options --> Save tags"` setting has been enabled. See :ref:`action_options` for more information.


**Tags are being set in the file naming script**

   Tags created or updated in the file naming script will not be written to the output files. This script is only used for developing the file name and directory structure for the output. If you want to set or update a tag value in a script, it must be in a tagging script. Please see the :doc:`../extending/scripts` section for more information about the different types of scripts.


**The tags begin with an underscore**

   Tags whose names begin with an underscore, regardless of how they are created, will not be written to the output files. These are considered variables for use within Picard rather than tags. Please see the :doc:`../variables/variables` section for more information regarding the difference between tags and variables.


**The file type does not support writing tags**

   Confirm that the file type that you are writing actually supports the tags that are to be written. Not all file types support all the tags Picard supports.

   Please see the :doc:`../appendices/tag_mapping` section for details about the tags supported by various file formats.

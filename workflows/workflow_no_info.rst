.. MusicBrainz Picard Documentation Project

:index:`When files are not grouped and have little or no existing metadata <workflows; no metadata>`
=====================================================================================================

This is perhaps the worst case scenario, because it provides the greatest chance of tagging your music files
with an incorrect match from the MusicBrainz database.

In this situation, you will need to feed batches of files to Picard to process.  In order to minimize the
performance impact, it is recommended to keep the batches relatively small (i.e.: approximately 200 files at
most in a single batch).  Picard will try to group them into clusters based on their AcoustID fingerprints.

.. note::

   This workflow will likely only partially match the files to a release in each batch processed.  This means
   that an album may not be fully matched, tagged and renamed until multiple batches have been processed.

**1. Load the files**

   Drag the batch of files to process from the browser to the "Unclustered Files" section in the left-hand pane.


**2. Scan the files**

   Select the files in the left-hand pane and scan them using the :menuselection:`Tools --> Scan"` command.
   Picard will attempt to calculate the AcoustID fingerprint for each of the files and then retrieve releases
   with matching recordings.  See the :doc:`../usage/retrieve_scan` section for details.

**3. Match the files to the tracks on the release**

   Drag the files from the left-hand pane and drop them on the release in the right-hand pane.  Check that each
   track on the release is associated with only one file.  The release icon will likely remain silver, indicating
   that not all tracks have been matched to files.  See the :doc:`../usage/match` section for details.


**4. Verify the metadata and cover art**

   Check that the metadata and cover art image for the release and tracks are what you want.  Adjust if required.
   See the :doc:`../usage/coverart` section for details.


**5. Save the files**

   Save the files using the :menuselection:`"File --> Save"` command.  See the :doc:`../usage/save` section for details.

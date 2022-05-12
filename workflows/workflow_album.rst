.. MusicBrainz Picard Documentation Project

:index:`When files are grouped by album <workflows; files grouped by album>`
=============================================================================

If the music files to be processed are already grouped into folders by album, then the process of looking up
the release in the MusicBrainz database is greatly simplified because Picard works best when processing one
album at a time.

**1. Load the files**

   Drag the files or folder from the browser to the "Unclustered Files" section in the left-hand pane.


**2. Cluster and lookup the files**

   Select the files in the left-hand pane and combine them into an album cluster using the :menuselection:`"Tools
   --> Cluster"` command.  Select the cluster in the left-hand pane and initiate the lookup using the
   :menuselection:`"Tools --> Lookup"` command.  See the :doc:`/usage/retrieve_lookup` section for details.


**3. Select the correct release**

   If there is only one release that matches the lookup, it will be loaded automatically.  Before proceeding,
   please check to ensure that it properly matches your album (e.g.: release country, date and label,
   catalog number, barcode, media type, and cover art).  This is especially important if you are going to submit
   any information such as AcoustID fingerprints.


**4. Match the files to the tracks on the release**

   Drag the files from the left-hand pane and drop them on the release in the right-hand pane.  Check that each
   track on the release is associated with only one file.  The release icon should turn gold.  See the
   :doc:`/usage/match` section for details.


**5. Verify the metadata and cover art**

   Check that the metadata and cover art image for the release and tracks are what you want.  Adjust if required.
   See the :doc:`/usage/coverart` section for details.


**6. Save the files**

   Save the files using the :menuselection:`"File --> Save"` command.  See the :doc:`/usage/save` section for details.


**7. Calculate and submit AcoustID fingerprints**

   :index:`This step is optional <acoustic fingerprint; submitting>`, but appreciated because it will help identify the files for others to look up for tagging.

   Select the album entry in the right-hand pane and calculate the AcoustID fingerprints using :menuselection:`"Tools -->
   Generate AcoustID Fingerprints"`.  Once the fingerprints have been calculated, submit them using :menuselection:`"Files -->
   Submit AcoustIDs"`.

   .. note::

      AcoustID fingerprints should only be submitted after the files have been tagged with MusicBrainz metadata, and you have
      verified that the files have been matched to the correct track on the proper release.

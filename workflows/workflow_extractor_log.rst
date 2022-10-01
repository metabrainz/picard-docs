.. MusicBrainz Picard Documentation Project

:index:`When the ripper log file is available <workflows; ripper log, lookup; ripper log, EAC; lookup log, XLD; lookup log, Whipper; lookup log, fre:ac; lookup log, dBpoweramp; lookup log>`
=============================================================================================================================================================================================

This option was added to Picard in version 2.8, and supports the use of log files produced by :ref:`supported
popular CD file rippers <faq_supported_rippers>`. Because the log files of these rippers contain sufficient
information to generate the CD table of contents they can be used in place of reading the CD. As with reading
the CD itself, this method provides the greatest chance of tagging your music files with the most accurate
match from the MusicBrainz database.  It is also one of the easier methods for looking up the release.

**1. Lookup the CD on MusicBrainz**

   Use the ripper log file to look up the release automatically by selecting the
   :menuselection:`"Tools --> Lookup CD --> From CD ripper log file..."` command. This will open a
   file browser dialog to allow you to select the log file to process. See the :doc:`/usage/retrieve_lookup_cd`
   section for detailed instructions.


**2. Select the correct release**

   A list of all releases matching the toc of the CD will be displayed for selection, with an option to submit
   the disc id if none of the releases are a match to your CD.  Before proceeding, please check to ensure that
   the release you select properly matches your CD (e.g.: release country, date and label, catalog number,
   barcode, media type, and cover art).  This is especially important if you are going to submit any
   information such as acoustic features to AcousticBrainz or AcoustID fingerprints.

   .. image:: /usage/images/cd_lookup_1.png
      :width: 100%


**3. Load the files**

   Drag the files or folder from the browser to the "Unclustered Files" section in the left-hand pane.  You do not
   need to scan or cluster them.


**4. Match the files to the tracks on the release**

   Drag the files from the left-hand pane and drop them on the release in the right-hand pane.  Check that each
   track on the release is associated with only one file.  The release icon should turn gold.  See the
   :doc:`/usage/match` section for details.


**5. Verify the metadata and cover art**

   Check that the metadata and cover art image for the release and tracks are what you want.  Adjust if required.
   See the :doc:`/usage/coverart` section for details.


**7. Save the files**

   Save the files using the :menuselection:`"File --> Save"` command.  See the :doc:`/usage/save` section for details.


**8. Calculate and submit AcoustID fingerprints**

   :index:`This step is optional <acoustic fingerprint; submitting>`, but appreciated because it will help identify
   the files for others to look up for tagging.

   Select the album entry in the right-hand pane and calculate the AcoustID fingerprints using
   :menuselection:`"Tools --> Generate AcoustID Fingerprints"`.  Once the fingerprints have been calculated, submit
   them using :menuselection:`"Files --> Submit AcoustIDs"`.

   .. note::

      AcoustID fingerprints should only be submitted after the files have been tagged with MusicBrainz metadata, and you have
      verified that the files have been matched to the correct track on the proper release.

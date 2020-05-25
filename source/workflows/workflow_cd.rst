..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


When the CD is available
========================

.. index::
   single: work flows; cd

This is perhaps the best case scenario, because it provides the greatest chance of tagging your music files
with the most accurate match from the MusicBrainz database.  It is also one of the easier methods for looking
up the release.

**1. Rip the CD to music files**

   Extract the music filed from the CD using your favorite ripping program (e.g.: `Exact Audio Copy
   <http://exactaudiocopy.de/>`_ for Windows or `Whipper <https://github.com/whipper-team/whipper>`_ for Linux).
   The format for the output files depends on your personal preference and the formats supported by your player.
   A popular format is FLAC, which is a compressed lossless format.


**2. Lookup the CD on MusicBrainz**

   With the CD in the drive, it can be looked up automatically using the :menuselection:`"Tools --> Lookup CD"` command.
   See the :doc:`../usage/retrieve_lookup_cd` section for detailed instructions.


**3. Select the correct release**

   If there is only one release that matches the disc id for your disc, it will be loaded automatically.  Before
   proceeding, please check to ensure that it properly matches your CD (e.g.: release country, date and label,
   catalog number, barcode, media type, and cover art).  This is especially important if you are going to submit
   any information such as disc id or AcoustID fingerprints.


**4. Load the files**

   Drag the files or folder from the browser to the "Unclustered Files" secion in the left-hand pane.  You do not
   need to scan or cluster them.


**5. Match the files to the tracks on the release**

   Drag the files from the left-hand pane and drop them on the release in the right-hand pane.  Check that each
   track on the release is associated with only one file.  The release icon should turn gold.  See the
   :doc:`../usage/match` section for details.


**6. Verify the metadata and cover art**

   Check that the metadata and cover art image for the release and tracks are what you want.  Adjust if required.
   See the :doc:`../usage/coverart` section for details.


**7. Save the files**

   Save the files using the :menuselection:`"File --> Save"` command.  See the :doc:`../usage/save` section for details.


.. index::
   single: acoustic fingerprint; submitting

**8. Calculate and submit AcoustID fingerprints**

   This step is optional, but appreciated because it will help identify the files for others to look up for tagging.

   Select the album entry in the right-hand pane and calculate the AcoustID fingerprints using :menuselection:`"Tools -->
   Generate AcoustID Fingerprints"`.  Once the fingerprints have been calculated, submit them using :menuselection:`"Files -->
   Submit AcoustIDs"`.

   .. note::

      AcoustID fingerprints should only be submitted after the files have been tagged with MusicBrainz metadata, and you have
      verified that the files have been matched to the correct track on the proper release.

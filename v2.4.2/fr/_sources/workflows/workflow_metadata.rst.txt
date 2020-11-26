.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


When files are not grouped but have some metadata
=================================================

.. index::
   single: workflows; files not grouped

In this situation, you will need to feed batches of files to Picard to process.  In order to minimize the
performance impact, it is recommended to keep the batches relatively small (i.e.: approximately 200 files at
most in a single batch).  Picard will try to group them into clusters based on the metadata currently
existing in the files.

.. note::

   This workflow will likely only partially match the files to a release in each batch processed.  This means
   that an album may not be fully matched, tagged and renamed until multiple batches have been processed.

**1. Load the files**

   Drag the batch of files to process from the browser to the "Unclustered Files" secion in the left-hand pane.


**2. Cluster and lookup the files**

   Select the files in the left-hand pane and combine them into album clusters using the :menuselection:`Tools
   --> Cluster"` command.  Picard will attempt to cluster the files based on their existing metadata.  Select
   the desired cluster(s) in the left-hand pane and initiate the lookup using the :menuselection:`Tools -->
   Lookup"` command.  See the :doc:`../usage/retrieve_lookup` section for details.

**3. Match the files to the tracks on the release**

   Drag the files from the left-hand pane and drop them on the release in the right-hand pane.  Check that each
   track on the release is associated with only one file.  The release icon will likely remain silver, indicating
   that not all tracks have been matched to files.  See the :doc:`../usage/match` section for details.


**4. Verify the metadata and cover art**

   Check that the metadata and cover art image for the release and tracks are what you want.  Adjust if required.
   See the :doc:`../usage/coverart` section for details.


**5. Save the files**

   Save the files using the :menuselection:`"File --> Save"` command.  See the :doc:`../usage/save` section for details.


.. note::

   It is not recommended to submit AcoustID fingerprints for files matched in this way, because it is virtually
   impossible to verify that your files actually match the recordings being matched.

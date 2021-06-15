.. MusicBrainz Picard Documentation Project

:index:`Submitting Cluster as a Release <cluster; submitting, release; submitting>`
====================================================================================

Picard can assist you in submitting information to the MusicBrainz database by automatically
populating the submission form on the website with data from your files.  This is typically
used when you have the music files for an album, but it is not yet available on MusicBrainz.

To use this functionality, the steps to follow are:

**1. Load the files**

   Drag the batch of files to process from the browser pane to the "Unclustered Files" section in the clustering pane.

   .. image:: images/submit_cluster_1.png
      :width: 100%

.. raw:: latex

   \clearpage

**2. Cluster the files**

   Select the files in the clustering pane and combine them into album clusters using the :menuselection:`"Tools
   --> Cluster"` command.  Picard will attempt to cluster the files based on their existing metadata.  Depending
   on the quality of the metadata, you may need to manually add items to the cluster or remove items from the
   cluster to ensure that it is complete for the album, and does not contain any additional files.

   .. image:: images/submit_cluster_2.png
      :width: 100%

.. raw:: latex

   \clearpage

**3. Submit the cluster**

   Once you have the proper files in the cluster and it is complete for the album, you can submit it to MusicBrainz
   by selecting the cluster and right-click to bring up the context menu.  From there you should see an option to
   :menuselection:`"Submit cluster as release..."`.

   .. image:: images/submit_cluster_3.png
      :width: 100%

.. raw:: latex

   \clearpage

**4. Confirm submitted information**

   When the option is selected, the system will submit a request to add the information to MusicBrainz, and you will
   be presented with a confirmation screen in your browser.  You can see the information that will be submitted by
   expanding the "Data submitted with this request" link.  Selecting :kbd:`Continue` will open an "Add Release" edit
   screen with the fields populated with your information.

   .. image:: images/submit_cluster_4.png
      :width: 100%

**5. Complete the submission**

   Selecting :kbd:`Continue` will open an "Add Release" edit screen with the fields populated with your information.
   From here you can check and submit your edit as if you had entered all of the information manually.

   .. note::

      Before submitting the edit, you should check that all of the information has been correctly entered and that
      artist and release groups have been matched to existing items as appropriate.  You should also add an edit note
      citing the source of the information.

.. raw:: latex

   \clearpage

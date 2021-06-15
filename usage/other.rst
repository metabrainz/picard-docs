.. MusicBrainz Picard Documentation Project

Other Picard Tasks
==================

.. only:: html

   In addition to the general functionality of Picard tagging and organizing your audio files,
   there are some other tasks that it can perform:

   **Attaching disc ids to releases on MusicBrainz**

      This will read the id of a cd and attach it to a specified release in the MusicBrainz
      database.  This will allow the release to be included in the list provided when someone
      uses the "Lookup CD" function.


   **Submitting track acoustic fingerprints**

      This will calculate the acoustic fingerprints for the selected tracks and submit them to
      the AcoustID database.

   **Generating tags from file names**

      This will extract tags such as track number and title from the file name.

   **Submitting cluster as a release**

      You can submit a cluster as a release to the MusicBrainz database.  This functionality has
      long been available through a plugin, but has been included within Picard itself as of v2.7.

   .. seealso::

      Step-by-step detailed instructions:
      :doc:`attach_disc_id` /
      :doc:`submit_acoustid` /
      :doc:`tags_from_file_names` /
      :doc:`submit_cluster_as_release`

.. .. only:: latex

..    Each of these steps are described in detail in the following sections.

.. toctree::
   :hidden:

   attach_disc_id
   submit_acoustid
   tags_from_file_names
   submit_cluster_as_release

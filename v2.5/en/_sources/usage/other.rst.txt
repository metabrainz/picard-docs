.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Other Picard Tasks
==================

In addition to the general functionality of Picard tagging and organizing your audio files,
there are some other tasks that it can perform:

.. only:: html

   **Attaching disc ids to releases on MusicBrainz**

      This will read the id of a cd and attach it to a specified release in the MusicBrainz
      database.  This will allow the release to be included in the list provided when someone
      uses the "Lookup CD" function.


   **Submitting track acoustic fingerprints**

      This will calculate the acoustic fingerprints for the selected tracks and submit them to
      the AcoustID database.

   **Generating tags from file names**

      This will extract tags such as track number and title from the file name.

.. .. only:: latex

..    Each of these steps are described in detail in the following sections.

.. only:: html

   .. seealso::

      Step-by-step detailed instructions:
      :doc:`attach_disc_id` /
      :doc:`submit_acoustid` /
      :doc:`tags_from_file_names`

.. toctree::
   :hidden:

   attach_disc_id
   submit_acoustid
   tags_from_file_names

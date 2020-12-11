.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Using Picard
============

There are four stages to using Picard to process your audio files:

.. only:: html

   **Retrieving album information from MusicBrainz**

      This stage identifies the album on MusicBrainz that will provide the information used
      for tagging the files, and retrieves the metadata from the MusicBrainz database.  There
      are a few different methods available, depending on the information currently available
      on your system (e.g.: metadata existing in the files, or having the source CD available).


   **Matching audio files to tracks**

      This stage is where individual files are matched to specific tracks in the information
      retrieved from the MusicBrainz database.


   **Selecting Cover Art**

      Depending on the option settings, you can change or confirm the cover art to save with a
      track or album.


   **Saving the updated audio files**

      This stage is where Picard updates the matched files with the metadata retrieved in the
      first stage, based on the settings configured in the Options.  This may also include
      renaming the files and placing them in a different directory.

.. .. only:: latex

..    Each of these steps are described in detail in the following sections.

.. only:: html

   .. seealso::

      Details:
      :doc:`retrieve` /
      :doc:`match` /
      :doc:`coverart` /
      :doc:`save`

.. toctree::
   :hidden:

   retrieve
   match
   coverart
   save

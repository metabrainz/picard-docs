..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Using Picard
============

There are three stages to using Picard to process your audio files:

1. **Retrieving album information from MusicBrainz**

   | This stage identifies the album on MusicBrainz that will provide the information used
     for tagging the files, and retrieves the metadata from the MusicBrainz database.  There
     are a few different methods available, depending on the information currently available
     on your system (e.g.: metadata exising in the files, or having the source CD available).
   |

2. **Matching audio files to tracks**

   | This stage is where individual files are matched to specific tracks in the information
     retrieved from the MusicBrainz database.
   |

3. **Saving the updated audio files**

   | This stage is where Picard updates the matched files with the metadata retrieved in the
     first stage, based on the settings configured in the Options.  This may also include
     renaming the files and placing them in a different directory.
   |

.. only:: latex

   Each of these steps are described in detail in the following sections.

.. only:: html

   .. seealso::

      Details:
      :doc:`retrieve` /
      :doc:`match` /
      :doc:`save`

.. toctree::
   :hidden:

   retrieve
   match
   save

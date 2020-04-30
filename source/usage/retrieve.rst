..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Retrieving Album information
============================

There are basically four methods used to retrieve album information from the MusicBrainz database.

.. only:: latex

   Lookup CD
   ---------

.. only:: html

   **Lookup CD**

This is the preferred method of automatically identifying the album to retrieve, and
should be used when you have the CD available.  Typically this would be used right after ripping the
audio files from the CD.  When initiated, the table of contents (toc) is read from the CD and a request
is sent to MusicBrainz to return a list of the releases that match the toc.  If there are any matches,
then they will be listed for you to select the one to use.  If there are no matches or none of the
matches are correct, you can search the database manually for the matching album, and are given the
option of attaching the toc from your CD to the selected release for future lookup.

.. only:: latex

   .. include:: retrieve_lookup_cd_steps.txt


.. only:: latex

   Lookup Files
   ------------

.. only:: html

   **Lookup Files**

Need to add details here.


.. only:: latex

   Scan Files
   ----------

.. only:: html

   **Scan Files**

Need to add details here.


.. only:: latex

   Manual Lookup
   -------------

.. only:: html

   **Manual Lookup**

Need to include details here.


.. only:: html

   .. toctree::
      :hidden:

      retrieve_lookup_cd
      retrieve_lookup
      retrieve_scan
      retrieve_browser

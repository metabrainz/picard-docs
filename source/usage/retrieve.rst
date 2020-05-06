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

   :doc:`Lookup CD <retrieve_lookup_cd>`

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

   :doc:`Lookup Files <retrieve_lookup>`

If you don't have the CD available, and your files are grouped by album, this is the preferred method of
automatically identifying the album to retrieve.  This is done by grouping the files into album clusters in
Picard and then perform the lookup.  Picard will try to match the entire set of clustered files to the same
release.

.. only:: latex

   .. include:: retrieve_lookup_steps.txt


.. only:: latex

   Scan Files
   ----------

.. only:: html

   :doc:`Scan Files <retrieve_scan>`

If your files are not grouped into albums and you don't have the CD available, this is the only remaining method of
automatically identifying the album to retrieve.  This is done by scanning the files to obtain their AcoustID
fingerprints and then perform the lookup for the individual files by fingerprint.  The album(s) matching the files
will show up in the right-hand pane based on a "best match" using the Preferred Releases settings in the Metadata options.

.. only:: latex

   .. include:: retrieve_lookup_steps.txt


.. only:: latex

   Lookup in Browser
   -----------------

.. only:: html

   :doc:`Lookup in Browser <retrieve_browser>`

If none of the automated methods are available, or don't produce the desired results, you have the option of retrieving
the album information by having Picard initiate a search on the MusicBrainz website using your web browser.  There are two
methods of initiating this search. The first method searches based on the tag information from the selected files.

.. only:: latex

   .. include:: retrieve_browser_steps.txt


.. only:: latex

   Manual Lookup
   -------------

.. only:: html

   :doc:`Manual Lookup <retrieve_manual>`

The second browser search method uses manually entered information as the search criterion.

.. only:: latex

   .. include:: retrieve_manual_steps.txt


.. only:: html

   .. toctree::
      :hidden:

      retrieve_lookup_cd
      retrieve_lookup
      retrieve_scan
      retrieve_browser
      retrieve_manual

.. MusicBrainz Picard Documentation Project

Scan Files
==========

The steps to follow to :index:`scan and lookup files <scan files>` are:

Step 1
-------

Add your files using :menuselection:`"Files --> Add Files..."` or :menuselection:`"Files --> Add Folder..."`.

For ease of use it is recommended to use the internal File Browser to manage file system interactions. This is enabled from :menuselection:`"View --> File Browser"`.

.. only:: not latex

   .. image:: images/lookup_1.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_1.png
      :width: 65%
      :align: center


Step 2
-------

Drag the selected directory or files to the "Unclustered Files" folder, and wait for Picard to process the files - the names will turn from grey to black.

.. only:: not latex

   .. image:: images/lookup_2.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_2.png
      :width: 65%
      :align: center


Step 3
-------

Select the desired files and use :menuselection:`"Tools --> Scan"` to scan the files to determine their AcoustID fingerprints and lookup using this information. The album(s) matching the files will show up in the right-hand pane based on a "best match" using the Preferred Releases settings in the Metadata options.

A music symbol in front of a track number in the right-hand pane indicates that there has been no file assigned to the track.

.. only:: not latex

   .. image:: images/lookup_5.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_5.png
      :width: 75%
      :align: center

If no album was retrieved, or if the album retrieved was incorrect, you may have to try a different method such as clustering the files or a browser lookup.

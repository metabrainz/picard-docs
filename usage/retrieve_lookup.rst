.. MusicBrainz Picard Documentation Project

Lookup Files
============

The steps to follow to :index:`lookup files` are:

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
      :width: 75%
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
      :width: 75%
      :align: center

Step 3
-------

Use :menuselection:`"Tools --> Cluster"` to group the files into album :index:`clusters <pair: cluster; lookup>`.

.. only:: not latex

   .. image:: images/lookup_3.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_3.png
      :width: 75%
      :align: center

Step 4
-------

Select a clustered album and use :menuselection:`"Tools --> Lookup"` to lookup the cluster. Depending on your previous metadata, the album will show up in the right-hand pane.

A music symbol in front of a track number in the right-hand pane indicates that there has been no file assigned to the track.

.. only:: not latex

   .. image:: images/lookup_5.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_5.png
      :width: 75%
      :align: center

If you're not sure that the album retrieved is correct, you can use :menuselection:`"Tools --> Show other album versions..."` to open a window displaying all releases matched. From this window, you can select a different matching version to use, or refine the search criteria and perform a new search.

.. only:: not latex

   .. image:: images/lookup_other_matching.png
      :align: center

   |

.. only:: latex

   .. image:: images/lookup_other_matching.png
      :width: 100%
      :align: center

If no album was retrieved, or if the album retrieved was incorrect, you may have to try a different method such as scanning the files or a manual lookup.

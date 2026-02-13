.. MusicBrainz Picard Documentation Project

:index:`Submitting Acoustic Fingerprints <AcoustID; submitting, acoustic fingerprint; submitting, fingerprint; submitting>`
===========================================================================================================================

Acoustic fingerprints are very useful for identifying tracks and recordings, allowing them to be looked up in the MusicBrainz database. Thus, it is very valuable to add them when you are tagging files. Note that an acoustic fingerprint is **not** an AcoustID. Please see the :doc:`../tutorials/acoustid` tutorial for additional information.

.. note::

   When using Picard to submit acoustic fingerprints, it is recommended to enable the Fingerprint column in the table view in the right-hand pane. This is done by right-clicking the column header and checking the box beside "Fingerprint status". This will display an icon indicating whether the AcoustID was calculated and whether it ready for submission (red = unsubmitted, grey = already submitted).

There are two methods for submitting acoustic fingerprints, depending on the workflow that you are using to identify the releases that you are tagging. Note that both methods require that you first match your audio files to release and track information from the MusicBrainz database. See the :doc:`retrieve` and :doc:`match` sections for more information about retrieving release information and matching audio files to releases.

The steps to follow to submit acoustic fingerprints for each of the two workflows are:

.. raw:: latex

   \clearpage

Submitting when using Scan to identify the release
--------------------------------------------------

Step 1
+++++++

Load files into the clustering pane. Select the files and select :menuselection:`"Tools --> Scan"`, or click the "Scan" button.

.. only:: not latex

   .. image:: images/submit_acoustid_1.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_1.png
      :align: center
      :width: 75%

.. .. raw:: latex

..    \clearpage

Step 2
+++++++

If the files are matched to a track and move to the right-hand pane, they already exist in the AcoustID database and do not need to be re-submitted. The "Submit" button will remain disabled.

.. only:: not latex

   .. image:: images/submit_acoustid_2.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_2.png
      :align: center
      :width: 75%


Step 3
+++++++

If the files are not matched, or you manually move them to match to a different track they could be submitted. The AcoustID icon for the tracks will show up in red (i.e.: unsubmitted status) and the "Submit" button will be enabled.

.. only:: not latex

   .. image:: images/submit_acoustid_3.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_3.png
      :align: center
      :width: 75%

.. .. raw:: latex

..    \clearpage

Step 4
+++++++

Clicking the "Submit" button will only submit the fingerprints for the files identified in Step 3. The AcoustID icon for the tracks will change to grey (i.e.: submitted status) and the "Submit" button will be disabled.

.. only:: not latex

   .. image:: images/submit_acoustid_4.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_4.png
      :align: center
      :width: 75%

.. raw:: latex

   \clearpage

Submitting when not using Scan to identify the release
------------------------------------------------------

Step 1
+++++++

Make sure that the files are properly matched to tracks on a release in the right-hand pane.

.. only:: not latex

   .. image:: images/submit_acoustid_5.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_5.png
      :align: center
      :width: 75%

.. .. raw:: latex

..    \clearpage

Step 2
+++++++

Select the files in the right-hand pane and select :menuselection:`"Tools --> Generate AcoustID fingerprints"`. This will calculate the acoustic fingerprints for the selected files.

.. only:: not latex

   .. image:: images/submit_acoustid_6.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_6.png
      :align: center
      :width: 75%

.. raw:: latex

   \par

.. note::

   The "Generate AcoustID fingerprints" action button can be added to the button bar by changing the settings in the User Interface options.

The AcoustID icon for the tracks will show up in red (i.e.: unsubmitted status) and the "Submit" button will be enabled.

.. only:: not latex

   .. image:: images/submit_acoustid_7.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_7.png
      :align: center
      :width: 75%

.. .. raw:: latex

..    \clearpage

Step 3
+++++++

Clicking the "Submit" button will submit the fingerprints for the files. The AcoustID icon for the tracks will change to grey (i.e.: submitted status) and the "Submit" button will be disabled.

.. only:: not latex

   .. image:: images/submit_acoustid_8.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_acoustid_8.png
      :align: center
      :width: 75%

.. raw:: latex

   \clearpage

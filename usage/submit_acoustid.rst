.. MusicBrainz Picard Documentation Project

:index:`Submitting Acoustic Fingerprints <AcoustID; submitting, acoustic fingerprint; submitting, fingerprint; submitting>`
============================================================================================================================

Acoustic fingerprints are very useful for identifying tracks and recordings, allowing them to be
looked up in the MusicBrainz database. Thus, it is very valuable to add them when you are tagging
files.  Please see the :doc:`../tutorials/acoustid` tutorial for additional information.

.. note::

   When using Picard to submit acoustic fingerprints, it is recommended to enable the Fingerprint
   column in the table view in the right-hand pane.  This is done by right-clicking the column header
   and checking the box beside "Fingerprint status".  This will display an icon indicating whether the
   AcoustID was calculated and whether it ready for submission (red = unsubmitted, grey = already
   submitted).

There are two methods for submitting acoustic fingerprints, depending on the workflow that you are
using to identify the releases that you are tagging.  The steps to follow to submit acoustic
fingerprints for each of the two workflows are:

Submitting when using Scan to identify the release
--------------------------------------------------

1. Load files into the clustering pane.  Select the files and click the "Scan" button, or select
   :menuselection:`"Tools --> Scan"`.

   .. image:: images/submit_acoustid_1.png
      :width: 100%

   .. raw:: latex

      \clearpage

2. If the files are matched to a track and move to the right-hand pane, they already exist in the
   AcoustID database and do not need to be re-submitted.  The "Submit" button will remain disabled.

   .. image:: images/submit_acoustid_2.png
      :width: 100%

   |

3. If the files are not matched, or you manually move them to match to a different track they could
   be submitted.  The AcoustID icon for the tracks will show up in red (i.e.: unsubmitted status) and
   the "Submit" button will be enabled.

   .. image:: images/submit_acoustid_3.png
      :width: 100%

   .. raw:: latex

      \clearpage

4. Clicking the "Submit" button will only submit the fingerprints for the files identified in Step 3.
   The AcoustID icon for the tracks will change to grey (i.e.: submitted status) and the "Submit"
   button will be disabled.

   .. image:: images/submit_acoustid_4.png
      :width: 100%

   |


Submitting when not using Scan to identify the release
------------------------------------------------------

1. Make sure that the files are properly matched to tracks on a release in the right-hand pane.

   .. image:: images/submit_acoustid_5.png
      :width: 100%

   .. raw:: latex

      \clearpage

2. Select the files in the right-hand pane and select :menuselection:`"Tools --> Generate AcoustID fingerprints"`.
   This will calculate the acoustic fingerprints for the selected files.

   .. image:: images/submit_acoustid_6.png
      :width: 100%

   .. raw:: latex

      \par

   .. note::

      The "Generate AcoustID fingerprints" action button can be added to the button bar by changing the settings
      in the User Interface options.

   The AcoustID icon for the tracks will show up in red (i.e.: unsubmitted status) and the "Submit" button will
   be enabled.

   .. image:: images/submit_acoustid_7.png
      :width: 100%

   .. raw:: latex

      \clearpage

3. Clicking the "Submit" button will submit the fingerprints for the files. The AcoustID icon for the tracks will
   change to grey (i.e.: submitted status) and the "Submit" button will be disabled.

   .. image:: images/submit_acoustid_8.png
      :width: 100%

.. raw:: latex

   \clearpage

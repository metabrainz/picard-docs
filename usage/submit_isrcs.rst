.. MusicBrainz Picard Documentation Project

:index:`Submitting ISRCs <ISRC; submitting>`
==============================================

ISRCs are very useful for identifying tracks and recordings, so it is valuable to add them when you are tagging files. Picard can be used to submit ISRCs to the MusicBrainz database.

You can submit ISRCs for tracks that are already in the MusicBrainz database, provided they have ISRCs available in their metadata. If you have a CD with ISRCs, you can enable the "Read ISRCs from CD" option in the :doc:`../config/options_cdlookup` to read them from the CD when you do a disc lookup.

To submit ISRCs, select :menuselection:`"File --> Submit ISRCs"` or click the "Submit ISRCs" button if you have it included in your action toolbar. Picard will check that the ISRCs are valid, that the same ISRC doesn't appear on more than one track on the release, and that the ISRCs are not already present in the database. If all checks pass, the ISRCs will be marked for submission to the MusicBrainz database. The user will be presented with a list of all tracks and their ISRCs, and can select which tracks to submit. Any ISRCs that cannot be submitted will be indicated as such, and hovering over them will show the reason why they cannot be submitted. The user can cancel the submission if they want to make changes before submitting.

The steps to follow to submit ISRCs are:

1. Match your files to a release in the right-hand pane.

2. Select :menuselection:`"File --> Submit ISRCs"` or click the "Submit ISRCs" button if you have it included in your action toolbar.

3. Picard will check the ISRCs and present a list of all tracks and their ISRCs.

4. Review the list, select the tracks you want to submit, and click "Submit" to submit the ISRCs to the MusicBrainz database.

.. only:: not latex

   .. image:: images/submit_isrcs_confirmation.png
      :align: center

   |

.. only:: latex

   .. image:: images/submit_isrcs_confirmation.png
      :align: center
      :width: 75%

.. note::

   The submission confirmation dialog will show a list of all tracks and their ISRCs for **every** release appearing in the Album pane. The list will show the status of the ISRCs for each track, and you can select which tracks you want to submit. New ISRCs that cannot be submitted because they are invalid or appear on more than one track will not be allowed to be submitted. You can cancel the submission if you want to make changes before submitting.

.. raw:: latex

   \clearpage

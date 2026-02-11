.. MusicBrainz Picard Documentation Project

.. _ref_tutorial_acoustid:

Understanding :index:`Acoustic Fingerprinting <pair: acoustic; fingerprint>` and :index:`AcoustIDs <AcoustID; usage>`
---------------------------------------------------------------------------------------------------------------------

.. From https://community.metabrainz.org/t/picard-fingerprinting-and-acoustids/190/2

The fingerprinting is the basis for the whole AcoustID song identification system. The audio fingerprint captures the characteristics of the recording, but there can be slight differences in the fingerprint of files of the same recording caused by such things as different encoding or bitrate. Fingerprints, along with the track metadata, are submitted to the AcoustID website where the AcoustID server combines fingerprints that are similar enough and assigns them a single AcoustID. This is actually what makes the AcoustID system really work for audio identification. The same recording can generate many slightly different fingerprints, but the AcoustID represents what the service identifies as the same recording for all of the associated fingerprints.

What Picard does is as follows:

1. When you click :menuselection:`"Scan"` on a file, Picard generates the audio fingerprint for the file, using the :program:`fpcalc` command line utility provided by AcoustID.

2. Picard uses this fingerprint to lookup an AcoustID from the AcoustID server. The AcoustID server will compare the fingerprint and will try to match it to an existing AcoustID. There are three possibilities:

   - It doesn't find an AcoustID. The lookup failed.
   - The AcoustID server finds an existing AcoustID for the submitted fingerprint, but it is not associated with any MusicBrainz recording. The lookup failed.
   - The AcoustID server finds an existing AcoustID for the submitted fingerprint and it is associated with a MusicBrainz recording. Picard matches the file to one of the MusicBrainz recordings linked to the AcoustID.

If there was no AcoustID found you can use the :menuselection:`"Submit"` button in Picard to submit the fingerprints to the AcoustID server once you have matched the files to the proper recordings. If there is no AcoustID already existing for a fingerprint, the server will generate a new AcoustID (which can take some time). It will also link the AcoustID to the MusicBrainz recording identified by the submitted metadata. Please see the :doc:`../usage/submit_acoustid` section for a detailed step-by-step procedure.

You don't need the AcoustID fingerprinting software to manually generate new AcoustIDs. The difference is, that the fingerprinting software is meant to be run on already tagged files, so if it cannot find an AcoustID it will immediately do the submission. For Picard the AcoustID is primarily an identification tool, and because the files are considered untagged at this *identification* stage, you can only do the submission once the files have been properly matched to a MusicBrainz recording. You will also find that after submission Picard will not automatically fetch the newly generated AcoustIDs. This is because the generation can take some time, and the response received from the AcoustID server does not contain newly generated AcoustIDs. However, if you do another scan on the files after submission, the AcoustID should be available.


.. From https://community.metabrainz.org/t/why-sometimes-acoustids-are-not-available-to-be-uploaded/511870/6

.. note::

   If files are matched using :menuselection:`"Scan"` and then :menuselection:`"Generate fingerprints"` is used on them, submission will not be enabled, because they have already been matched by fingerprint. This is the same situation as just using :menuselection:`"Scan"`, because after the files are scanned the resulting fingerprint / recording ID is remembered as already having been submitted.

   Also if you have files matched to tracks and use :menuselection:`"Generate fingerprints"` and are able to successfully submit the fingerprints, attempting to use :menuselection:`"Generate fingerprints"` for the same files and tracks again does not re-enable submission for those files. The reason is the same: Picard remembers the fingerprint / recording ID combinations already being submitted. However, restarting Picard (or even just removing and re-adding those files) and then using :menuselection:`"Generate fingerprints"` will enable submission again.

   Fingerprints are submitted in batches depending on fingerprint size, but often up to 200 or 250 fingerprints can be submitted in one batch. A submission request for a batch might fail due to various reasons such as networking or server issues. If a request fails, all of the fingerprints of this submission batch are still marked as not having been submitted and submission could be retried.

   You can also use :menuselection:`"Generate fingerprints"` on either unmatched or matched files. This will only generate the acoustic fingerprints without doing any lookup on the AcoustID server. This also means there will be no AcoustID tag created. However, you can submit these fingerprints if you match the fingerprinted files to a track.

.. raw:: latex

   \clearpage

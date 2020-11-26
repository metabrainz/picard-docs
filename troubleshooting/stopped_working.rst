.. MusicBrainz Picard Documentation Project

:index:`Picard just stopped working <troubleshooting; program freezes>`
========================================================================

There are typically two reasons that Picard will run very slowly or appear to be stalled:

**Processing a large number of files at one time**

    When processing a large number of files in one batch, Picard can run into issues either due to processing each file (e.g.:
    AcoustID fingerprinting) or during lookups following clustering or fingerprinting because of all of the information requests
    to the MusicBrainz server API, as well as downloading cover art.  Even though Picard may still be working its way through
    the backlog, the user interface may become non-responsive and appear that the program has stalled or frozen.

    The impact of processing files in large batches is exacerbated when using plugins that make additional information request
    calls to the MusicBrains server API.

    If you are processing a large library of files, it is generally more effective to process smaller batches (e.g.: 200 files)
    at a time, first retrieving the information using a cluster and lookup process, and then processing any remaining unmatched
    files using the scan process.  Please see the :doc:`../usage/retrieve` section for more information.

**Processing files across a network connection**

    If you are processing files across a network connection, this can impact the speed at which Picard works because of the speed
    difference between a network connection and a local drive.  In this case, the throughput can be improved by first copying the
    source files to a local drive, process with Picard, and then move the resulting files to the network drive.

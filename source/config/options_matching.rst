.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`Matching <configuration; matching preferences>`
=========================================================

.. image:: ../images/options-matching.png
   :width: 100 %

It is recommended for most users to leave these settings at their default values. For advanced users,
these allow you to tune the way Picard matches your files and clusters to MusicBrainz releases
and tracks.

**Minimal similarity for file lookups**

    The higher the percentage value, the more similar an individual file's metadata must be to the
    metadata from MusicBrainz for it to be matched to a release on the right-hand side.

**Minimal similarity for cluster lookups**

    The higher the percentage value, the more similar a cluster of files from the left-hand pane must
    be to a MusicBrainz release for the entire cluster to be matched to a release on the right-hand
    side.

**Minimal similarity for matching files to tracks**

    The higher the percentage value, the more similar an individual file's metadata must be to the
    metadata from MusicBrainz for it to be matched to a release on the right-hand side.

If you have absolutely no metadata in your current files, and you are using "Scan" to match tracks,
you may find that you need to lower the value of "Minimal similarity for matching files to tracks"
in order for Picard to match the files within a release. Otherwise you may find that Picard matches
the track to a release but then is not sure which track is correct; and leaves it in an "unmatched
files" group within that release.

As a general rule, lowering the percentages may increase the chance of finding a match at the risk of
false positives and incorrect matches.

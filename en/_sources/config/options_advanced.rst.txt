..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Advanced Options
================

**Ignore file paths matching the following regular expression**

    You can specify patterns for files and directories that Picard should never load.
    For example, if you set this to the regular expression ``\.bak$`` any file ending in ".bak"
    will be ignored when loading files.

**Ignore hidden files**

    If this option is enabled then hidden files and directories will not be loaded. This also
    includes any file or subdirectory inside a hidden directory.

**Include sub-folders when adding files from folders**

    If this option is enabled Picard will load all audio files in the selected directory and all
    its subdirectories. If disabled only audio files in the selected directory will be loaded.

**Ignore track duration difference under this number of seconds**

    This specifies the number of seconds that a file can differ in length from the length in the
    MusicBrainz database and still be considered to be the same.  The default value is 2 seconds.

**Ignore the following tracks when determining whether a release is complete**

    Missing tracks of the selected type (i.e.: video, pregap, data or silence) will be ignored when
    determining whether a release is considered to be complete. For example, if "video" is selected
    then a release with a bonus video will be marked as complete if it has all the audio tracks
    matched with a file even if the video file is missing.

**Tags to ignore for comparison**

    Tags in this list will not be considered when comparing the existing file metadata to the data
    retrieved from MusicBrainz. If the only difference between the file's metadata and the metadata
    retrieved from MusicBrainz is a tag listed in this ignore list then the file will be
    considered unmodified.

Network
-------

**Web Proxy**

    If you need a proxy to make an outside network connection you may specify one here.  The required
    settings are **Server Address**, **Port**, **Username** and **Password**.

.. |lookup_tagger| image:: ../images/mblookup-tagger.png

**Browser Integration**

    The browser integration allows you to load releases and recordings into Picard directly from the
    MusicBrainz website. Once you have opened musicbrainz.org in your browser from Picard, the website
    will show the green tagger button |lookup_tagger| next to releases and recordings.  Clicking on
    this button will load the corresponding release or recording into Picard.

**Default listening port**

    This identifies the default port Picard will listen on for the browser integration. If the port
    is not available Picard will try to increase the port number by one until it finds a free port.

**Listen only on localhost**

    By default Picard will limit access to the browser integration port to your local machine.
    Deactivating this option will expose the port on your network, allowing you to request Picard to
    load a specific release or recording via the network. For example, this would be used for the
    `Picard Barcode Scanner <https://play.google.com/store/apps/details?id=org.musicbrainz.picard.barcodescanner>`_
    Android app.

    **Warning**: *Only enable this option when you actually need it and only on networks you trust.
    Exposing application ports via the network can open potential security holes on your system.*


Matching
--------

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

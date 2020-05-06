..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Matching Files to Tracks
========================

Once you have retrieved the desired album information into the right-hand pane, the next step is to match the files from the
left-hand pane to the corresponding track in the right-hand pane.  A music symbol in front of a track number in the right-hand
pane indicates that there has been no file assigned to the track.  In some cases, Picard may have already tried to do the
matching for you.  If the matching wasn't done automatically, drag the appropriate files onto the appropriate album and track.

.. image:: ../images/lookup_4.png
   :width: 100%

Depending on your previous metadata, Picard will try to guess the matching tracks. The order is green > yellow > orange > red,
where green is the best match. If you are seeing a lot of red and orange, it could mean that Picard has guessed incorrectly, or that
your files didn't have a lot of previous metadata to work with.  If this is the case, it's recommended to select a track and
compare the "Original Values" and "New Values" in the metadata pane. If there is an incorrect match, simply drag the track to its
correct spot in the right-hand pane.

.. image:: ../images/matching_1.png
   :width: 100%

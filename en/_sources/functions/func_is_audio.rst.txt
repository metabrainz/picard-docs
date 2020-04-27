..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$is_audio
=========

| Usage: **$is_audio()**
| Category: conditional
| Implemented: Picard 2.2

**Description:**

Returns true, if the track being processed is not shown as being a video.


**Example:**

The following statements will return the values indicated::

    $is_audio()  ==>  "1"  (True, if the track is not a video)
    $is_audio()  ==>  ""   (False, if the track is a video)


.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

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


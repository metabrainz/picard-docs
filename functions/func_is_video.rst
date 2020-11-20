.. MusicBrainz Picard Documentation Project

$is_video
=========

| Usage: **$is_video()**
| Category: conditional
| Implemented: Picard 2.2

**Description:**

Returns true, if the track being processed is shown as being a video.


**Example:**

The following statements will return the values indicated::

    $is_video()  ==>  "1"  (True, if the track is a video)
    $is_video()  ==>  ""   (False, if the track is not a video)

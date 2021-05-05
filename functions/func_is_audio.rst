.. MusicBrainz Picard Documentation Project

.. _func_is_audio:

$is_audio
=========

| Usage: **$is_audio()**
| Category: conditional
| Implemented: Picard 2.2

**Description:**

Returns true, if the track being processed is not shown as being a video.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $is_audio()  ==>  "1"  (True, if the track is not a video)
    $is_audio()  ==>  ""   (False, if the track is a video)


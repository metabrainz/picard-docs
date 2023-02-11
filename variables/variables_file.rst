.. MusicBrainz Picard Documentation Project

:index:`File Variables <variables; file>`
==========================================

These variables are populated from information found in the audio files themselves, without any special Picard settings.

.. note::

   Variables that rely on information from the files (e.g.: _bitrate) are only available for use on
   tracks with attached files, when running scripts manually on files or in the file naming script.

.. warning::

   Prior to version 2.5 Picard did not support using file variables in tagging scripts.

**_bitrate**

    Approximate bitrate in kbps.

**_bits_per_sample**

    Bits of data per sample.

**_channels**

    Number of audio channels in the file.

**_dirname**

    The name of the directory containing the file at the point of being loaded into Picard. (*since Picard 1.1*)

**_extension**

    The file's extension. (*since Picard 0.9*)

**_filename**

    The name of the file without extension. (*since Picard 1.1*)

**_format**

    Media format of the file (e.g.: MPEG-1 Audio).

**_length**

    The length of the track in format mins:secs.

**_sample_rate**

    Number of digitizing samples per second (Hz).

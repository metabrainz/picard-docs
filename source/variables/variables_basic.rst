..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Basic Variables
===============

These variables are populated from MusicBrainz data for most releases, without any special Picard settings.

**_absolutetracknumber**

    The absolute number of this track disregarding the disc number (i.e.: ``%_absolutetracknumber%`` of ``%_totalalbumtracks%``). (since Picard 1.3)

**_albumartists**

    The Album's Artists' Name(s) (multi-value). (since Picard 1.3)

**_albumartists_sort**

    The Album Artist's Sort Name(s) (multi-value). (since Picard 1.3)

**_artists_sort**

    The Artist's Sort Name(s) (multi-value). (since Picard 1.3)

**_bitrate**

    Approximate bitrate in kbps.

**_bits_per_sample**

    Bits of data per sample.

**_channels**

    Number of audio channels in the file.

**_dirname**

    The name of the directory containing the file at the point of being loaded into Picard. (since Picard 1.1)

**_extension**

    The file's extension. (since Picard 0.9)

**_filename**

    The name of the file without extension (since Picard 1.1)

**_format**

    Media format of the file (e.g.: MPEG-1 Audio).

**_length**

    The length of the track in format mins:secs.

**_multiartist**

    0 if tracks on the album all have the same primary artist, 1 otherwise. (Since Picard 1.3)

.. _ref_primaryreleasetype:

**_primaryreleasetype**

    Release Group Primary type (i.e.: album, single, ep, broadcast, or other).

**_rating**

    Rating 0-5 by Musicbrainz users.

**_releasecomment**

    Release disambiguation comment. (since Picard 0.15)

**_releasegroup**

    Release Group Title which is typically the same as the Album Title, but can be different.

**_releasegroupcomment**

    Release Group disambiguation comment.

**_releaselanguage**

    Release Language as per `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_. (since Picard 0.10)

**_sample_rate**

    Number of digitizing samples per second (Hz).

.. _ref_secondaryreleasetype:

**_secondaryreleasetype**

    Zero or more Release Group Secondary types (i.e.: audiobook, compilation, dj-mix, interview, live, mixtape/street, remix, soundtrack, or spokenword).

**_totalalbumtracks**

    The total number of tracks across all discs of this release.

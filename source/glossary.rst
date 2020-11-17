.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`Glossary of Terms <glossary>`
=======================================

Many of the terms used in this documentation and within Picard itself have specific meaning
in the MusicBrainz environment.  Specific terms are defined as follows:

**acoustic fingerprint**

   An :index:`acoustic fingerprint` is a digital summary of an audio signal, that can be used to
   quickly identify the :index:`audio <fingerprint; acoustic>`.

   Please see `Wikipedia <https://wikipedia.org/wiki/Acoustic_fingerprint>`_ for a full
   explanation of acoustic fingerprinting.

**AcoustID**

   :index:`AcoustID` is an acoustic fingerprint system built entirely on open-source technology.  See
   the `AcoustID website <https://acoustid.org/>`_ for additional information.

**albumartist**

   The musician or group of musicians performing on a release.  For example, "The Beatles" is the
   :index:`albumartist` for the album "`Past Masters, Volume One
   <https://musicbrainz.org/release/9383a6f5-9607-4a36-9c68-8663aad3592b>`_", while the albumartist
   for "`No Boundaries: A Benefit for the Kosovar Refugees
   <https://musicbrainz.org/release/65536c6a-9219-4c41-9829-781eab7cdb50>`_" is "Various Artists".

   .. note::

      The albumartist usage is different for Classical Music releases, which follow the MusicBrainz
      `Classical Style Guide <https://musicbrainz.org/doc/Style/Classical>`_, listing the composer(s)
      first, followed by the performers.

**artist**

   The musician or group of musicians performing on a track.  For example, "Jeen" is the :index:`artist` on
   the track "`Be (One in a Million) <https://musicbrainz.org/track/5acda7a7-697c-4614-8467-7c48b3d946a6>`_"
   on the album "`Tourist <https://musicbrainz.org/release/472f4da8-c7dd-4e4a-8aae-9e7824f85afc>`_".

   Please see the `Artist <https://musicbrainz.org/doc/Artist>`_ page on the MusicBrainz website
   for additional information.

   .. note::

      The artist usage is different for Classical Music releases, which follow the MusicBrainz
      Classical Style Guide, showing only the composer and not the performers.

**artist credit**

   :index:`Artist credits <artist credit>` indicate who is the main credited artist (or artists) for releases, release
   groups, tracks and recordings, and how they are credited. They consist of artists, with
   (optionally) their names as credited in the specific release, track, etc., and join phrases
   between them.  For example, on the release "`Love Sponge
   <https://musicbrainz.org/release/6ca797fd-8f3a-4326-bdc7-f805cb2de088>`_" the artist is
   "`Walk off the Earth <https://musicbrainz.org/artist/e2a5eaeb-7de7-4ffe-a519-e18e427a5060>`_"
   but is credited as "Gianni and Sarah".

   Please see the `Artist Credits <https://musicbrainz.org/doc/Artist_Credits>`_ page on the MusicBrainz
   website for additional information.

**caa**

   :index:`The <see: CAA; cover art archive>` `Cover Art Archive <https://coverartarchive.org/>`_ which is a :index:`joint project <cover art archive>` between the
   `Internet Archive <https://archive.org/>`_ and `MusicBrainz <https://musicbrainz.org/>`_, whose
   goal is to make cover art images available to everyone on the Internet in an organized and
   convenient way.

   Please see the `Cover Art Archive page <https://musicbrainz.org/doc/Cover_Art_Archive>`_ on the
   MusicBrainz website for additional information.

**disc id**

   A :index:`Disc ID <disc id>` is the code number which MusicBrainz uses to link a physical CD to a release listing.
   It is a string of letters, like ``XzPS7vW.HPHsYemQh0HBUGr8vuU-``.  Disc IDs for a release can be
   seen on the disc IDs tab for the release on MusicBrainz. Clicking on these will give a detailed
   display of the disc ID, including the list of attached releases.

   A release may have any number of disc IDs, and a disc ID may be linked to multiple releases. This
   is because `disc ID calculation <https://musicbrainz.org/doc/Disc_ID_Calculation>`_ involves a
   hash of the frame offsets of the CD tracks.  Different pressing of a CD often have slightly
   different frame offsets, and hence different disc IDs.

   Conversely, two different CDs may happen to have exactly the same set of frame offsets and hence
   the same disc ID.  For example ``lwHl8fGzJyLXQR33ug60E8jhf4k-`` applies to a wide `variety of releases
   <https://musicbrainz.org/cdtoc/lwHl8fGzJyLXQR33ug60E8jhf4k->`_ by a variety of artists.

**mbid**

   :index:`The <see: mbid; MusicBrainz Identifier>` :index:`MusicBrainz Identifier`, which is a unique code used to identify each element in the MusicBrainz
   database.  These are 128-bit Universally Unique Identifiers (UUID) represented as 32 hexadecimal digits,
   displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters.

   Please see the `UUID page on Wikipedia <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_
   for more information.

**medium**

   :index:`One <medium>` of the physical, separate things you would get when you buy something in a record store. They are the
   individual CDs, vinyls, etc. contained within the packaging of an album (or any other type of release).
   Mediums are always included in a release, and have a position in said release (e.g. disc 1 or disc 2).
   They have a format like CD, 12" vinyl or cassette (in some cases this will be unknown), and can have
   an optional title (e.g. disc 2: The Early Years). For example, CD 1 of "`The Wall
   <https://musicbrainz.org/release/4bd2dbd5-a961-335a-a618-39c26b2ee791#disc1>`_".

   Please see the `Medium <https://musicbrainz.org/doc/Medium>`_ page on the MusicBrainz
   website for additional information.

**non-album track**

   :index:`This <see: non-album track; standalone recording>` term is obsolete and has been replaced with 'standalone recording'.

**recording**

   An entity in MusicBrainz which can be linked to tracks on releases. Each track must always be
   associated with a single recording, but a :index:`recording` can be linked to any number of tracks.
   For example, this recording of "`Bohemian Rhapsody
   <https://musicbrainz.org/recording/b1a9c0e9-d987-4042-ae91-78d6a3267d69>`_" is found as a track on over 100 releases.

   Please see the `Recording <https://musicbrainz.org/doc/Recording>`_ page on the MusicBrainz
   website for additional information.

**release**

   Represents the unique issuing of a product on a specific date with specific
   :index:`release` information such as the country, label, barcode and packaging. For example "`Sea of No Cares
   <https://musicbrainz.org/release/4e4ba41e-24ae-3f57-87f6-3d8f19ae9483>`_" is one version of the album released by Great Big Sea.

   Please see the `Release <https://musicbrainz.org/doc/Release>`_ page on the MusicBrainz
   website for additional information.

**release group**

   Groups several different releases into a single logical entity. Every release
   belongs to one, and only one :index:`release group`. Both release groups and releases are "albums" in a
   general sense, but with an important difference: a release is something you can buy as media such
   as a CD or a vinyl record, while a release group embraces the overall concept of an album — it
   doesn't matter how many CDs or editions / versions it had.  For example the `"Sea of No Cares"
   <https://musicbrainz.org/release-group/7e7ffd2b-3d1b-3487-aaaf-e4e6037f09ca>`_ release group
   contains multiple releases.

   Please see the `Release Group <https://musicbrainz.org/doc/Release_Group>`_ page on the MusicBrainz
   website for additional information.

**standalone recording**

   :index:`A <recording; standalone>` :index:`recording <standalone recording>` that is not linked to any release. An example is "`Sea of No Cares (live)
   <https://musicbrainz.org/recording/0198c132-ed38-430c-92bd-d3c7e9ff25b8>`_" by Great Big Sea.

   Please see the `Standalone Recording <https://musicbrainz.org/doc/Standalone_Recording>`_ page on
   the MusicBrainz website for additional information.

**track**

   A :index:`track` is the way a recording is represented on a particular release (or, more precisely, on a
   particular medium). Every track has a title and is credited to one or more artists.  For example,
   track 7 of the album "`Back to Boston <https://musicbrainz.org/release/9780e88d-a9e2-4e99-87c4-e54b65e7e49b>`_"
   by Jason Anderson is "`Driving Home <https://musicbrainz.org/track/bf8ecb3c-6fe6-41b7-a078-5748265a9f94>`_".

   Please see the `Track <https://musicbrainz.org/doc/Track>`_ page on
   the MusicBrainz website for additional information.

**work**

   :index:`A <work>` distinct intellectual or artistic creation, which can be expressed in the form of
   one or more audio recordings. While a 'Work' in MusicBrainz is usually musical in nature, it is
   not necessarily so. A work could also be a novel, play, poem or essay, later recorded as
   an oratory or audiobook. For example, the song "`Blinded by the Light
   <https://musicbrainz.org/work/7a757d97-da2a-3751-8d32-94d471de2eeb>`_" written by Bruce Springsteen
   has been recorded well over 100 times.

   Please see the `Work <https://musicbrainz.org/doc/Work>`_ page on the MusicBrainz website for
   additional information.

.. seealso::

   For more information on these and other terms used, please refer to the
   `Terminology <https://musicbrainz.org/doc/Terminology>`_ page on the MusicBrainz website.

.. seealso::

   For a detailed explanation of how all the elements are related within the MusicBrainz environment, please refer
   to the `MusicBrainz Database / Schema <https://musicbrainz.org/doc/MusicBrainz_Database/Schema>`_ webpage.

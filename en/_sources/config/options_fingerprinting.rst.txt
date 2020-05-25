..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Fingerprinting Options
======================

.. index::
   single: configuration; fingerprinting

.. image:: ../images/options-fingerprinting.png
   :width: 100 %

If you select a file or cluster in the left-hand side of the Picard screen and select :menuselection:`"Tools
--> Scan"`, Picard will invoke a program to scan the files and produce a fingerprint for each that can then
be used to look up the file on MusicBrainz.

MusicBrainz currently supports only `AcoustID <https://musicbrainz.org/doc/AcoustID>`_ (an Open Source
`acoustic fingerprinting <https://musicbrainz.org/doc/Fingerprinting>`_ system created by `Lukáš Lalinský
<https://oxygene.sk/>`_) but has previously supported TRM and MusicID PUID.

**Audio Fingerprinting**

   This allows you to select whether or not to enable acoustic fingerprinting within Picard.
   If acoustic fingerprinting is diabled then all remaining options in this tab will be locked and
   ignored.

**Ignore existing AcoustID fingerprints**

   When checked, any existing AcoustID fingerprint information will not be used, and the files will be
   rescanned.

**Fingerprint calculator**

   This identifies the external program on your system that will be used to calculate the AcoustID
   fingerprints.  By default, Picard uses the `Chromaprint <https://acoustid.org/chromaprint>`_ (fpcalc)
   utility which is included with the Picard installation.

**API key**

   The key used to access the AcoustID API to lookup and submit AcoustID fingerprints.  There is no
   cost to obtain an API key.

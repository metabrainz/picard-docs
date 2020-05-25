..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Download & Install
==================

.. index::
   single: install; download

The latest version of MusicBraiz Picard is always available for download from the `Picard
Website <https://picard.musicbrainz.org/downloads/>`_.  This includes installers for all
major operating systems (e.g.: Linux, macOS and Windows) as well as the `source code
<https://picard.musicbrainz.org/downloads/#source>`_. The latest source code is also
available at the `project repository <https://github.com/musicbrainz/picard>`_ on GitHub.


Installing Using Flatpak
------------------------

.. index::
   pair: install; flatpak

Picard is also available on Flathub. This version should work on all modern Linux distributions,
as long Flatpak is installed.

First enable the Flathub repository:

.. code-block:: bash

   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

You can now install Picard:

.. code-block:: bash

   flatpak install flathub org.musicbrainz.Picard

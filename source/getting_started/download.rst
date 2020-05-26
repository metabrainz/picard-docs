.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


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

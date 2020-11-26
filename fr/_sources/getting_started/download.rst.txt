.. MusicBrainz Picard Documentation Project

:index:`Download & Install Picard <install; download>`
=======================================================

MusicBrainz Picard is available for all major desktop operating systems (e.g. Windows, Linux and macOS),
and in multiple forms (directly downloadable formal release executables, package manager versions of these,
daily build executables, Python source code that you can execute with your own Python environment, etc.)

It is expected that most users will run formal release executables or package manager equivalents as these are
easy to install, and are stable versions which are less likely to have bugs in experimental or new functionality.

However, any users wishing to contribute to the development of Picard or its Plugins may want to run from source code,
downloading it from GitHub using a version of Git on their own computer. If you want to contribute to the Picard code
but you don't understand what the previous sentence said, then you have a bit of a learning curve. :-)

The latest version of MusicBrainz Picard is always available for download from the `Picard
Website <https://picard.musicbrainz.org/downloads/>`_.  This includes installers for all supported platforms as well as
`release source code <https://picard.musicbrainz.org/downloads/#source>`_. The very latest source code is also
available at the `GitHub repository <https://github.com/musicbrainz/picard>`_.


Linux: :index:`Installing with Flatpak <pair: install; flatpak>`
-----------------------------------------------------------------

Picard is also available on Flathub. This version should work on all modern Linux distributions,
as long Flatpak is installed.

First enable the Flathub repository:

.. code-block:: bash

   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

You can now install Picard:

.. code-block:: bash

   flatpak install flathub org.musicbrainz.Picard

.. raw:: latex

   \clearpage

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


Installing Picard on Linux
--------------------------

:index:`Installing with Flatpak <pair: install; flatpak>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Picard is available on `Flathub <https://flathub.org/apps/details/org.musicbrainz.Picard>`_.
This version should work on all modern Linux distributions, as long as Flatpak is installed
(see `Flatpak Quick Setup <https://flatpak.org/setup/>`_).

First enable the Flathub repository:

.. code-block:: bash

   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

You can now install Picard:

.. code-block:: bash

   flatpak install flathub org.musicbrainz.Picard


:index:`Installing with Snap <pair: install; snap>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Picard is available as a Snap from the Snap Store.  This version should work on all modern
Linux distributions, as long as Snap is installed (see `Installing Snap <https://snapcraft.io/docs/installing-snapd>`_).

The `Snap Store page of Picard <https://snapcraft.io/picard>`_ gives detailed instructions on how to install Picard on
various Linux distributions.  If your Linux distributions supports it you can install Picard from your distribution's
software center, e.g. Ubuntu Software or KDE Discover.  You can also install Picard from the terminal:


.. code-block:: bash

   snap install picard

.. note::

   Picard installed as a Snap is running inside a sandbox and thus it does not have full access to all files and
   folders on your system.  By default Picard has access to your home folder.  You can additionally give it access to
   removable media by running the following command on a terminal:

   .. code-block:: bash

      snap connect picard:removable-media


:index:`Installing from your distribution's package repository <pair: install; Linux package>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Picard is available in the package repositories of most distributions.  The `download page
<https://picard.musicbrainz.org/downloads/#linux>`_ provides links to the packages for common Linux
distributions.  Please refer to your distribution's documentation for how to install software packages.

Please note that most distributions usually ship older versions of Picard.  If you want to use
the latest available version, as is recommended, install Picard as Flatpak or Snap as described above.

.. raw:: latex

   \clearpage

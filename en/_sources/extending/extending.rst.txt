..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Extending Picard
================

There are two primary ways that the functionality of MusicBrainz Picard can be extended:
:doc:`plugins <plugins>` and :doc:`scripts <scripts>`.

Plugins can be installed / uninstalled and enabled / disabled from the Options menu.
Installed plugins are loaded during the startup of Picard, and are made available to the
program.

Scripts are stored within the user settings, and are managed from the :menuselection:`"Options --> Options..."` menu.

.. only:: html

   .. seealso::

      Details:
      :doc:`plugins` /
      :doc:`scripts` /
      :doc:`processing`

.. toctree::
   :hidden:

   plugins
   scripts
   processing

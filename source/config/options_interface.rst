..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


User Interface Options
======================

.. index::
   pair: configuration; user interface

.. image:: ../images/options-interface.png
   :width: 100 %

**Show text labels under icon**

    If this option is disabled, the text labels under the icons in the toolbar will not be displayed,
    causing the toolbar to appear a little smaller.

**Allow selection of multiple directories**

    Enabling this option will bypass the native directory selector and use QT's file dialog.  This
    may be desirable since the native directory selector generally doesn't allow you to select more
    than one directory. This applies to the :menuselection:`"File --> Add folder"` dialog. The file
    browser always allows multiple directory selection.

**Use advanced query syntax**

    This will enable advanced query syntax parsing on your searches. This only applies to the search
    box at the top right of Picard, not the lookup buttons.

**Show a quit confirmation dialog for unsaved changes**

    When this is enabled, Picard will show a dialog when you try to quit the program with unsaved
    files loaded. This may help prevent accidentally losing tag changes you've made, but not yet saved.

**Begin browsing in the following directory**

    By default, Picard remembers the last directory used to load files. If you enable this option
    and provide a directory, Picard will always start in the directory provided.

**User interface language**

    By default, Picard will display in the language displayed by your operating system, however you can
    override this and select a different language if needed.

**Customize action toolbar**

    This allows you to to add, remove or rearrange the items displayed in the Action Toolbar.

.. only:: html

   .. seealso::

      Details:
      :doc:`options_interface_colors` /
      :doc:`options_interface_top_tags`

.. toctree::
   :hidden:

   options_interface_colors
   options_interface_top_tags

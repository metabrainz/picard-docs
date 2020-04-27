..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


User Interface Options
======================

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

Colors
------

This section allows you to customize the various colors used in the Picard user interface.  To change a
color, simply click on the color block currently displayed for the desired text condition to bring up a
selection dialog, then pick your desired color.  The colors can be changed for the following text
conditions:

* **Errored entity**: files and other elements with errors on loading or saving

* **Pending entity**: files and other elements queued up for processing

* **Saved entity**: successfully saved files

* **Log view text (debug)**: debug messages in the Error/Debug Log

* **Log view text (error)**: error messages in the Error/Debug Log

* **Log view text (info)**: informational messages in the Error/Debug Log

* **Log view text (warning)**: warning messages in the Error/Debug Log

* **Tag added**: newly added tags in the metadata pane

* **Tag changed**: changed tags in the metadata pane

* **Tag removed**: removed tags in the metadata pane

Top Tags
--------

The tags specified in this option setting will always be shown in the specified order at the top of the
metadata pane (which shows the metadata of selected files or tracks).
This allows you to have the most important tags always on top of the list. Tags not listed here will be shown
in alphabetical order below the top tags.

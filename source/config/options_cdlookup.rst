..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


CD Lookup Options
=================

This section allows you to select which CD ROM device to use by default for looking up a CD.

**Windows**

   On Windows, Picard has a pulldown menu listing the various CD drives it has found. Pull down the
   menu and select the drive you want to use by default.

**macOS**

   In macOS, this option is currently a text field. The device is usually ``/dev/rdisk1``.

   If that doesn't work, one way is to simply keep increasing the number (e.g. ``/dev/rdisk2``) until
   it does work. A less trial and error method is to open "Terminal" and type ``mount``. The output
   should include a line such as::

      /dev/disk2 on /Volumes/Audio CD (local, nodev, nosuid, read-only)

   You need to replace ``/dev/disk`` with ``/dev/rdisk``, so if, for example, it says ``/dev/disk2``,
   you should enter ``/dev/rdisk2`` in Picard's preferences.

**Linux**

   In Linux, Picard has a pulldown menu like in Windows. If you're using an older version of Picard
   with a text field, you should enter the device name (typically ``/dev/cdrom``).

**Other platforms**

   On other platforms, the CD Lookup option is a text field and you should enter the path to the CD
   drive here.

On Windows and Linux systems, you can override this setting by clicking on :menuselection:`"Tools -->
Lookup CD..."` and selecting the desired device from the list of available devices.

.. MusicBrainz Picard Documentation Project

:index:`How do I change the fonts size or font? <change font size>`
===================================================================

General
-------

Picard is a Qt application, so whatever works for other Qt application will work for Picard.

Linux specific
--------------

Two ways to change the size/scaling are:

1. **Desktop Settings**

   |  The usual default way to change the scaling is to rely on the settings of the desktop environment, e.g. on GNOME the scaling set when configuring the screens. This usually works, and should be the first approach to take.

2. **Environment Settings**

   |  Setting the environment variable ``QT_SCALE_FACTOR`` will scale fonts for Qt applications. This can be useful on 4k monitors. From a terminal, you can then run ``QT_SCALE_FACTOR=2.0 picard`` to start Picard, or create an alias in your shell, or set the variable in your shell to affect all Qt applications.

To change both the size/scaling and the font, use `qt6ct <https://github.com/trialuser02/qt6ct>`_ to set the new font and/or size. Note that these changes will apply to all Qt applications, not just Picard.

`The official documentation on high DPI <https://doc.qt.io/qt-6/highdpi.html>`_ could be a useful read as well.

.. MusicBrainz Picard Documentation Project

:index:`How do I change the fonts?`
===================================

Picard is a QT app, so whatever works for other QT apps will work for Picard. Things you
can look at are:
* The usual default way to change the scaling is to rely on the settings of the desktop
  environment, e.g. on GNOME the scaling set when configuring the screens. This usually
  works, and should be the first approach to take.
* ``qt6ct`` (``qy5ct`` for versions less than 3) will allow you to set the fonts for all QT apps.
* ``QT_SCALE_FACTOR`` will scale fonts. This is useful on 4k monitors. You can then run
  ``QT_SCALE_FACTOR=2.0 picard`` or create an alias in your shell.

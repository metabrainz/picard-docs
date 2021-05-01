.. MusicBrainz Picard Documentation Project

macOS
=====

In macOS, the CD Lookup option is currently a text field. The device is usually ``/dev/rdisk1``.

If that doesn't work, one way is to simply keep increasing the number (e.g. ``/dev/rdisk2``) until
it does work. A less trial and error method is to open "Terminal" and type ``mount``. The output
should include a line such as::

   /dev/disk2 on /Volumes/Audio CD (local, nodev, nosuid, read-only)

You need to replace ``/dev/disk`` with ``/dev/rdisk``, so if, for example, it says ``/dev/disk2``,
you should enter ``/dev/rdisk2`` in Picard's preferences.

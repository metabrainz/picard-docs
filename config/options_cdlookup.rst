.. MusicBrainz Picard Documentation Project

:index:`CD Lookup Options <configuration; cd lookup>`
=====================================================

This section allows you to select which CD ROM device to use by default for looking up a CD.

.. only:: not latex

   .. image:: images/options-cdlookup-linux.png
      :align: center

.. only:: latex

   .. image:: images/options-cdlookup-linux.png
      :width: 75%
      :align: center

When the "Read ISRCs from CD" option is enabled, ISRCs will be read from the CD during the disc lookup. The ISRCs will be added to the file metadata when the CD is read, and will be used when looking up releases on MusicBrainz.

.. warning::

   Not all CD drives support reading ISRCs, and some may significantly slow down the disc reads.

   Not all CDs have ISRCs, and some readers may not be able to read them even if they are present on the CD. It is also possible that the ISRCs on the CD are not correct or have been read incorrectly, so you should always check the ISRCs before submitting them to the MusicBrainz database.

Platform-specific details
--------------------------

**Windows:**

   Picard has a pulldown menu listing the various CD drives it has found. Pull down the menu and select the drive you want to use by default. You can override this setting by clicking on :menuselection:`"Tools --> Lookup CD..."` and selecting the desired device from the list of available devices.

**Linux:**

   Picard has a pulldown menu like in Windows for the CD Lookup option. If you're using an older version of Picard with a text field, you should enter the device name (typically ``/dev/cdrom``). You can override this setting by clicking on :menuselection:`"Tools --> Lookup CD..."` and selecting the desired device from the list of available devices.

**macOS:**

   In macOS, the CD Lookup option is currently a text field. The device is usually ``/dev/rdisk1``. If that doesn't work, one way is to simply keep increasing the number (e.g. ``/dev/rdisk2``) until it does work. A less trial and error method is to open "Terminal" and type ``mount``. The output should include a line such as:

   .. code-block:: shell

      /dev/disk2 on /Volumes/Audio CD (local, nodev, nosuid, read-only)

   You need to replace ``/dev/disk`` with ``/dev/rdisk``. For example, if it says ``/dev/disk2`` you should enter ``/dev/rdisk2`` in Picard's preferences.

**Other platforms:**

   On other platforms, the CD Lookup option is a text field and you should enter the path to the CD drive here.

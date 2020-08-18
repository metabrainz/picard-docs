.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


How do I tell Picard which browser to use?
============================================================

.. index::
   pair: configuration; browser

On Windows, macOS, GNOME and KDE, Picard uses the default browser that has been configured for the system. On other systems, you can
use the ``BROWSER`` environment variable.

For example::

   export BROWSER="firefox '%s' &"

Another approach that works in some GNU/Linux systems is the following command::

   sudo update-alternatives --config x-www-browser

This should present you with a list of existing browsers in your system, allowing you to select the one to use by default.

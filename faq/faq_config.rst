.. MusicBrainz Picard Documentation Project

:index:`Configuration <configuration; config file location>`
============================================================

Where is the Picard :index:`configuration <configuration; file>` saved?
-----------------------------------------------------------------------

Picard saves the configuration in the file :file:`Picard.ini`. Its location depends on the operating system:

**Windows:**

   :file:`%APPDATA%\\MusicBrainz\\Picard.ini`

   This usually will be :file:`C:\\Users\\\\{YourUserName}\\AppData\\Roaming\\MusicBrainz`, where ``YourUserName`` should be replaced with your actual Windows user name.

**macOS, Linux and other Unix like systems:**

   :file:`$HOME/.config/MusicBrainz/Picard.ini`


I tagged a file in Picard, but :index:`iTunes <itunes; tags, tagging; itunes>` is not seeing the tags!
------------------------------------------------------------------------------------------------------

First, you need to force :index:`iTunes <itunes>` to re-read the information from your tags and update its library. This is discussed in the `iTunes Guide <https://musicbrainz.org/doc/iTunes_Guide>`_.

Additionally, iTunes has a known bug in its ID3v2.4 implementation, which makes it unable to read such tags if they also contain embedded cover art. As a work-around, you can configure Picard to write ID3v2.3 tags.


My tags are :index:`truncated <tags; truncated, WMP; tags>` to 30 characters in Windows Media Player!
-----------------------------------------------------------------------------------------------------

Picard's default settings write ID3v2.4 and ID3v1 tags to files. Older WMP versions can't read ID3v2.4, so it falls back to ID3v1 which has a limitation of 30 characters per title. To resolve this issue, configure Picard to write ID3v2.3 tags instead.

Since Windows 10 Creators Update (version 1703) ID3v2.4 is supported and the above issue should no longer apply.


How do I tell Picard which :index:`browser <pair: configuration; browser>` to use?
----------------------------------------------------------------------------------

On Windows, macOS, GNOME and KDE, Picard uses the default browser that has been configured for the system. On other systems, you can use the ``BROWSER`` environment variable.

For example::

   export BROWSER="firefox '%s' &"

Another approach that works in some GNU/Linux systems is the following command::

   sudo update-alternatives --config x-www-browser

This should present you with a list of existing browsers in your system, allowing you to select the one to use by default.

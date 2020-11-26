.. MusicBrainz Picard Documentation Project

:index:`macOS shows the app is damaged <troubleshooting; macOS shows app is damaged>`
======================================================================================

On macOS 10.12 and 10.13 there have been reports that sometimes the MusicBrainz Picard app
cannot be started and macOS shows an error message:

   "MusicBrainz Picard.app" is damaged and can't be opened. You should move it to the Trash.

This mostly seems to happen after moving the file to the Applications folder and seems to be
caused by Gatekeeper mistakenly marking the app as damaged.  To solve the issue open a terminal
and run::

   xattr -c "/Applications/MusicBrainz Picard.app"

This will clear the app being marked as damaged.  If you have placed the app in a different
location then :file:`/Applications` adjust the path in the command above accordingly.

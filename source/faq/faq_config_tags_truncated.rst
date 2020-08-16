.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


My tags are truncated to 30 characters in Windows Media Player!
==================================================================================

Prior to version 0.14, Picard's default settings were to write ID3v2.4 and ID3v1 tags to files. WMP can't read ID3v2.4, so it falls
back to ID3v1 which has a limitation of 30 characters per title. To solve this on versions prior to 0.14, configure Picard to write
ID3v2.3 tags instead.

Starting with version 0.14, the default settings have been changed to ID3v2.3 and this should no longer be an issue.

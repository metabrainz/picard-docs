.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


:index:`How to I edit several tags at once? Why is it not easier do so? <tags; editing>`
=============================================================================================

Please understand that Picard is not designed as a general purpose tag editor. Its primary goal is to retrieve community-maintained MusicBrainz
data to write into your tags. Some secondary goals include:

* allowing rule-based customization of that data using scripts and plugins
* encouraging users to create an account and fix and update data via the MusicBrainz website, thus sharing their work with the rest of the community rather than simply fixing their tags locally.

To that end, Picard is likely to never have as much development focus on manual bulk editing of tags as other general purpose editors (e.g.:
`Mp3tag <https://www.mp3tag.de/en/>`_, `foobar2000 <https://www.foobar2000.org/>`_, or even many library managers such as iTunes, Windows
Media Player, and MediaMonkey). That doesn't mean that the team won't welcome patches in this area!

Having said all this, it is still possible to edit several tags at once in Picard by following the steps:

1. Click and select several files with CTRL or SHIFT
2. Right click on one of them, then click Details...
3. On the popup dialog you can see the tags, with entries that denote where tags are different across files. You can edit or add new tags here.
4. On exiting the dialog, you have changed the tags in memory. You need to click Save in order to persist these changes to your files.

This process should work in both panes.

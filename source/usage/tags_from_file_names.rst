.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

Generating tags from file names
===============================

Sometimes files have no or bad tags, but the file names are well structured and follow a pattern.
In this case you can use :menuselection:`"Tools --> Tags From &File Names..."` to generate the tags
from the file names.


Basic usage
-----------

To use this tool, select one or more files loaded into Picard and open the Tags From File Names
dialog from the menu at :menuselection:`"Tools --> Tags From &File Names..."`.  The dialog will
show you a list of filenames and an input field at the top where you can enter a matching pattern.

The matching pattern can consist of Picard tag names enclosed in ``%`` signs and other characters
that are matched verbatim.  For the tag names you can use predefined names such as ``%artist%``,
``%album%``, or ``%title%`` (see :doc:`../variables/variables`) or use custom names.  There are a
couple of predefined patterns available to select from, but you can also adjust them or set your own.

If your files for example consist of a track number and track title separated by a space
(e.g. :file:`04 Heart of Gold.mp3`) you can use the matching pattern :samp:`%tracknumber% %title%`.
Should the track number and title be separated by e.g. a colon like :file:`04 - Heart of Gold.mp3`
the pattern needs to also include this separator, e.g. :samp:`%tracknumber% - %title%`.

.. image:: ../images/tags_from_file_names_1.png
   :width: 100 %

Clicking on the "Preview" button next to the matching pattern will show a preview of the extracted
tags for each file name.  Once you are satisfied with the result accept the changes with the
"Ok" button.  The changed tags will be set for the files.  Note that the changes will not be
saved automatically, you still need to save the files if you want the tags to be written
(see :doc:`../usage/save`).


Matching folders
----------------

The pattern can also match the parent folders of the file. To match for folders use a slash (``/``)
as separator.  If for example the file is in a folder named after the album, which in turn is
inside a folder named after the artist (i.e. :file:`Neil Young/Harvest/04 Heart of Gold.mp3`) you
could match the artist, album, track number and title with a patter of
:samp:`%artist%/%album%/%tracknumber% - %title%`.

.. image:: ../images/tags_from_file_names_2.png
   :width: 100 %


Replace underscores with spaces
-------------------------------

Sometimes files have been named without spaces and use underscores instead.  For example a file
could be named :file:`04_Heart_of_Gold.mp3`.  By default the title would get extracted as
"Heart_of_Gold".  In this case enable the checkbox "Replace underscores with spaces" and use a
pattern like :samp:`%tracknumber%_%title%` to extract the title properly as "Heart of Gold".

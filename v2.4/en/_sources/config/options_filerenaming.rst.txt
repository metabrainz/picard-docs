.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


File Naming Options
===================

.. index::
   pair: configuration; file naming

.. image:: ../images/options-filenaming.png
   :width: 100 %

These options determine how Picard handles files when they are saved with updated metadata.

**Move files when saving**

   If selected, this option tells Picard to move your audio files to a new directory when it saves
   them. One use for this is to keep your work organized: all untagged files are under "Directory A",
   and when Picard tags them it moves them to "Directory B". When "Directory A" is empty, your
   tagging work is done.

   If this option is left unchecked, then Picard will leave the files in the same directory when they
   are saved.

   Note that the "Rename Files" and "Move Files" options are independent of one another. "Rename Files"
   refers to Picard changing file names, typically based on artist and track names. "Move Files" refers
   to Picard moving files to new directories, based on a specified parent directory and subdirectories,
   typically based on album artist name and release title. However, they both use the same "file naming
   string". "Move files" uses the portion up until the last '/'. "Rename files" uses the portion after
   the last '/'.

**Destination directory**

   This specifies the destination parent diretory to which files are moved when they are saved, if the
   "Move files when saving" option is selected.  If you use the directory "." the files will be moved
   relative to their current location. If they are already in some sort of directory structure, this will
   probably not do what you want!

**Move additional files**

   Enter patterns that match any other files you want Picard to move when saving music files (e.g.:
   "Folder.jpg", "\*.png", "\*.cue", "\*.log"). Patterns are separated by spaces. When these additional
   files are moved they will end up in the release directory with your music files. In a pattern, the
   '\*' character matches zero or more characters. Other text, like ".jpg", matches those exact
   characters. Thus "\*.jpg" matches "cover.jpg", "liner.jpg", "a.jpg", and ".jpg", but not "nomatch.jpg2".

**Delete empty directories**

   When selected, Picard will remove directories that have become empty once a move is completed. Leave
   this unchecked if you want Picard to leave the source directory structure unchanged. Checking this box
   may be convenient if you are using the "move files" option to organize your work. An empty directory has
   no more work for you to do, and deleting the directory makes that clear.

**Rename files when saving**

   Select this option to let Picard change the file and directory names of your files when it saves
   them, in order to make the file and directory names consistent with the new metadata.

**Replace non-ASCII characters**

   Select this option to replace non-ASCII characters with their ASCII equivalent (e.g.: 'á', 'ä' and 'ǎ'
   with 'a'; 'é', 'ě' and 'ë' with 'e'; 'æ' with "ae"). More information regarding ASCII characters can be
   found on `Wikipedia <https://en.wikipedia.org/wiki/ASCII>`_.

**Windows compatibility**

   This option tells Picard to replace all Windows-incompatible characters with an underscore. This is
   enabled by default on Windows systems, with no option to disable.

.. index::
   single: scripts; file naming

**Name files like this**

   An edit box that contains a formatting string that tells Picard what the new name of the file and its
   containing directories should be in terms of various metadata values. The formatting string is in
   :doc:`Picard's scripting language <../scripting>` where dark blue text starting with a '$' is a
   :doc:`function name <../functions/list_by_type>` and names in light blue within '%' signs are Picard's
   :doc:`tag and variable names <../variables/variables>`, and is generally referred to as a "file naming
   script". Note that the use of a '/' in the formatting string separates the output directory from the file
   name. The formatting string is allowed to contain any number of '/' characters. Everything before the
   last '/' is the directory location, and everything after the last '/' becomes the file's name.

   There is only one file naming script defined in a user’s settings, although it can vary from a simple
   one-line script such as ``%album%/%title%`` to a very complex script using different file naming formats
   based on different criteria. In all cases, the files will be saved using the text output by the script.

   Scripts are often discussed in the `MetaBrainz Community Forum <https://community.metabrainz.org/>`_,
   and there is a thread specific to `file naming and script snippets
   <https://community.metabrainz.org/t/repository-for-neat-file-name-string-patterns-and-tagger-script-snippets/2786/>`_.

   .. note::

      Any new tags set or tags modified by the file naming script will not be written to the output files' metadata.

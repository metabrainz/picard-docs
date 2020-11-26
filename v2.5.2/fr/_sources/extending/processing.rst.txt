.. MusicBrainz Picard Documentation Project

:index:`Processing Order <processing order>`
=============================================

In order to make effective use of plugins and scripts, it is important to understand when
each is processed in relation to the others. As a general statement, plugins are always
processed before scripts. Plugins of the same type will be executed in order based upon
the priority specified when the plugin was registered.

Startup
-------

During program startup, plugins with the following hooks are processed, and any additional
functionality that they provide will be available immediately:

* File Formats
* Cover Art Providers
* Tagger Script Functions
* Context Menu Actions
* Option Pages

Loading a Release
-----------------

When data gets loaded from MusicBrainz (while the album shows the "loading" status in the
right-hand pane), the following are processed:

* Metadata Processor Plugins
* Tagging Scripts

Plugins have access to the raw data loaded from MusicBrainz and are processed before scripts,
in the order of priority set when the plugin was registered.

Scripts are processed in the order set in the Options menu.

.. note::

   Tagging scripts are always run against metadata loaded from MusicBrainz, and exactly after
   the data gets loaded and before files get matched. They are one of the last steps in the loading
   process. Tagging scripts do not have access to metadata stored in existing files.

Loading Music Files
-------------------

After a file has been loaded into Picard, plugins registered with ``file_post_load_processor()`` are
executed. This could, for example, be used to load additional data for a file.

Adding / Removing Files
-----------------------

After a file has been added to a track (on the right-hand pane of Picard), plugins registered with
``file_post_addition_to_track_processor()`` are executed.

After a file has been removed from a track (on the right-hand pane of Picard), plugins registered with
``file_post_removal_from_track_processor()`` are executed.

Saving Files
------------

When files are saved, for each file the File Naming Script is first executed to determine the
destination path and file name. Note that this script has no effect on the tag values written to the
output file.

After a file has been saved, plugins registered with ``file_post_save_processor()`` are executed. This
can, for example, be used to run additional post-processing on the file or write extra data. Note that
the file's metadata is already the newly saved metadata.

Removing Albums
---------------

After an album has been removed from Picard, plugins registered with ``album_post_removal_processor()``
are executed.

Context Menus
-------------

Individual tagging scripts can be executed on-demand from the context menu displayed when right-clicking
on a file, album, track, cluster or cluster list.

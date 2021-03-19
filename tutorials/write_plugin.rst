.. MusicBrainz Picard Documentation Project

Writing a :index:`Plugin <plugin; writing>`
==================================================================================

You have a great idea for extending Picard with a plugin but don't know where to start.  Unfortunately, this is a
common problem and prevents far too many of those great ideas from ever seeing the light of day.  Perhaps this tutorial
will help get you started in turning your great idea a reality.

Picard plugins are written in Python, so that's the language you'll be using.  Please check the `INSTALL.md
<https://github.com/metabrainz/picard/blob/master/INSTALL.md>`_ file on the Picard repository on GitHub to see the minimum
version requirements.  Also refer to the :doc:`Plugins API <../appendices/plugins_api>` for addition information, including
the parameters passed to each of the function types.

.. note::

   To ensure maximum compatibility, you should only use standard Python modules, or third-party modules that are already
   included in Picard.  If you use other modules, then the plugin will not function properly if used on a system that
   doesn't have the proper version of the module installed.

For the purpose of this tutorial, we're going to develop a simple plugin to save the argument information provided by Picard
to track and release processing plugins.  This will demonstrate how the information is accessed, and will provide a utility
that you might find useful when developing your own plugins.  This is based on the
`Data Dumper <https://github.com/rdswift/picard-plugins/tree/2.0_RDS_Plugins/plugins/data_dumper>`_ plugin by Bob Swift (rdswift).

The first thing that we'll need to include is the header information that describes the plugin.

.. code-block:: python

   PLUGIN_NAME = "Example plugin"
   PLUGIN_AUTHOR = "This authors name"
   PLUGIN_DESCRIPTION = "This plugin is an example"
   PLUGIN_VERSION = '0.1'
   PLUGIN_API_VERSIONS = ['2.2']
   PLUGIN_LICENSE = "GPL-2.0-or-later"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

Next we list the modules that will be referenced in our code.  In this case, we will be using the ``os`` module to build the
output file path, and the ``json`` module to format the text for readability. We will be saving our output file to the base
directory used for file naming so we import the ``config`` module from Picard, as well as the ``log`` module so that we can write
debug or error messages to Picard's log.  Finally, we import the appropriate processing hooks and plugin priority settings.

.. code-block:: python

   import json
   import os

   from picard import config, log
   from picard.metadata import (register_album_metadata_processor,
                              register_track_metadata_processor)
   from picard.plugin import PluginPriority

Now we can start on our code that we want to process.  First we'll identify the output file to store the parameter information
provided by Picard.  This is a file named ``data_dump.txt`` to be stored in the file naming output directory.

.. code-block:: python

   OFILE = "data_dump.txt"
   file_to_write = os.path.join(config.setting["move_files_to"], OFILE)

The next part is a function to write a Python object to our output file.  To allow the same function to be used for different
situations, we include parameters to identify the type of line (input), the object to write, and options for writing to JSON
format and appending or overwriting an existing output file.  We also include error checking to write to the Picard log in the
event of an exception.

.. code-block:: python

   def write_line(line_type, object_to_write, dump_json=False, append=True):
       file_mode = 'a' if append else 'w'
       try:
           with open(file_to_write, file_mode, encoding="UTF-8") as f:
               if dump_json:
                   f.write('{0} JSON dump follows:\n'.format(line_type,))
                   f.write('{0}\n\n'.format(json.dumps(object_to_write, indent=4)))
               else:
                   f.write("{0:s}: {1:s}\n".format(line_type, str(object_to_write),))
       except Exception as ex:
           log.error("{0}: Error: {1}".format(PLUGIN_NAME, ex,))

Now we include the functions to be called when releases and tracks are retrieved by Picard. The release function hook provides
three arguments, and the track function hook provides four arguments.  The argument types are described in the :doc:`Plugins API
<../appendices/plugins_api>` section.

.. code-block:: python

   def dump_release_info(album, metadata, release):
       write_line('Release Argument 1 (album)', album, append=False)
       write_line('Release Argument 3 (release)', release, dump_json=True)


   def dump_track_info(album, metadata, track, release):
       write_line('Track Argument 1 (album)', album)
       write_line('Track Argument 3 (track)', track, dump_json=True)
       # write_line('Track Argument 4 (release)', release, dump_json=True)

Finally, we need to register our functions so that they are processed with the appropriate events.  In our case, we set the priority
to ``HIGH`` so that we output the parameter information as it is received by Picard before any other plugins have an opportunity to
modify it.

.. code-block:: python

   # Register the plugin to run at a HIGH priority so that other plugins will
   # not have an opportunity to modify the contents of the metadata provided.
   register_album_metadata_processor(dump_release_info, priority=PluginPriority.HIGH)
   register_track_metadata_processor(dump_track_info, priority=PluginPriority.HIGH)

That's it for our plugin code. Now we need to package it so that we can install it into Picard.  If we're going to just use it locally
for ourself, the easiest way is to just name the file something like ``my_plugin.py``.  If there are multiple files, such as plugins that
include additional settings screens, then the files should be saved in a directory such as ``my_plugin`` with the main file named
``__init__.py``.  The directory is then archived into a ``my_plugin.zip`` file, with the file name the same as the included directory name.
The the contents of the archive would show as something like::

   my_plugin/__init__.py
   my_plugin/another_file.py
   my_plugin/etc

If you've made it this far, congratulations! You've just created your first Picard plugin. Now you have a starting point for turning that
great idea into reality.

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

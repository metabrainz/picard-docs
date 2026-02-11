.. MusicBrainz Picard Documentation Project

Writing a :index:`Plugin <plugin; writing>`
===========================================

You have a great idea for extending Picard with a plugin but don't know where to start. Unfortunately, this is a common problem and prevents far too many of those great ideas from ever seeing the light of day. Perhaps this tutorial will help get you started in turning your great idea a reality.

Picard plugins are written in Python, so that's the programming language you'll be using. Please check the `INSTALL.md <https://github.com/metabrainz/picard/blob/master/INSTALL.md>`_ file in the Picard repository on GitHub to see the minimum version requirements. This is Python 3.6 as of the time this tutorial was written. Also refer to the :doc:`Plugins API <../appendices/plugins_api>` for additional information, including the parameters passed to each of the function types.

For the purpose of this tutorial, we're going to develop a simple plugin to save the argument information provided by Picard to ``track`` and ``release`` processing plugins. This will demonstrate how the information is accessed, and will provide a utility that you might find useful when developing your own plugins.

The first thing that we'll need to include is the header information that describes the plugin.

.. code-block:: python

   PLUGIN_NAME = "Example plugin"
   PLUGIN_AUTHOR = "This authors name"
   PLUGIN_DESCRIPTION = "This plugin is an example"
   PLUGIN_VERSION = '0.1'
   PLUGIN_API_VERSIONS = ['2.2']
   PLUGIN_LICENSE = "GPL-2.0-or-later"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

Next we list the modules that will be referenced in our code. In this case, we will be using the ``os`` module to build the output file path, and the ``json`` module to format the argument dictionary text for readability. We will be saving our output file to the base directory used for file naming so we import the ``config`` module from Picard, as well as the ``log`` module so that we can write debug or error messages to Picard's log. Finally, we import the appropriate processing hooks and plugin priority settings.

.. code-block:: python

   import json
   import os

   from picard import config, log
   from picard.metadata import (register_album_metadata_processor,
                              register_track_metadata_processor)
   from picard.plugin import PluginPriority

.. warning::

   To ensure maximum compatibility, you should only use standard Python modules, or third-party modules that are already included in Picard. If you use other modules, then the plugin will not function properly if used on a system that doesn't have the proper version of the module installed or if someone is using an executable version of Picard.

Now we can start adding the code that we want Picard to execute. First we'll identify the output file to store the parameter information provided by Picard. This is a file named ``data_dump.txt`` to be stored in the file naming output directory. We find the name of the configuration setting we need, ``move_files_to``, by examining the Picard source code for the corresponding option setting screen. In this case it is a TextOption in the ``RenamingOptionsPage`` class found in the file `picard/ui/options/renaming.py <https://github.com/metabrainz/picard/blob/master/picard/ui/options/renaming.py>`_.

.. code-block:: python

   file_to_write = os.path.join(config.setting['move_files_to'], 'data_dump.txt')

The next part is a function to write a Python object to our output file. To allow the same function to be used for different situations, we include parameters to identify the type of line (input type), the object to write, and options for writing to JSON format and appending or overwriting an existing output file. In our case, we want to overwrite the file each time a new release is processed, but always append the track information to the file.

We also include error checking to write an entry to the Picard log in the event of an exception.

.. code-block:: python

   def write_line(line_type, object_to_write, dump_json=False, append=True):
       file_mode = 'a' if append else 'w'
       try:
           with open(file_to_write, file_mode, encoding='UTF-8') as f:
               if dump_json:
                   f.write(f"{line_type} JSON dump follows:\n")
                   f.write(f"{json.dumps(object_to_write, indent=4)}\n\n")
               else:
                   f.write(f"{line_type}: {str(object_to_write)}\n")
       except Exception as ex:
           log.error("%s: Error: %s", PLUGIN_NAME, ex,)

Now we include the functions to be called when releases and tracks are retrieved by Picard. The release function hook provides three arguments, and the track function hook provides four arguments. The argument types are described in the :doc:`Plugins API <../appendices/plugins_api>` section. The first argument, ``album``, is an object that holds information about the selected album. See the ``Album`` class in the `picard/album.py <https://github.com/metabrainz/picard/blob/master/picard/album.py>`_ file in Picard's source code for more information.

The second argument, ``metadata``, is an object that holds the tags and variables that Picard has assigned for the current release and track. This is where you can add or edit the tags and variables that Picard makes available to the user for scripts. See the ``Metadata`` class in the `picard/metadata.py <https://github.com/metabrainz/picard/blob/master/picard/metadata.py>`_ file in Picard's source code for more information.

The ``track`` and ``release`` arguments are Python dictionaries containing the information provided in response to Picard's calls to the MusicBrainz API. The information may differ, depending on the user's :doc:`../config/options_metadata` settings for things like "*Use release relationships*" or "*Use track relationships*".

.. code-block:: python

   def dump_release_info(album, metadata, release):
       write_line('Release Argument 1 (album)', album, append=False)
       write_line('Release Argument 3 (release)', release, dump_json=True)

   def dump_track_info(album, metadata, track, release):
       write_line('Track Argument 1 (album)', album)
       write_line('Track Argument 3 (track)', track, dump_json=True)
       # write_line('Track Argument 4 (release)', release, dump_json=True)

Finally, we need to register our functions so that they are processed with the appropriate events. In our case, we set the priority to ``HIGH`` so that we output the parameter information as it is received by Picard before any other plugins have an opportunity to modify it.

.. code-block:: python

   # Register the plugin to run at a HIGH priority so that other plugins will
   # not have an opportunity to modify the contents of the metadata provided.
   register_album_metadata_processor(dump_release_info, priority=PluginPriority.HIGH)
   register_track_metadata_processor(dump_track_info, priority=PluginPriority.HIGH)

The complete plugin code file looks something like:

.. code-block:: python

   PLUGIN_NAME = "Example plugin"
   PLUGIN_AUTHOR = "This authors name"
   PLUGIN_DESCRIPTION = "This plugin is an example"
   PLUGIN_VERSION = '0.1'
   PLUGIN_API_VERSIONS = ['2.2']
   PLUGIN_LICENSE = "GPL-2.0-or-later"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

   import json
   import os

   from picard import config, log
   from picard.metadata import (register_album_metadata_processor,
                              register_track_metadata_processor)
   from picard.plugin import PluginPriority

   file_to_write = os.path.join(config.setting['move_files_to'], 'data_dump.txt')

   def write_line(line_type, object_to_write, dump_json=False, append=True):
       file_mode = 'a' if append else 'w'
       try:
           with open(file_to_write, file_mode, encoding='UTF-8') as f:
               if dump_json:
                   f.write(f"{line_type} JSON dump follows:\n")
                   f.write(f"{json.dumps(object_to_write, indent=4)}\n\n")
               else:
                   f.write(f"{line_type}: {str(object_to_write)}\n")
       except Exception as ex:
           log.error("%s: Error: %s", PLUGIN_NAME, ex,)

   def dump_release_info(album, metadata, release):
       write_line('Release Argument 1 (album)', album, append=False)
       write_line('Release Argument 3 (release)', release, dump_json=True)

   def dump_track_info(album, metadata, track, release):
      write_line('Track Argument 1 (album)', album)
      write_line('Track Argument 3 (track)', track, dump_json=True)
      # write_line('Track Argument 4 (release)', release, dump_json=True)

   # Register the plugin to run at a HIGH priority so that other plugins will
   # not have an opportunity to modify the contents of the metadata provided.
   register_album_metadata_processor(dump_release_info, priority=PluginPriority.HIGH)
   register_track_metadata_processor(dump_track_info, priority=PluginPriority.HIGH)

That's it for our plugin code. Now we need to package it so that we can install it into Picard. If we're going to just use it locally for ourself, the easiest way is to just name the file something like :file:`my_plugin.py`. If there are multiple files, such as plugins that include additional settings screens, then the files should be saved in a directory such as :file:`my_plugin` with the main file named :file:`__init__.py`. The directory is then archived into a :file:`my_plugin.zip` file, with the file name the same as the included directory name. The contents of the archive would show as something like::

   my_plugin/__init__.py
   my_plugin/another_file.py
   my_plugin/etc

If you've made it this far, congratulations! You've just created your first Picard plugin. Now you have a starting point for turning that great idea into reality.

.. seealso::

   Relevant portions of Picard's source code including:

   * Option settings modules in `picard/ui/options/ <https://github.com/metabrainz/picard/tree/master/picard/ui/options>`_ for names used to access the settings.
   * ``Album`` class in the `picard/album.py <https://github.com/metabrainz/picard/blob/master/picard/album.py>`_ file.
   * ``Metadata`` class and metadata processing plugin registration functions in the `picard/metadata.py <https://github.com/metabrainz/picard/blob/master/picard/metadata.py>`_ file.
   * ``PluginPriority`` class in the `picard/plugin.py <https://github.com/metabrainz/picard/blob/master/picard/plugin.py>`_ file.

.. raw:: latex

   \clearpage

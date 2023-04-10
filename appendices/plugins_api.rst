.. MusicBrainz Picard Documentation Project

:index:`Appendix A <pair: plugins; programming>`: :index:`Plugins API <pair: plugins; api>`
============================================================================================

:index:`Plugin Metadata <plugins; metadata>`
---------------------------------------------

Each plugin must provide some metadata as variables. Those variables should be placed at the top of the file.

.. code-block:: python

   PLUGIN_NAME = "Example plugin"
   PLUGIN_AUTHOR = "This authors name"
   PLUGIN_DESCRIPTION = """
   This plugin is an example

   Since *Picard 2.7* the description can be formatted using
   [Markdown](https://daringfireball.net/projects/markdown/) syntax.
   If you use Markdown formatting make sure the minimum version in
   `PLUGIN_API_VERSIONS` is set to 2.7.
   """
   PLUGIN_VERSION = '0.1'
   PLUGIN_API_VERSIONS = ['2.7', '2.8']
   PLUGIN_LICENSE = "GPL-2.0-or-later"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"
   PLUGIN_USER_GUIDE_URL = "https://my.program.site.org/example_plugin_documentation.html"

Variables explanation:

* **PLUGIN_NAME** should be a short but descriptive name for the plugin.

* **PLUGIN_DESCRIPTION** should be as simple as possible, while still describing the main function.
  If your plugin targets Picard 2.7 or later you can use `Markdown <https://daringfireball.net/projects/markdown/>`_
  syntax to format the text.  If your plugin targets earlier versions you can instead use simple HTML formatting.
  Please restrict the usage of HTML to basic text formatting (e.g. ``<strong>``, ``<em>``), links (``<a>``) and
  lists (``<ul>``, ``<ol>``).

* **PLUGIN_VERSION** should be filled with the version of Plugin. Plugin versions should be in the format ``x.y.z``
  (e.g.: "1.0" or "2.12.4"). It is recommended that you use `Semantic Versioning <https://semver.org/>`_.

* **PLUGIN_API_VERSIONS** should be set to the versions of Picard this plugin to run with. New Picard versions
  will usually support older plugin API versions, but on breaking changes support for older plugin versions can
  be dropped. Versions available for Picard 2 are "2.0", "2.1" and "2.2".

* **PLUGIN_LICENSE** should be set with the license name of the plugin. If possible use one of the license names
  from the `SPDX License List <https://spdx.org/licenses/>`_, but you are welcomed to use another license if the
  one you chose is not available in the list.

* **PLUGIN_LICENSE_URL** should be set to a URL pointing to the full license text.

* **PLUGIN_USER_GUIDE_URL** should be set to a URL pointing to the documentation for the plugin.  This variable is
  optional and may be omitted.  If a URL is provided, it will be shown as a clickable link in the description
  displayed for the plugin in the Plugins option settings screen.


:index:`Metadata Processors <plugins; metadata processors>`
------------------------------------------------------------

MusicBrainz metadata can be post-processed at two levels, album and track. The types of the arguments passed to
the processor functions in the following examples are as follows:

* **album**: ``picard.album.Album``
* **metadata**: ``picard.metadata.Metadata``
* **release**: ``dict`` with release data from MusicBrainz JSON web service
* **track**: ``dict`` with track data from MusicBrainz JSON web service


Album metadata example:
+++++++++++++++++++++++

.. code-block:: python

   PLUGIN_NAME = "Disc Numbers"
   PLUGIN_AUTHOR = "Lukas Lalinsky"
   PLUGIN_DESCRIPTION = "Moves disc numbers from album titles to tags."

   from picard.metadata import register_album_metadata_processor
   import re

   def remove_discnumbers(tagger, metadata, release):
       matches = re.search(r"\(disc (\d+)\)", metadata["album"])
       if matches:
           metadata["discnumber"] = matches.group(1)
           metadata["album"] = re.sub(r"\(disc \d+\)", "", metadata["album"])

   register_album_metadata_processor(remove_discnumbers)


Track metadata example:
+++++++++++++++++++++++

.. code-block:: python

   PLUGIN_NAME = "Feat. Artists"
   PLUGIN_AUTHOR = "Lukas Lalinsky"
   PLUGIN_DESCRIPTION = "Removes feat. artists from track titles."

   from picard.metadata import register_track_metadata_processor
   import re

   def remove_featartists(tagger, metadata, track, release):
       metadata["title"] = re.sub(r"\(feat. [^)]*\)", "", metadata["title"])

   register_track_metadata_processor(remove_featartists)


:index:`Event Hooks <pair: plugins; event hooks>`
--------------------------------------------------

Plugins can register themselves to listen for different events. Currently the following event hooks are available:

file_post_load_processor(file)
++++++++++++++++++++++++++++++

This hook is called after a file has been loaded into Picard. This could for example be used to load additional
data for a file. Usage:

.. code-block:: python

   from picard.file import register_file_post_load_processor

   def file_post_load_processor(file):
     pass

   register_file_post_load_processor(file_post_load_processor)


file_post_save_processor(file)
++++++++++++++++++++++++++++++

This hook is called after a file has been saved. This can for example be used to run additional post-processing on
the file or write extra data. Note that the file's metadata is already the newly saved metadata. Usage:

.. code-block:: python

   from picard.file import register_file_post_save_processor

   def file_post_save_processor(file):
     pass

   register_file_post_save_processor(file_post_save_processor)


file_post_addition_to_track_processor(track, file)
++++++++++++++++++++++++++++++++++++++++++++++++++

This hook is called after a file has been added to a track (on the right-hand pane of Picard).

.. code-block:: python

   from picard.file import register_file_post_addition_to_track_processor

   def file_post_addition_to_track_processor(track, file):
     pass

   register_file_post_addition_to_track_processor(file_post_addition_to_track_processor)


file_post_removal_from_track_processor(track, file)
+++++++++++++++++++++++++++++++++++++++++++++++++++

This hook is called after a file has been removed from a track (on the right-hand pane of Picard).

.. code-block:: python

   from picard.file import register_file_post_removal_from_track_processor

   def file_post_removal_from_track_processor(track, file):
     pass

   register_file_post_removal_from_track_processor(file_post_removal_from_track_processor)


album_post_removal_processor(album)
+++++++++++++++++++++++++++++++++++

This hook is called after an album has been removed from Picard.

.. code-block:: python

   from picard.album import register_album_post_removal_processor

   def album_post_removal_processor(album):
     pass

   register_album_post_removal_processor(album_post_removal_processor)


.. note::

   Event hooks have been available since API version 2.2.


:index:`File Formats <pair: plugins; file format>`
---------------------------------------------------

Plugins can extend Picard with support for additional file formats. See the existing `file format implementations
<https://github.com/metabrainz/picard/tree/master/picard/formats>`_ for details on how to implement the ``_load``
and ``_save`` methods. Example:

.. code-block:: python

   PLUGIN_NAME = "..."
   PLUGIN_AUTHOR = "..."
   PLUGIN_DESCRIPTION = "..."
   PLUGIN_VERSION = '...'
   PLUGIN_API_VERSIONS = ['...']
   PLUGIN_LICENSE = "..."
   PLUGIN_LICENSE_URL = "..."

   from picard.file import File
   from picard.formats import register_format
   from picard.metadata import Metadata

   class MyFile(File):
       EXTENSIONS = [".foo"]
       NAME = "Foo Audio"

       def _load(self, filename):
           metadata = Metadata()
           # Implement loading and parsing the file here.
           # This method is supposed to return a Metadata instance filled
           # with all the metadata read from the file.
           metadata['~format'] = self.NAME
           return metadata

       def _save(self, filename, metadata):
           # Implement saving the metadata to the file here.
           pass

   register_format(MyFile)


:index:`Tagger Script Functions <pair: scripting functions; plugins>`
----------------------------------------------------------------------

To define new tagger script functions use ``register_script_function(function, name=None)`` from the ``picard.script`` module.
``parser`` is an instance of ``picard.script.ScriptParser``, and the rest of the arguments passed to it are the arguments from
the function call in the tagger script. Example:

.. code-block:: python

   PLUGIN_NAME = "Initials"
   PLUGIN_AUTHOR = "Lukas Lalinsky"
   PLUGIN_DESCRIPTION = "Provides tagger script function $initials(text)."
   PLUGIN_VERSION = '0.1'
   PLUGIN_API_VERSIONS = ['2.0']
   PLUGIN_LICENSE = "GPL-2.0"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.txt"

   from picard.script import register_script_function

   def initials(parser, text):
       return "".join(a[:1] for a in text.split(" ") if a[:1].isalpha())

   register_script_function(initials)


``register_script_function`` supports two optional arguments:

* **eval_args**: If this is **False**, the arguments will not be evaluated before being passed to **function**.
* **check_argcount**: If this is **False** the number of arguments passed to the function will not be verified.

The default value for both arguments is **True**.


:index:`Context Menu Actions <pair: plugins; context menu actions>`
--------------------------------------------------------------------

Right-click context menu actions can be added to albums, tracks and files in "Unmatched Files", "Clusters"
and the "ClusterList" (parent folder of Clusters). Example:

.. code-block:: python

   PLUGIN_NAME = u'Remove Perfect Albums'
   PLUGIN_AUTHOR = u'ichneumon, hrglgrmpf'
   PLUGIN_DESCRIPTION = u'''Remove all perfectly matched albums from the selection.'''
   PLUGIN_VERSION = '0.2'
   PLUGIN_API_VERSIONS = ['0.15.1']
   PLUGIN_LICENSE = "GPL-2.0"
   PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.txt"

   from picard.album import Album
   from picard.ui.itemviews import BaseAction, register_album_action

   class RemovePerfectAlbums(BaseAction):
       NAME = 'Remove perfect albums'

       def callback(self, objs):
           for album in objs:
               if isinstance(album, Album) and album.is_complete()\
                  and album.get_num_unmatched_files() == 0\
                  and album.get_num_matched_tracks() == len(list(album.iterfiles()))\
                  and album.get_num_unsaved_files() == 0 and album.loaded == True:
                   self.tagger.remove_album(album)

   register_album_action(RemovePerfectAlbums())

Use ``register_x_action`` where 'x' is "*album*", "*track*", "*file*", "*cluster*" or "*clusterlist*".

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

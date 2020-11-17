.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

:index:`Plugins <plugins>`
===========================

Plugins are written in Python, and are registered to the appropriate hooks.  Each plugin
has its own version identifier, but also lists the plugin API versions that it supports.
When loading a plugin, Picard first compares its list of API versions to the plugin’s
supported versions to ensure that the plugin will operate correctly.  The Picard API
versions indicate the version of the program in which the plugin API was last updated and
any plugin APIs with which it is backwards compatible.

Hooks are connections to the various objects in Picard that call a specific type of plugin.
During the normal running of Picard, when it encounters a hook it will first retrieve a
list of all plugins registered for that specific hook, and then execute them sequentially
in order based upon the priority specified when the plugin was registered to the hook.

There are a few different :index:`types of plugins <plugins; types>`, including:

**Metadata processors**: These plugins can access and modify the metadata when it is loaded
from MusicBrainz. They are registered with ``register_album_metadata_processor()`` or
``register_track_metadata_processor()``.  These are what you might call "automatic" because
they operate without any user intervention.  An example is the Classical Extras plugin.

**Cover art providers**: These plugins provide another cover art source, and are registered
with ``register_cover_art_provider()``. They are also "automatic" in that they load album art
without user intervention, although they must be enabled by the user in the Cover Art options.
The Fanart.tv plugin is an example.

**Scripting function**: Some plugins just provide additional scripting functions for use in
:menuselection:`"Options --> Scripting"` or the renaming script. These are registered with
``register_script_function()``.  Keep tag, which provides the ``$keep()`` function, is an example.

**Context menu actions**: Plugins can register actions that can be activated manually via the
context menu. This is what the Load as non-album track plugin does. Another example is Generate
Cuesheet.  These are registered with ``register_album_action()``, ``register_track_action()``,
``register_file_action()``, ``register_cluster_action()`` or ``register_clusterlist_action()``.

**File formats**: Plugins can also provide support for new file formats not yet supported by
Picard.  These are registered with ``register_format()``.

**Event processors**: Plugins can execute automatically based on certain event triggers.
These are registered with ``file_post_load_processor()``, ``file_post_save_processor()``,
``file_post_addition_to_track_processor()``, ``file_post_removal_from_track_processor()``
or ``album_post_removal_processor()``.

Note that plugins are not limited to one of those areas.  A single plugin could implement all
of the above, but most existing plugins focus on one.

The :doc:`Plugins API <../technical/plugins_api>` provides information regarding the different
plugin hooks available, along with some examples of their use.  There is also a list of the
`available plugins <https://picard.musicbrainz.org/plugins/>`_ that have been submitted to the
MusicBrainz Picard repository shown on the Picard website.

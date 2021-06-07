.. MusicBrainz Picard Documentation Project

Configuration
=============

Once Picard has been installed on your system, the next step is to configure it to your
preferences.  The configuration consists of enabling the desired screen sections for display,
selecting the desired actions, and setting the various options.

:index:`Screen Setup <configuration; screen setup>`
----------------------------------------------------

The screen setup is found under the :menuselection:`"View"` item on the menu bar.  To enable the display of an
item, simply check the box for the screen option.  The items are:

**File Browser**

   This displays a file browser on the left side of the screen for selecting
   files and directories for processing. Files can be loaded into Picard by dragging and dropping
   them to the right panes, double clicking on individual files or by selecting multiple files
   and folders and selecting "Load selected files" from the context menu.

   Files and directories can also be selected using your system's file browser by dragging and
   dropping them onto the Picard application.

**Cover Art**

   This displays the cover art for the currently selected item (track or release)
   in a window to the right of the tags section of the display.  This allows you to select or replace
   the cover art saved with the release.

**Actions**

   This displays the button bar of the actions performed by Picard, located just below the menu bar.

**Search**

   This displays the manual search box to the right of the "Actions" button bar.

**Player**

   This displays the built-in player for playing selected audio files.

.. _action_options:

:index:`Action Options <configuration; action options>`
--------------------------------------------------------

The action options are found under the :menuselection:`"Options"` item on the menu bar.  There are three available
actions that Picard can perform when saving selected music files:

**Rename Files**

   Picard will rename each file in accordance with the naming script.

**Move Files**

   Picard will move files to the target directory in accordance with the naming script.

**Save Tags**

   Picard will update the metadata tags in the files in accordance with the specified
   option settings and tagging scripts.


:index:`User Profiles <user profiles, profiles; user>`
---------------------------------------------------------------

As of version 2.7, Picard supports multiple user profiles that can quickly switch between option settings. The profile
management functions are found under the :menuselection:`"Options --> User Profiles..."` item on the menu bar.  Please
see the :doc:`Managing User Profiles <../usage/user_profiles>` section for a detailed explanation of the profile system.


:index:`Option Settings <see: option settings; configuration>`
---------------------------------------------------------------

The option settings are found under the :menuselection:`"Options --> Options..."` item on the menu bar.  This will open
a new window with the option groups listed in a tree format on the left hand side, and the individual
settings on the right hand side.  This is where the majority of Picard's customization is performed.

.. only:: html

   .. image:: images/options-general.png
      :width: 100 %

   .. seealso::

      :doc:`options_general` /
      :doc:`options_metadata` /
      :doc:`options_tags` /
      :doc:`options_cover` /
      :doc:`options_filerenaming` /
      :doc:`options_fingerprinting` /
      :doc:`options_cdlookup` /
      :doc:`options_plugins` /
      :doc:`options_interface` /
      :doc:`options_scripting` /
      :doc:`options_advanced`

.. toctree::
   :hidden:

   options_general.rst
   options_metadata.rst
   options_tags.rst
   options_cover.rst
   options_filerenaming.rst
   options_fingerprinting
   options_cdlookup.rst
   options_plugins.rst
   options_interface.rst
   options_scripting.rst
   options_advanced.rst

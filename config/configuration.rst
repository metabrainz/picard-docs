.. MusicBrainz Picard Documentation Project

Configuration
=============

Once Picard has been installed on your system, the next step is to configure it to your preferences. The configuration consists of enabling the desired screen sections for display, selecting the desired actions, and setting the various options.

:index:`Screen Setup <configuration; screen setup>`
----------------------------------------------------

The screen setup is found under the :menuselection:`"View"` item on the menu bar. To enable the display of an item, simply check the box for the screen option.  The items are:

**File Browser**

   This displays a file browser on the left side of the screen for selecting files and directories for processing. Files can be loaded into Picard by dragging and dropping them to the right panes, double clicking on individual files or by selecting multiple files and folders and selecting "Load selected files" from the context menu.

   Files and directories can also be selected using your system's file browser by dragging and dropping them onto the Picard application.

**Cover Art**

   This displays the cover art for the currently selected item (track or release) in a window to the right of the tags section of the display. This allows you to select or replace the cover art saved with the release.

**Actions**

   This displays the button bar of the actions performed by Picard, located just below the menu bar.

**Search**

   This displays the manual search box to the right of the "Actions" button bar.

**Player**

   This displays the built-in player for playing selected audio files.

.. _action_options:


:index:`Action Options <configuration; action options>`
--------------------------------------------------------

The action options are found under the :menuselection:`"Options"` item on the menu bar. There are three available actions that Picard can perform when saving selected music files:

**Rename Files**

   Picard will rename each file in accordance with the naming script.

**Move Files**

   Picard will move files to the target directory in accordance with the naming script.

**Save Tags**

   Picard will update the metadata tags in the files in accordance with the specified option settings and tagging scripts.


:index:`Option Settings <see: option settings; configuration>`
---------------------------------------------------------------

The option settings are found under the :menuselection:`"Options --> Options..."` item on the menu bar. On macOS they can be accessed with :menuselection:`"MusicBrainz Picard --> Preferences..."`. This will open a new window with the option groups listed in a tree format on the left hand side, and the individual settings on the right hand side. This is where the majority of Picard's customization is performed.

.. note::
   When running your code from the source in a macOS environment, you can access the option settings by navigating to the :menuselection:`"Python --> Preferences..."` option in the menu bar. This allows you to configure and customize various settings for your development environment.

.. only:: html

   .. image:: images/options-general-with-tree.png
      :width: 100 %


:index:`Option Profiles <see: profiles; configuration>`
--------------------------------------------------------

The option settings can also be manipulated with option profiles. A detailed explanation can be found in the :doc:`/usage/option_profiles` section, but they basically function as follows:

With option profiles, you can save a number of settings to a profile, which you can enable or disable to quickly change the settings for a particular usage scenario. For example, if you want to process your classical music differently to other music.

Options that are controlled by an enabled profile will be shown as highlighted. Hovering your cursor over the highlighted option will identify which profile currently controls the setting. Settings are always displayed based on the first enabled profile in the profile stack, which corresponds to the setting that will be used during processing.

Changes made to a profile's options settings, enabled status, or position in the profile stack will be reflected in the option settings displayed on the other configuration pages.

.. only:: latex

   .. toctree::

      /config/options_general
      /config/options_profiles
      /config/options_metadata
      /config/options_tags
      /config/options_cover
      /config/options_filerenaming
      /config/options_fingerprinting
      /config/options_cdlookup
      /config/options_plugins
      /config/options_interface
      /config/options_scripting
      /config/options_advanced


.. only:: html and not epub

   .. seealso::

      :doc:`/config/options_general` /
      :doc:`/config/options_profiles` /
      :doc:`/config/options_metadata` /
      :doc:`/config/options_tags` /
      :doc:`/config/options_cover` /
      :doc:`/config/options_filerenaming` /
      :doc:`/config/options_fingerprinting` /
      :doc:`/config/options_cdlookup` /
      :doc:`/config/options_plugins` /
      :doc:`/config/options_interface` /
      :doc:`/config/options_scripting` /
      :doc:`/config/options_advanced`

.. only:: not latex

   .. toctree::
      :hidden:

      /config/options_general
      /config/options_profiles
      /config/options_metadata
      /config/options_tags
      /config/options_cover
      /config/options_filerenaming
      /config/options_filerenaming_editor
      /config/options_filerenaming_compat
      /config/options_fingerprinting
      /config/options_cdlookup
      /config/options_plugins
      /config/options_interface
      /config/options_scripting
      /config/options_advanced

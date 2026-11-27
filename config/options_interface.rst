.. MusicBrainz Picard Documentation Project

:index:`User Interface Options <pair: configuration; user interface>`
=====================================================================

.. only:: not latex

   .. image:: images/options-interface.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-interface.png
      :width: 75%
      :align: center

.. _opt_interface_show_text_labels_under_icons:

**Show text labels under icons**

   If this option is disabled, the text labels under the icons in the toolbar will not be displayed, causing the toolbar to appear a little smaller.

.. _opt_interface_show_icons_in_menus:

**Show icons in menus**

   Some users prefer to disable menu icons, which is the default behavior for macOS systems. This option allows the user to select whether the icons are displayed in the menus.

.. _opt_interface_user_interface_language:

**User interface language**

   By default, Picard will display in the language displayed by your operating system, however you can override this and select a different language if needed.

.. _opt_interface_user_interface_color_theme:

**User interface color theme**

   This option allows the user to select the color theme used by Picard. On macOS and Windows systems, the available choices are:

   * Default - The default color scheme based on the operating system display settings.
   * Light - A light display theme.
   * Dark - A dark display theme.

   .. note::

      The colors for the light and dark themes can be customized in the :doc:`options_interface_colors` section. Separate sets of color selections are maintained for the light and dark themes. The colors for the currently displayed theme are the ones displayed for editing.

.. _opt_interface_allow_selection_of_multiple_directories:

**Allow selection of multiple directories**

   Enabling this option will bypass the native directory selector and use Qt's file dialog. This may be desirable since the native directory selector generally doesn't allow you to select more than one directory. This applies to the :menuselection:`"File --> Add folder"` dialog. The file browser always allows multiple directory selection.

   .. warning::

      When enabling the multiple directories option setting Picard will no longer use the system file picker for selecting directories. This may result in reduced functionality.

.. _opt_interface_show_a_confirmation_dialog_when_saving:

**Adjust horizontal position in file browser automatically**

   When this is enabled, Picard will automatically scroll the file browser display to keep relevant content visible.

.. _opt_interface_begin_browsing_in_the_following_directory:

**Begin browsing in the following directory**

   By default, Picard remembers the last directory used to load files. If you enable this option and provide a directory, Picard will always start in the directory provided.

.. only:: html and not epub

   .. seealso::

      Details:
      :doc:`options_interface_colors` /
      :doc:`options_interface_top_tags` /
      :doc:`options_interface_quick_menu` /
      :doc:`options_interface_coverart_box` /
      :doc:`options_interface_toolbar` /
      :doc:`options_interface_hints`

.. toctree::
   :hidden:

   options_interface_colors
   options_interface_top_tags
   options_interface_quick_menu
   options_interface_coverart_box
   options_interface_toolbar
   options_interface_hints

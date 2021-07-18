.. MusicBrainz Picard Documentation Project

Option Profiles
===============

As of version 2.7, Picard supports multiple profiles that can allow the user to quickly switch between option settings.

How Option Profiles Work
------------------------

A profile is defined by a set of options it manages.  For example, one profile may include settings for file naming such as
the target directory and which file naming script to use, while another profile may include different settings for the same
options or different options entirely (or some of each).  Profiles are stacked and processed in the order specified by the
user, from top to bottom with the lowest level being the system's "user settings" profile.  Each user-defined profile can be
enabled or disabled independently from the other user-defined profiles.  The system's "user settings" profile is always
enabled and includes all options.

When an option value is retrieved as part of Picard's processing, it comes from the first enabled profile in the stack that
manages that option. Initially, the profile stack contains only the system's "User base settings" profile, which holds the
default settings for the user.

Example of Using Profiles
-------------------------

For this example, the user would like to define a set of options with alternate values, in this case a target directory where
audio files are saved (option ``move_files_to``).

The user creates a new profile (named "TargetMyDir"), adds the option ``move_files_to`` to it, and enables this profile.
The stack is now:

.. code-block::

   [x] TargetMyDir    move_files_to
   [x] user settings  move_files_to  [plus all other settings]

Since the profile "TargetMyDir" is enabled, the value for ``move_files_to`` is retrieved from this profile.  The "user settings"
still has the old ``move_files_to`` value.

Now the user wants to work on another set of music files, wanting to disable ``windows_compatibility`` for this set and save
them to the "not_for_windows" directory.

They create a new profile (named "ByeByeWin"), add options ``move_files_to`` and ``windows_compatibility``, and enable it.
Now the stack looks like:

.. code-block::

   [x] ByeByeWin      move_files_to  windows_compatibility
   [x] TargetMyDir    move_files_to
   [x] user settings  move_files_to  windows_compatibility  [plus all other settings]

They change the values of ``move_files_to`` (to "not_for_windows") and ``windows_compatibility`` (to false) for this new profile.
Now when they process their files, the files are saved to the "ByeByeWin" ``move_files_to`` directory, with ``windows_compatibility`` = false.

Now the user wants to save files to the "TargetMyDir" target directory again, with their usual options.  To do this they simply
disable the "ByeByeWin" profile (which can later be re-enabled if needed).  The stack looks like:

.. code-block::

   [ ] ByeByeWin      move_files_to  windows_compatibility
   [x] TargetMyDir    move_files_to
   [x] user settings  move_files_to  windows_compatibility  [plus all other settings]

Finally, to return to their usual output directory the user only has to disable the "TargetMyDir" profile so the stack is:

.. code-block::

   [ ] ByeByeWin      move_files_to  windows_compatibility
   [ ] TargetMyDir    move_files_to
   [x] user settings  move_files_to  windows_compatibility  [plus all other settings]


Managing Option Profiles
------------------------

All option profile management is done within the Option Profile Editor screen available from the :menuselection:`"Options -->
Option Profiles..."` item on the menu bar.  From this screen you will be able to add, copy, edit, remove, enable and disable
profiles, as well as setting the order of the profile stack.

Initially, the list of profiles will be empty.  To create a new profile click on the :guilabel:`New` button.  This will create a
profile with no options selected for the profile to manage.  To rename the profile, right-click on the profile name and
select the :menuselection:`"Rename profile"` command.  The list of options that the profile is to manage are selected from the
list in the right-hand pane.  Options can be selected either by group or individually.  The groups can be expanded to see
the individual options belonging to that group.

.. image:: images/user_profiles1.png
   :width: 100 %

You can see the value currently assigned to a profile's option setting by hovering your cursor over the setting in the list. The
value will be displayed as a tooltip for the setting.

.. image:: images/option-setting-value-tooltip.png
   :width: 100 %

The profiles stack order can be rearranged either by selecting a profile and using the up and down arrow buttons below the
list, or by dragging the profile to a new position in the stack.  Profiles are enabled when the box beside the profile's name
is checked.

When you are satisfied with your changes, click the :guilabel:`Make It So!` button to store them and exit the profile editor screen.
Use the :guilabel:`Cancel` button to exit without saving your changes.

.. note::

   Creating a new profile, or adding new options to an existing profile, does not save the settings for the options.  Settings
   must be updated in the :menuselection:`"Options..."` window, as described in the following section.

Saving Profile Option Settings
------------------------------

To save a value to a profile option setting, simply select the target profile in the :menuselection:`"Options..."` window, make
the desired changes, and then click the :guilabel:`Make It So!` button.

.. image:: images/options-profile-selector.png
   :width: 100 %

The changes will only be applied to the selected profile, and only for option settings managed by the profile — all other changes will
be ignored.  The default target is "User base settings" which is the user's normal settings, and includes all options.  If no option
profiles have been defined, this "Save settings to:" section will not be displayed in the :menuselection:`"Options..."` window.

Whenever a profile is selected in the "Save settings to:" section, the setting values displayed are updated to show the values that
are associated with the profile. Any option settings not managed by the profile will display the values for the user's base settings.

From the :menuselection:`"Options..."` window you will also be able to see which profiles, if any, manage any of the options on
the current page.  This is done by clicking the :guilabel:`Attached Profiles` button beside the output target profile selector.

.. image:: images/options-attached-profiles.png
   :width: 100 %


.. MusicBrainz Picard Documentation Project

:index:`Metadata Pane <user interface; metadata pane>`
=======================================================

When a file is selected in the Cluster Pane, the Metadata Pane will display the differences between the original tags found in the file metadata and the new tags that will be written to the file.

When a track is selected in the Album Pane and there is no file matched to the track, the Metadata Pane will display the differences between the original tags found in the metadata retrieved from MusicBrainz and the new tags that will be written to the file.

When a file that has been matched to a track is selected in the Album Pane, the Metadata Pane will display the differences between the original tags found in the file and the new tags that will be written to the file.

In all cases, the original metadata is displayed in the middle column, and the new metadata is displayed in the right-hand column.

.. only:: not latex

   .. image:: images/metadata-pane-differences.png
      :align: center

   |

.. only:: latex

   .. image:: images/metadata-pane-differences.png
      :width: 90%
      :align: center


Note that selected files can be saved from either the Cluster Pane, or the Album Pane when matched to a track. The tags written will be those associated with the appropriate save location.


Tag Differences Display
------------------------

When there are differences between the original and new metadata tags, Picard will highlight the differences for easy identification of the changes. Additions will be highlighted in green, and deletions will be highlighted in red.

In addition, the tag name in the first column will be highlighted in a different color. Modified tags will be highlighted in yellow, added tags will be highlighted in green, and deleted tags will be highlighted in red.


Tag Actions
------------

A number of actions can be taken with respect to a tag in the Metadata Pane. These include:

- Editing the tag's value
- Adding the tag to the "Preserve Tags" list
- Removing the tag
- Copying the tag's value to the clipboard
- Replacing the tag's value by pasting from the clipboard

These actions can be accessed from the context menu brought up by right-clicking on a tag.

.. only:: not latex

   .. image:: images/metadata-pane-context-menu.png
      :align: center

   |

.. only:: latex

   .. image:: images/metadata-pane-context-menu.png
      :width: 90%
      :align: center

The context menu also provides actions to add a new tag, and an option to display the changed tags at the top of the list.


:index:`Editing Metadata <user interface; editing metadata>`
-------------------------------------------------------------

To begin editing a tag's value, you can double-click the value to edit it in-place. You can also edit the tag in the tag editor, brought up from the context menu or by pressing :kbd:`Alt+Shift+E`. Note that double-clicking a multi-value tag always opens the tag editor.

.. only:: not latex

   .. image:: images/metadata-pane-tag-editor.png
      :align: center

   |

.. only:: latex

   .. image:: images/metadata-pane-tag-editor.png
      :width: 90%
      :align: center

Note that the tag editor displays multi-value tags as a list of tags, and normal tags as a list with only one item.

From the tag editor, you can select which tag to edit from the drop down list at the top of the editor. You can also add a new tag by entering the new tag name in the tag selector.

Once you have edited a tag, the right-click context menu for that tag shows two additional actions:

- Use Original Values: This will reset the tag back to the original value.
- Merge Original Values: This will merge the original values into the list of current values, creating a multi-value tag as required.

You can edit multiple files or tracks at once by selecting them in the Cluster Pane or Album Pane before performing the edits. The edits will change the values for all selected items to the same value. This should be used with caution because you could end up with unwanted results, such as accidentally setting all track titles to be the same.


:index:`Copying and Pasting Tags <user interface; copying and pasting tags>`
----------------------------------------------------------------------------

Tag values can be copied to the clipboard and pasted, either into another tag or into other files or tracks. The behavior depends on how much you have selected. The :guilabel:`Copy` and :guilabel:`Paste` actions are available from the context menu, and can also be performed using the standard :kbd:`Ctrl+C` and :kbd:`Ctrl+V` keyboard shortcuts (:kbd:`Cmd+C` and :kbd:`Cmd+V` on macOS).

Copying
~~~~~~~

When a single cell is selected, its value is copied to the clipboard as plain text. Copying a cell in the first column copies the tag name, while copying a cell in the original or new value column copies that value. The individual values of a multi-value tag are joined together with a semicolon and a space.

When more than one cell is selected, the selected tags and their values are copied as a set. Picard places two representations on the clipboard at the same time. One is an internal representation that is used when pasting back into Picard. The other is a tab-separated representation, with one line per tag containing the tag name, the original value and the new value, that can be pasted into a spreadsheet or a text editor.

Pasting
~~~~~~~

When the clipboard contains plain text, pasting replaces the value of the currently selected cell in the new value column. Multiple values can be pasted by separating them with a semicolon and a space.

When the clipboard contains a set of tags that was copied from Picard, pasting applies all of those tags to the currently selected files or tracks at once. The existing values of those tags are replaced, and any tags that were removed in the copied selection are also removed from the selected files or tracks.

Note that read-only tags, such as the track length, cannot be pasted into and will be skipped. If the clipboard does not contain any data that Picard can use, a message will be shown in the status bar.

Note that pasting a set of tags takes effect immediately and can change many tags across all of the selected files or tracks. Because Picard does not currently provide an undo function, this should be used with caution to avoid unintended changes, such as accidentally overwriting the tags of several files at once.

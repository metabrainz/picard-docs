.. MusicBrainz Picard Documentation Project

Custom Columns
==============

Beginning with Picard v3, you can create your own columns in Picard's Cluster and Album panes to display additional information about your music files and albums. You can enter a simple variable (e.g., ``%artist%``) or a full Picard script to compute the value shown.


Opening the Custom Columns Manager
----------------------------------

To access the Custom Columns manager:

1. Right-click any column header in the Cluster or Album pane.
2. Click "Manage Custom Columns…". If the option is disabled, you must first uncheck "Lock columns" in the same menu.

.. only:: not latex

   .. image:: images/custom_columns_1.png
      :align: center

   |

.. only:: latex

   .. image:: images/custom_columns_1.png
      :align: center
      :width: 75%

This will open a new window showing the manager, where you can add, edit and remove custom column definitions.

.. only:: not latex

   .. image:: images/custom_columns_2.png
      :align: center

   |

.. only:: latex

   .. image:: images/custom_columns_2.png
      :align: center
      :width: 100%

Select an item from the list to edit or :guilabel:`Delete` it, or click :guilabel:`New` or :guilabel:`Duplicate` to create a new custom column item.

The details for the selected item can be edited in the middle section, and include:

- **Column Title**: The column title you'll see in the header.
- **Expression**: The Picard script to compute the value. This can be as simple as a single tag like ``%artist%`` or ``%album%``, or a more complex script.
- **Width**: The width of the column. Leave this blank for automatic sizing.
- **Align**: How the column should be aligned (left or right)
- **Sorting**: How the values in the column are sorted (Default, Case Insensitive, Numeric, Natural, etc.)
- **Add to views**: The sections in which the custom column could be applied: Cluster pane (File view) and/or Album pane (Album view)

Basic scripting function and tag documentation is also available.


Examples
--------

Adding a simple field column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To show "Bitrate" as a column in the Cluster pane, set the following values:

- **Column Title**: Bitrate
- **Expression**: ``%_bitrate%``
- **Align**: right (optional)
- **Sorting**: Natural (optional)
- **Add to views**: File view (checked)


Adding a script column
~~~~~~~~~~~~~~~~~~~~~~

To show "Artist - Title" with fallbacks, set the following values:

- **Column Title**: Artist - Title
- **Expression**:

.. code-block:: taggerscript

   $if2(%artist%,%albumartist%,Unknown Artist) - $if2(%title%,%album%,Unknown Title)

- **Align**: left
- **Sorting**: Case Insensitive (optional)
- **Add to views**: File view and Album view (both)

.. warning::

   For the best performance, any scripts used should be short and simple to avoid excessive processing.


Showing or Moving Columns
--------------------------

If you don't see your new column immediately, right-click the header and enable it from the list. New columns are added at the end. To move a column, drag the column header to the desired position.


Troubleshooting
---------------

**Column not visible**

   Ensure the correct view is selected and enable the column from the header menu.

**Wrong position**

   Drag the column header to the desired position.

**Script errors**

   Simplify the expression and verify your ``%field%`` names and functions.


Best Practices and Tips
-----------------------

Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Keep scripts simple**: Complex scripts with many nested functions can slow down the interface.
- **Use field references when possible**: Field references are faster than scripts for simple values.
- **Avoid redundant calculations**: Don't repeat the same script logic in multiple columns.
- **Test with large libraries**: Verify performance with your actual music collection.

Column Organization
~~~~~~~~~~~~~~~~~~~

- **Group related columns**: Place similar columns together (e.g., all technical information in one area).
- **Use meaningful names**: Choose descriptive column titles that clearly indicate the content.
- **Consider alignment**: Use 'right' alignment for numeric values, 'left' for text.
- **Set appropriate widths**: Leave the width blank for automatic sizing, or set specific widths for consistency.

.. seealso::

   For detailed information about the Picard scripting language, including all available functions and syntax, see :doc:`/extending/scripts`. For a complete list of available variables, see :doc:`/variables/variables`.

.. MusicBrainz Picard Documentation Project

Custom Columns
==============

Create your own columns in Picard's File and Album views to display additional information about your music files and albums. You can show a single tag (Field Reference) or the result of a Picard script (Script).

.. note::
   This feature was added in `PICARD-2103: Add UI to manage custom columns <https://github.com/metabrainz/picard/pull/2714>`_.

Opening the Custom Columns Manager
----------------------------------

To access the Custom Columns manager:

1. Right‑click any column header in File or Album view
2. Click "Manage Custom Columns…"
   - If the option is disabled, uncheck "Lock columns" in the same menu first

The manager provides options to Add…, Edit…, Duplicate, Delete, and "Make It So!" (apply) your changes.

Column Types
------------

**Field Reference**
   Show the value of one tag. Enter the field key only, without percent signs. Examples: ``artist``, ``albumartist``, ``catalognumber``, ``~bitrate``.

**Script**
   Show the result of a Picard script using functions like ``$if()``, ``$if2()`` and variables like ``%artist%``.

Common Options
--------------

- **Field Name**: The column title you'll see in the header
- **Type**: Field or Script
- **Expression**: The field key (Field) or the script (Script)
- **Width**: Leave blank for automatic sizing
- **Align**: LEFT or RIGHT
- **Add to views**: Choose File view and/or Album view
- **Insert after key**: Place the new column after an existing column key (e.g. ``title``, ``artist``, ``album``). Leave empty to append at the end

Click OK to confirm, then "Make It So!" to apply your changes.

Examples
--------

Adding a Script Column
~~~~~~~~~~~~~~~~~~~~~~

**Goal**: Show "Artist – Title" with sensible fallbacks, placed after the Title column.

**Steps**:

1. Right‑click header → "Manage Custom Columns…" → Add…
2. Set the following values:
   - **Field Name**: Artist – Title
   - **Type**: Script
   - **Expression**:

     .. code-block:: text

        $if(%title%,$if2(%artist%,Unknown Artist) - $if2(%title%,Unknown Title),$if2(%albumartist%,Unknown Artist) - $if2(%album%,Unknown Album))

   - **Align**: LEFT
   - **Add to views**: File view and Album view (both)
   - **Insert after key**: title
3. Click OK, then "Make It So!"

**Tips**:
- Use ``%field%`` variables and script functions like ``$if()``, ``$if2()``, ``$upper()``, ``$lower()``
- Keep scripts short for best performance

Adding a Field Reference Column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal**: Show Bitrate as a column in the File view, placed after Length.

**Steps**:

1. Right‑click header → "Manage Custom Columns…" → Add…
2. Set the following values:
   - **Field Name**: Bitrate
   - **Type**: Field
   - **Expression**: ``~bitrate``
   - **Align**: RIGHT (optional)
   - **Add to views**: File view (checked), Album view (optional)
   - **Insert after key**: length
3. Click OK, then "Make It So!"

**Other field ideas**: ``catalognumber``, ``releasecountry``, ``media``, ``originalyear``, ``~channels``

Advanced Script Examples
~~~~~~~~~~~~~~~~~~~~~~~~

**Show release country with flag emoji**:

.. code-block:: text

   $if(%releasecountry%,%releasecountry% 🇺🇸,%releasecountries% 🌍)

**Display track length in seconds**:

.. code-block:: text

   $if(%length%,$replace(%length%,:,$mul($left(%length%,$sub($pos(%length%,:),1)),60)$add($right(%length%,$sub($len(%length%),$pos(%length%,:))),0)),0)

**Show artist with role information**:

.. code-block:: text

   $if(%performer%,%artist% (%performer%),%artist%)

**Display catalog number with label**:

.. code-block:: text

   $if(%catalognumber%,%label% %catalognumber%,%label%)

**Show recording date vs release date**:

.. code-block:: text

   $if(%recording_firstreleasedate%,%recording_firstreleasedate% (rec.),%date% (rel.))

Managing Your Columns
---------------------

Showing or Moving Columns
~~~~~~~~~~~~~~~~~~~~~~~~~

- If you don't see your new column immediately, right‑click the header and enable it from the list
- Drag the header to reorder, or use "Insert after key" when creating/editing

Editing, Duplicating, and Deleting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Select a row in the manager and click Edit…, Duplicate, or Delete
- Changes take effect after "Make It So!". Closing the window also applies pending changes

Troubleshooting
---------------

**Column not visible**
   Ensure the correct view(s) are selected and enable it from the header menu.

**Wrong position**
   Provide a valid existing key in "Insert after key" (e.g. ``title``, ``artist``, ``album``, ``length``).

**Script errors**
   Simplify the expression and verify your ``%field%`` names and functions.

Best Practices and Tips
-----------------------

Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Keep scripts simple**: Complex scripts with many nested functions can slow down the interface
- **Use field references when possible**: Field references are faster than scripts for simple values
- **Avoid redundant calculations**: Don't repeat the same script logic in multiple columns
- **Test with large libraries**: Verify performance with your actual music collection

Column Organization
~~~~~~~~~~~~~~~~~~~

- **Group related columns**: Place similar columns together (e.g., all technical info in one area)
- **Use meaningful names**: Choose descriptive column titles that clearly indicate the content
- **Consider alignment**: Use RIGHT alignment for numeric values, LEFT for text
- **Set appropriate widths**: Leave width blank for automatic sizing, or set specific widths for consistency

Script Writing Tips
~~~~~~~~~~~~~~~~~~~

- **Test incrementally**: Build complex scripts step by step, testing each addition
- **Use fallbacks**: Always provide fallback values with ``$if2()`` for missing data
- **Handle empty values**: Check for empty strings and provide meaningful defaults
- **Document your scripts**: Add comments in your script expressions for future reference

Common Patterns
~~~~~~~~~~~~~~~

**Conditional display**:

.. code-block:: text

   $if(%field%,%field%,Default Value)

**Multiple fallbacks**:

.. code-block:: text

   $if2(%primary%,%secondary%,%tertiary%,Unknown)

**Formatting with separators**:

.. code-block:: text

   $if(%artist%,%artist% - %title%,%album%)

**Numeric formatting**:

.. code-block:: text

   $if(%rating%,%rating%/5,No Rating)

Field Reference Keys
--------------------

Use these keys in Field Reference columns (no percent signs). Track and Album rows can show most music tags; File rows can also show technical file info (prefixed with ``~``).

**Common examples**:
- **title**: Track title
- **artist**: Track artist(s)
- **album**: Release title
- **albumartist**: Release artist(s)
- **~bitrate**: File bitrate (kbps)
- **~filesize**: File size (bytes)
- **catalognumber**: Label catalog number
- **releasecountry**: Release country code
- **rating**: Community rating 0–5
- **length**: Track length mins:secs

.. seealso::
   For detailed information about the Picard scripting language, including all available functions and syntax, see :doc:`/extending/scripts`.
   For a complete list of available variables, see :doc:`/variables/variables`.

# Documentation Style Guide

The following sections are intended to provide some guidance when preparing or modifying the Picard Documentation source files.


## File Type

The documentation preparation and generation is handled by [Sphinx](https://www.sphinx-doc.org). Although Sphinx can process both [RestructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) (\*.rst) and Markdown (\*.md) input files, the decision was made to use RestructuredText files for this project. The primary reason for this decision was the superior handling of links and bookmarks provided by RestructuredText.

Submitted pull requests should provide new content or changes in `*.rst` files. If you are not familiar with RestructuredText and are unable to provide the submission in this format, please contact us for assistance in preparing the changes in the appropriate format.


## Document Structure

The following should be considered when adding new sections and information to the documentation.

### Document hierarchy

Use a single top-level title per document page (file).

Headings should follow a strict depth order: `=` → `-` → `+` → `'`. Levels should never be skipped. For example:

```rst
Correct Use
===========

Second Level
------------

Third level
+++++++++++
```

and not:

```rst
Incorrect Use
=============

Directly jump to third level
++++++++++++++++++++++++++++
```

Adornment characters must be at least as long as the heading text. For example:

```rst
Correct
=======

Allowed
----------

Incorrect
+++++++
```

Each file should cover one distinct topic. Split large documents into multiple files linked via the `toctree::` directive.

### Sections and flow

Each major section should start with a one- or two-sentence orienting statement before diving into the details.

Procedures should go in numbered lists. Reference information should typically go in bulleted lists or tables. Concepts go in text.

Avoid nesting lists more than two levels deep.

Use the `note::`, `warning::`, and `seealso::` directives sparingly. Typically try to limit them to one per section.


## Writing Style

Remember that you are writing for humans, and that the document will be used by a mixed audience with varying levels of skill and understanding. The following considerations should help make the documentation clear and easy to read and understand for most users.

### Consistency

Try to follow the same structure and formatting everywhere.

### Voice and tone

Preference is to write in second person ("you") for instructions, and third person for conceptual explanations.

Write in a clear and direct tone, without being terse. Try to be friendly, but not casual. Do not use slang, idioms or local expressions because these don't always translate well into other languages.

### Clarity and precision

Try to use short paragraphs as much as possible so that the documentation is easier to read. Ideally, each paragraph should no be more than three to five lines in length.

When using acronyms, be sure to define each one on the first use in each document file.

Try to avoid using vague quantifiers like "many", "some" or "several". Be specific if possible.

Use one term consistently for one concept. For example, don't alternate between "config", "configuration", and "settings".

### Remember your audience

Since your audience is mixed, state prerequisites at the top of technical sections. For example, "This section assumes familiarity with Python."

Link to background material rather than explaining foundational concepts inline.


## General Style Considerations

Note that the original language for the documentation is English (typically US English). Some items such as case selection and spacing may differ for translations into other languages and locales. Please check the spelling and grammar before submitting your changes.

The following items indicate the preferred style elements for the base language documentation.

### Long lines

When content includes a lengthy paragraph, the preference is to provide this as a single long line rather than multiple shorter lines manually wrapped. For example:

    This is an example of a
    long paragraph that has
    been word wrapped by
    splitting the line into
    multiple short lines in
    the file. This is not
    the preferred method
    for submitting the file.

The preferred method would be to provide this as a single long line as:

    This is an example...submitting the file.

Note that most editors can be configured to enable soft line breaks, allowing you to enter long lines that will be displayed as wrapped within the editor but will be saved as a single line without the line breaks.

### Spacing between sentences

The preference is to provide a single space between sentences. For example:

    This is the preferred. One space.
    This is not the way to do it.  Two spaces.
    This is also not the way to do it.No spaces.

### Case Selection

First and second level section titles should be entered in ***Title Case***. The exception to this is items in the Frequently Asked Questions (FAQ) section that are shown as questions, which should be entered in ***Sentence case***.

Third and subsequent level titles should be entered in ***Sentence case***.

### Use of lists

Numbered lists should be used for procedural steps.

General grouping of items should use bulleted lists.

### Emphasizing words and phrases

**Bold** and *italic* formatting can be used to effectively emphasize specific words or phrases. Care must be taken not to overuse this formatting.

## RestructuredText Considerations

The following are considerations and preferences related to RestructuredText roles, directives, references and other elements.

### Header levels

The general convention for identifying header levels (by underlining the header) is to use the following characters for the underline:

- Level 1 (Top Level): `=` (equals sign)
- Level 2: `-` (dash / minus sign)
- Level 3: `+` (plus sign)
- Level 4: `'` (apostrophe)

For example:

```rst
Top Level Heading
=================

Second Level Heading
--------------------

Third level heading
+++++++++++++++++++

Fourth level heading
''''''''''''''''''''
```

### Indentation

Indentation should be done using spaces and not tab characters. Standard indentation is three spaces for blocks of text or directives in RestructuredText files.

### Link references

Use descriptive link text. Never use phrases like "click here" or bare URLs.

When links are within the site, such as those in `:doc:` roles, they should use relative references. For example:

```rst
:doc:`correct <../about_picard/contributing>
:doc:`incorrect </about_picard/contributing>
```

Internal cross-references should use RestructuredText labels, and not hardcoded file paths. For example:

```rst
.. _ref_example

This is the section that will be referenced.

To provide a link to this section in another part of the document, use :ref:`referenced section <ref_example>`.
```

Use `:doc:` roles to refer to pages and `:ref:` roles to refer to specific sections or locations on a page.

Note that if the text portion of the `:ref:` and `:doc:` roles is omitted, the first header in the referenced section or document will be used as the link text. This can slightly reduce the effort when translating into another language, and help ensure a consistent title for the referenced item.

### Keyboard references

Keyboard references are shown using the `:kbd:` role, with each key separated by a plus sign with no surrounding spaces. For example:

```rst
:kbd:`Ctrl+E`
:kbd:`⌘+E`
```

Standard key names used include `Ctrl` (`⌘` for macOS), `Shift` (`⇧` for macOS), `F1` (`⌘+?` for macOS) through `F12`, `Alt` (`⌥` for macOS), `Ins`, `Del` (`⌘+⌫` for macOS), `Tab` and `Space`.

### Button references

Buttons can be displayed within a line of text by using the `:guilabel:` role. For example:

```rst
Click :guilabel:`Make It So!` to save your settings.
```

### Menu references

References to items from the menu bar should be entered using the `:menuselection:` role. Submenu item selections can be indicated by entering the selection chain, with each menu / submenu separated by `-->`. Menu bar selections or selection chains may be enclosed in double quotes (`"`) for clarity. For example:

```rst
Add your files using :menuselection:`"Files --> Add Files…"` or :menuselection:`"Files --> Add Folder…"`.
```

### Code blocks

Although RestructuredText allows identifying a code block by indenting the code following a paragraph ending with two colon characters (::), the preferred method for this documentation is to enter it as a [`code-block::`](https://documatt.com/restructuredtext-reference/element/code-block.html) directive. For example:

```rst
This type of code block definition should not be used::

    $set(album,%album%$if(%_releasecomment%, \(%_releasecomment%\)))

The preferred method is define the code block as a directive, such as:

.. code-block:: taggerscript

    $set(album,%album%$if(%_releasecomment%, \(%_releasecomment%\)))
```

The `code-block::` directive is preferred over the `code::` directive for consistency, and because it provides additional configuration options.

Whenever possible, a specific language argument should be included with the directive. In addition to the standard [code languages](https://pygments.org/languages/), the custom language "taggerscript" is available. If there is no applicable language available, the language argument should be set to "none".

Inline code such as filenames, command lines and variable names should be enclosed using double backticks so that they are rendered as code. For example:

```rst
The ``date`` argument is the date to use in the function, provided in the format "YYYY-MM-DD".
```

### Tables

In general, list tables are preferred over simple tables. For example:

```rst
.. list-table::
   :header-rows: 1

   * - Name
     - Value
   * - Item A
     - 123
```

is preferred over:

```rst
+-----------+-----------+
| Name      | Value     |
+===========+===========+
| Item A    | 123       |
+-----------+-----------+
```

### Admonitions

[Admonition directives](https://documatt.com/restructuredtext-reference/admonitions.html) such as `note::`, `caution::`, `warning::` and `seealso::` can be an effective way to emphasize specific information to the user. Care must be taken to strike a proper balance and not overuse admonitions.

### Images

The preferred format for images used in documentation pages is Portable Network Graphics (PNG). Images should not contain any spaces in the file name, and should be stored in the appropriate section's `images` directory. For example:

- Wrong: `config/my_image.png` (not in the `images` directory)
- Wrong: `config/images/my image.png` (space in the image file name)
- Right: `config/images/my_image.png`

Images should be scaled appropriately for display in the documentation page, and appropriately placed on the page. Typically images will be placed above the text describing or explaining the image, and horizontally centered. In some cases it may be more appropriate to place the image either left or right justified, with the text beside the image. Typically this would be done if the image is small or tall and narrow.

Large images should be typically scaled at 75% to 80% width (as appropriate) and horizontally centered for the PDF pages (latex), and no scale specified for the HTML pages because they will be auto scaled down to 100% width if necessary by the software. Typically a new line needs to be forced after the image for the HTML pages to avoid having the following text appear crowded immediately below the image. This is done by inserting a line containing a single vertical bar. For example:

```rst
.. only:: not latex

   .. image:: images/options-player.png
      :align: center
      :alt: Built in media player

      |

.. only:: latex

   .. image:: images/options-player.png
       :width: 75%
       :align: center
       :alt: Built in media player
```

For accessibility, it is generally good practice to include an `:alt:` option to provide alternate text for an image.

### Index entries

Topics can be included with a [page number reference](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#index-generating-markup) in the generated PDF documentation by using the `:index:` role or `index::` directive. Typically the role is used to provide references to specific portions of a paragraph rather than a whole block of text as provided by the directive. For example:

```rst
Use :menuselection:`"Tools --> Cluster"` to group the files into album :index:`clusters <pair: cluster; lookup>`.
```

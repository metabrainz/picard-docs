.. MusicBrainz Picard Documentation Project

.. _func_initials:

$initials
=========

| Usage: **$initials(text)**
| Category: text
| Implemented: Picard 0.12

**Description:**

Returns the first character of each word in ``text``, if it is an alphabetic character.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,This is a test)
    $initials(%foo%)               ==>  "Tiat"
    $initials(This is a test)      ==>  "Tiat"
    $initials(This is a 123 test)  ==>  "Tiat"

.. MusicBrainz Picard Documentation Project

$trim
=====

| Usage: **$trim(text[,character])**
| Category: text

**Description:**

Trims all leading and trailing whitespaces from ``text``. The optional second parameter ``character``
specifies the character to trim.  If multiple characters are provided in ``character``, each character
will be applied separately to the function.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $trim(  Trimmed  )       ==>  "Trimmed"
    $trim(__Trimmed__,_)     ==>  "Trimmed"
    $trim(x__Trimmed__y,_x)  ==>  "Trimmed__y"

.. Picard Function

$trim
=====

| Usage: **$trim(text[,char])**
| Category: text

**Description:**

Trims all leading and trailing whitespaces from ``text``. The optional second parameter ``char``
specifies the character to trim.  If multiple characters are provided in ``char``, each character
will be applied separately to the function.


**Examples:**

The following statements will return the values indicated::

    $trim(  Trimmed  )       ==>  "Trimmed"
    $trim(__Trimmed__,_)     ==>  "Trimmed"
    $trim(x__Trimmed__y,_x)  ==>  "Trimmed__y"

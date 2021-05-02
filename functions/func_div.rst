.. MusicBrainz Picard Documentation Project

$div
====

| Usage: **$div(x,y,\*args)**
| Category: mathematical

**Description:**

Divides x by y and returns the integer value (rounded down). Can be used with an arbitrary
number of arguments (i.e.: ``$div(x,y,z)`` = (x / y) / z). If an argument is empty or not
an integer, the function will return an empty string.  If the second or any subsequent
argument is zero, the function will return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $div(10,3)      ==> "3"
    $div(10,-3)     ==> "-4"
    $div(-10,3)     ==> "-4"
    $div(10,3,2)    ==> "1"
    $div(10,-3,-2)  ==> "2"
    $div(10,2,1.5)  ==> ""
    $div(10,2,0)    ==> ""
    $div(10,2,x)    ==> ""
    $div(10,2,)     ==> ""

.. MusicBrainz Picard Documentation Project

.. _func_num:

$num
====

| Usage: **$num(number,length)**
| Category: text

**Description:**

Returns ``number`` formatted to ``length`` digits, where ``number`` and ``length`` are integers and ``length`` cannot be greater than 20.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $num(,)        ==>  ""
   $num(,1)       ==>  "0"
   $num(a,)       ==>  ""
   $num(a,5)      ==>  "00000"
   $num(123,5)    ==>  "00123"
   $num(1.23,5)   ==>  "00000"
   $num(123,)     ==>  ""
   $num(123,0)    ==>  "123"
   $num(123,1)    ==>  "123"
   $num(123,20)   ==>  "00000000000000000123"
   $num(123,50)   ==>  "00000000000000000123"
   $num(123,5.5)  ==>  ""
   $num(1.23,10)  ==>  "0000000000"

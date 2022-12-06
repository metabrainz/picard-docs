.. MusicBrainz Picard Documentation Project

.. _func_min:

$min
====

| Usage: **$min(type,x,...)**
| Category: information
| Implemented: Picard 2.9

**Description:**

Returns the minimum value using the comparison specified in ``type``.

Possible values of ``type`` are "int" (integer), "float" (floating point), "text"
(case-sensitive text), "nocase" (case-insensitive text) and "auto" (automatically
determine the type of arguments provided), with "auto" used as the default
comparison method if ``type`` is not specified.  The "auto" type will use the
first type that applies to both arguments in the following order of preference:
"int", "float" and "text".

Can be used with an arbitrary number of arguments.  Multi-value arguments
will be expanded automatically.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $min(text,)                                  ==> ""
   $min(text,,a)                                ==> ""
   $min(text,a,)                                ==> ""
   $min(text,abc)                               ==> "abc"
   $min(text,abc,abcd,ac)                       ==> "abc"
   $min(text,A,a)                               ==> "A"
   $min(text,a,B)                               ==> "B"
   $min(text,2020-01-01,2020-01-02,2020-02)     ==> "2020-01-01"

   $min(int,1)                                  ==> "1"
   $min(int,1,2)                                ==> "1"
   $min(int,1,2,3.1)                            ==> ""
   $min(int,1,2,a)                              ==> ""
   $min(int,1,2,)                               ==> ""

   $min(float,1)                                ==> "1.0"
   $min(float,1,2)                              ==> "1.0"
   $min(float,1.1,2,3)                          ==> "1.1"
   $min(float,2.1,2.11,2.111)                   ==> "2.1"
   $min(float,1,2,a)                            ==> ""
   $min(float,1,2,)                             ==> ""

   $min(nocase,a,B)                             ==> "a"
   $min(nocase,a,B,c)                           ==> "a"

   $setmulti(mv,x; y; z)
   $min(text,%mv%)                              ==> "x"
   $min(text,a,%mv%)                            ==> "a"
   $min(text,x; y; z)                           ==> "x"
   $min(int,5,4; 6; 3)                          ==> "3"
   $min(float,5.9,4.2; 6; 3.35)                 ==> "3.35"

   $min(,1,2)                                   ==> "1"
   $min(auto,1,2)                               ==> "1"
   $min(,1,2.1)                                 ==> "1.0"
   $min(auto,1,2.1)                             ==> "1.0"
   $min(,1,2.1,a)                               ==> "1"
   $min(auto,1,2.1,a)                           ==> "1"
   $min(,a,A)                                   ==> "A"
   $min(,a,B)                                   ==> "B"
   $min(auto,a,A)                               ==> "A"
   $min(auto,a,B)                               ==> "B"

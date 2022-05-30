.. MusicBrainz Picard Documentation Project

.. _func_max:

$max
====

| Usage: **$max(type,x,...)**
| Category: information
| Implemented: Picard 3.0

**Description:**

Returns the maximum value using the comparison specified in ``type``.

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

   $max(text,)                                  ==> ""
   $max(text,,a)                                ==> "a"
   $max(text,a,)                                ==> "a"
   $max(text,abc)                               ==> "abc"
   $max(text,abc,abcd,ac)                       ==> "ac"
   $max(text,A,a)                               ==> "a"
   $max(text,a,B)                               ==> "a"
   $max(text,2020-01-01,2020-01-02,2020-02)     ==> "2020-02"

   $max(int,1)                                  ==> "1"
   $max(int,1,2)                                ==> "2"
   $max(int,1,2,3.1)                            ==> ""
   $max(int,1,2,a)                              ==> ""
   $max(int,1,2,)                               ==> ""

   $max(float,1)                                ==> "1.0"
   $max(float,1,2)                              ==> "2.0"
   $max(float,1,2,3.1)                          ==> "3.1"
   $max(float,2.1,2.11,2.111)                   ==> "2.111"
   $max(float,1,2,a)                            ==> ""
   $max(float,1,2,)                             ==> ""

   $max(nocase,a,B)                             ==> "B"
   $max(nocase,a,B,c)                           ==> "c"

   $setmulti(mv,x; y; z)
   $max(text,%mv%)                              ==> "z"
   $max(text,a,%mv%)                            ==> "z"
   $max(text,x; y; z)                           ==> "z"
   $max(int,5,4; 6; 3)                          ==> "6"
   $max(float,5.9,4.2; 6; 3.35)                 ==> "6.0"

   $max(,1,2)                                   ==> "2"
   $max(auto,1,2)                               ==> "2"
   $max(,1.1,2)                                 ==> "2.0"
   $max(auto,1.1,2)                             ==> "2.0"
   $max(,1,2.1,a)                               ==> "a"
   $max(auto,1,2.1,a)                           ==> "a"
   $max(,a,A)                                   ==> "a"
   $max(,a,B)                                   ==> "a"
   $max(auto,a,A)                               ==> "a"
   $max(auto,a,B)                               ==> "a"

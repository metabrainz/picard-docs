.. MusicBrainz Picard Documentation Project

.. _func_lt:

$lt
===

| Usage: **$lt(x,y[,type])**
| Category: conditional

**Description:**

Returns "1" (True) if ``x`` is less than ``y`` using the comparison specified in ``type``.
Possible values of ``type`` are "int" (integer), "float" (floating point), "text"
(case-sensitive text), "nocase" (case-insensitive text) and "auto" (automatically determine
the type of arguments provided), with "auto" used as the default comparison method if ``type``
is not specified.  The "auto" type will use the first type that applies to both arguments in
the following order of preference: "int", "float" and "text".

.. note::

   The ``type`` argument was added in Picard v2.9.  Prior to that, if an argument
   was missing or was not an integer, the function would return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $lt(-1,0)                        ==>   "1" (True)
   $lt(6,6)                         ==>   "" (False)
   $lt(6.5,6.6)                     ==>   "1" (True)
   $lt(a,b)                         ==>   "1" (True)
   $lt(6,a)                         ==>   "1" (True)
   $lt(6.5,a)                       ==>   "1" (True)

   $lt(4,6,int)                     ==>   "1" (True)
   $lt(4,6.1,int)                   ==>   "" (False)
   $lt(6,a,int)                     ==>   "" (False)

   $lt(4,4.1,float)                 ==>   "1" (True)
   $lt(4.1,4.2,float)               ==>   "1" (True)
   $lt(4,6,float)                   ==>   "1" (True)
   $lt(6.5,a,float)                 ==>   "" (False)

   $lt(2020-01-01,2020-01-02,text)  ==>   "1" (True)
   $lt(abc,abcd,text)               ==>   "1" (True)
   $lt(abc,ac,text)                 ==>   "1" (True)
   $lt(A,a,text)                    ==>   "1" (True)
   $lt(B,a,text)                    ==>   "1" (True)
   $lt(a,A,text)                    ==>   "" (False)

   $lt(a,B,nocase)                  ==>   "1" (True)
   $lt(A,b,nocase)                  ==>   "1" (True)
   $lt(B,a,nocase)                  ==>   "" (False)
   $lt(b,A,nocase)                  ==>   "" (False)

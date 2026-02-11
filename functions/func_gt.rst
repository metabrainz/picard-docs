.. MusicBrainz Picard Documentation Project

.. _func_gt:

$gt
===

| Usage: **$gt(x,y[,type])**
| Category: conditional

**Description:**

Returns "1" (True) if ``x`` is greater than ``y`` using the comparison specified in ``type``. Possible values of ``type`` are "int" (integer), "float" (floating point), "text" (case-sensitive text), "nocase" (case-insensitive text) and "auto" (automatically determine the type of arguments provided), with "auto" used as the default comparison method if ``type`` is not specified. The "auto" type will use the first type that applies to both arguments in the following order of preference: "int", "float" and "text".

.. note::

   The ``type`` argument was added in Picard v2.9. Prior to that, if an argument was missing or was not an integer, the function would return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $gt(0,-1)                        ==>   "1" (True)
   $gt(6,6)                         ==>   "" (False)
   $gt(6.6,6.5)                     ==>   "1" (True)
   $gt(b,a)                         ==>   "1" (True)
   $gt(B,a)                         ==>   "" (False)
   $gt(a,6)                         ==>   "1" (True)
   $gt(a,6.5)                       ==>   "1" (True)

   $gt(6,4,int)                     ==>   "1" (True)
   $gt(6.1,4,int)                   ==>   "" (False)
   $gt(a,6,int)                     ==>   "" (False)

   $gt(4.1,4,float)                 ==>   "1" (True)
   $gt(4.2,4.1,float)               ==>   "1" (True)
   $gt(6,4,float)                   ==>   "1" (True)
   $gt(a,6.5,float)                 ==>   "" (False)

   $gt(2020-01-01,2020-01,text)     ==>   "1" (True)
   $gt(abcd,abc,text)               ==>   "1" (True)
   $gt(ac,abc,text)                 ==>   "1" (True)
   $gt(a,A,text)                    ==>   "1" (True)
   $gt(a,B,text)                    ==>   "1" (True)
   $gt(B,a,text)                    ==>   "" (False)

   $gt(B,a,nocase)                  ==>   "1" (True)
   $gt(b,A,nocase)                  ==>   "1" (True)
   $gt(a,B,nocase)                  ==>   "" (False)
   $gt(A,b,nocase)                  ==>   "" (False)

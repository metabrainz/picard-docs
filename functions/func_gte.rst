.. MusicBrainz Picard Documentation Project

.. _func_gte:

$gte
====

| Usage: **$gte(x,y[,type])**
| Category: conditional

**Description:**

Returns "1" (True) if ``x`` is greater than or equal to ``y`` using the comparison specified in ``type``. Possible values of ``type`` are "int" (integer), "float" (floating point), "text" (case-sensitive text), "nocase" (case-insensitive text) and "auto" (automatically determine the type of arguments provided), with "auto" used as the default comparison method if ``type`` is not specified. The "auto" type will use the first type that applies to both arguments in the following order of preference: "int", "float" and "text".

.. note::

   The ``type`` argument was added in Picard v2.9. Prior to that, if an argument was missing or was not an integer, the function would return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $gte(0,-1)                       ==>   "1" (True)
   $gte(6,6)                        ==>   "1" (True)
   $gte(6.6,6.5)                    ==>   "1" (True)
   $gte(b,a)                        ==>   "1" (True)
   $gte(B,a)                        ==>   "" (False)
   $gte(a,6)                        ==>   "1" (True)
   $gte(a,6.5)                      ==>   "1" (True)

   $gte(6,4,int)                    ==>   "1" (True)
   $gte(6.1,4,int)                  ==>   "" (False)
   $gte(a,6,int)                    ==>   "" (False)

   $gte(4.1,4,float)                ==>   "1" (True)
   $gte(4.2,4.1,float)              ==>   "1" (True)
   $gte(6,4,float)                  ==>   "1" (True)
   $gte(a,6.5,float)                ==>   "" (False)

   $gte(2020-01-02,2020-01,text)    ==>   "1" (True)
   $gte(abcd,abc,text)              ==>   "1" (True)
   $gte(ac,abc,text)                ==>   "1" (True)
   $gte(A,a,text)                   ==>   "" (False)
   $gte(a,B,text)                   ==>   "1" (True)
   $gte(B,a,text)                   ==>   "" (False)

   $gte(A,a,nocase)                 ==>   "1" (True)
   $gte(B,a,nocase)                 ==>   "1" (True)
   $gte(b,A,nocase)                 ==>   "1" (True)
   $gte(a,B,nocase)                 ==>   "" (False)
   $gte(A,b,nocase)                 ==>   "" (False)

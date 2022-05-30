.. MusicBrainz Picard Documentation Project

.. _func_lte:

$lte
====

| Usage: **$lte(x,y[,type])**
| Category: conditional

**Description:**

Returns "1" (True) if ``x`` is less than or equal to ``y`` using the comparison specified in ``type``.
Possible values of ``type`` are "int" (integer), "float" (floating point), "text"
(case-sensitive text), "nocase" (case-insensitive text) and "auto" (automatically determine
the type of arguments provided), with "auto" used as the default comparison method if ``type``
is not specified.  The "auto" type will use the first type that applies to both arguments in
the following order of preference: "int", "float" and "text".

.. note::

   The ``type`` argument was added in Picard v3.0.  Prior to that, if an argument
   was missing or was not an integer, the function would return an empty string.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $lte(-1,0)                       ==>   "1" (True)
   $lte(6,6)                        ==>   "1" (True)
   $lte(6.5,6.6)                    ==>   "1" (True)
   $lte(a,b)                        ==>   "1" (True)
   $lte(6,a)                        ==>   "1" (True)
   $lte(6.5,a)                      ==>   "1" (True)

   $lte(4,6,int)                    ==>   "1" (True)
   $lte(4,6.1,int)                  ==>   "" (False)
   $lte(6,a,int)                    ==>   "" (False)

   $lte(4,4.1,float)                ==>   "1" (True)
   $lte(4.1,4.2,float)              ==>   "1" (True)
   $lte(4,6,float)                  ==>   "1" (True)
   $lte(6.5,a,float)                ==>   "" (False)

   $lte(2020-01-01,2020-02,text)    ==>   "1" (True)
   $lte(abc,abcd,text)              ==>   "1" (True)
   $lte(abc,ac,text)                ==>   "1" (True)
   $lte(A,a,text)                   ==>   "1" (True)
   $lte(B,a,text)                   ==>   "1" (True)
   $lte(a,A,text)                   ==>   "" (False)

   $lte(a,B,nocase)                 ==>   "1" (True)
   $lte(A,b,nocase)                 ==>   "1" (True)
   $lte(B,a,nocase)                 ==>   "" (False)
   $lte(b,A,nocase)                 ==>   "" (False)

.. MusicBrainz Picard Documentation Project

.. _func_countryname:

$countryname
============

| Usage: **$countryname(country_code\[,translate])**
| Category: text
| Implemented: Picard 2.7

**Description:**

Returns the name of the country for the specified country code. If the country code is invalid an empty string will be returned. If ``translate`` is not blank, the output will be translated into the current locale language, otherwise it will be in English.


**Examples:**

Assuming that the user's locale has been set to Russian, the following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,ca)
   $countryname(%foo%)        ==>  "Canada"
   $countryname(%foo%,yes)    ==>  "Канада"
   $countryname(ca)           ==>  "Canada"
   $countryname(ca,)          ==>  "Canada"
   $countryname(ca, )         ==>  "Канада"
   $countryname(ca,yes)       ==>  "Канада"
   $countryname(INVALID)      ==>  ""
   $countryname(INVALID,yes)  ==>  ""

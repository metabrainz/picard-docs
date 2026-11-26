.. MusicBrainz Picard Documentation Project

.. _func_languagename:

$languagename
=============

| Usage: **$languagename(language_code[,translate])**
| Category: text
| Implemented: Picard 3.1

**Description:**

Returns the name of the language for the specified three-character `ISO 639-3 <https://en.wikipedia.org/wiki/ISO_639-3>`_ language code. If the language code is invalid an empty string will be returned. The returned name is in English by default. For example, ``$languagename(fra)`` returns "French". If ``translate`` is not blank, that English name is translated into the currently selected locale language.


**Examples:**

Assuming that the user's locale has been set to Russian, the following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,eng)
   $languagename(%foo%)        ==>  "English"
   $languagename(%foo%,yes)    ==>  "английский"
   $languagename(fra)          ==>  "French"
   $languagename(fra,)         ==>  "French"
   $languagename(fra, )        ==>  "французский"
   $languagename(fra,yes)      ==>  "французский"
   $languagename(INVALID)      ==>  ""
   $languagename(INVALID,yes)  ==>  ""

.. MusicBrainz Picard Documentation Project

$title
======

| Usage: **$title(text)**
| Category: text
| Implemented: Picard 2.1

**Description:**

Returns ``text`` with the first character in every word capitalized. Note that other
characters in the words will not be modified, which allows the preservation of all
upper-case acronyms such as "BBC".  To only have the first character of each word
capitalized you could first change the text to lower-case.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,tHe houR is upOn uS)
    $title(%foo%)          ==>  "THe HouR Is UpOn US"
    $title($lower(%foo%))  ==>  "The Hour Is Upon Us"

    $set(bar,THIS TEXT IS ALL CAPITALS)
    $title(%bar%)          ==>  "THIS TEXT IS ALL CAPITALS"
    $title($lower(%bar%))  ==>  "This Text Is All Capitals"

    $set(baz,AC/DC recorded live at the BBC studio in London)
    $title(%baz%)          ==>  "AC/DC Recorded Live At The BBC Studio In London"
    $title($lower(%baz%))  ==>  "Ac/Dc Recorded Live At The Bbc Studio In London"

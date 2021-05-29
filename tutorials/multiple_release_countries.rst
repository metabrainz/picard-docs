.. MusicBrainz Picard Documentation Project

Handling of :index:`multiple release countries <multiple release countries, release countries; multiple>`
-----------------------------------------------------------------------------------------------------------

.. From https://community.metabrainz.org/t/handling-of-multiple-release-countries-with-picard-2-3-1/465485

There has been quite some debate about some digital releases with a really long list of release countries added. Independent on your stand on this matter,
this has shown that there are some issues with how these releases are handled by Picard.

Let’s take the release **Bleach**, by Nirvana (MusicBrainz release
`adab3feb-1822-4d27-a997-db7d6c9688c0 <https://musicbrainz.org/release/adab3feb-1822-4d27-a997-db7d6c9688c0>`_) as an example.

By default Picard will write a single ``releasecountry`` tag to the files. Prior to v2.3.1, Picard had been populating the tag with what the MusicBrainz server
returned as the country for the release. If there were multiple release events, this country field was just filled with the first one in alphabetical order
(Afghanistan in our example). Picard v2.3.1 introduced some options to better handle this.


Using preferred release countries
==================================

The first improvement was automatic if you configured preferred release countries in :menuselection:`"Options --> Metadata --> Preferred Releases"`.
Picard will use the first country from the preferred release countries that is also in the list of release events. So if you have configured
preferred release countries to be Europe, Canada, Germany and UK, for our example that would mean the ``releasecountry`` tag gets set to Canada.


Using scripting to set a different country
==============================================

Picard v2.3.1 also added a new variable ``%_releasecountries%``, which provides the complete list of release countries for a release as a multi-value variable.
You can use this to set different values for the ``releasecountry`` tag.

For example, the following script would set it to "\[International\]" if there are 10 or more release countries:

.. code-block:: taggerscript

   $if($gte($lenmulti(%_releasecountries%),10),$set(releasecountry,[International]))

Of course you can adjust the count and the replacement text to your liking. You can also choose to save the entire list instead of just a single country to
this tag using the script:

.. code-block:: taggerscript

   $setmulti(releasecountry,%_releasecountries%)

Perhaps you prefer to limit this list to the first few entries. The following example just uses the first 6 countries:

.. code-block:: taggerscript

   $setmulti(releasecountry,$slice(%_releasecountries%,0,6))


What’s missing?
================

Countries are currently written to the tags as their ISO 3166-1 country code, with some special values added for historical countries and things like \[Europe\]
or \[Worldwide\]. These codes are not always easily recognizable or obvious, such as "DZ" for Algeria or "DE" for Germany. You can of course use scripting to
make these more readable.  For example, if you want to see "United Kingdom" instead of "GB" in this tag use:

.. code-block:: taggerscript

   $if($eq(%releasecountry%,GB),$set(releasecountry,United Kingdom))

This might work if you deal only with a couple of countries in your collection, or you just want to handle some special cases like using "Europe" instead of "XE"
such as in the following script:

.. code-block:: taggerscript

   $if($eq(%releasecountry%,XE),$set(releasecountry,Europe))
   $if($eq(%releasecountry%,XU),$set(releasecountry,[Unknown]))
   $if($eq(%releasecountry%,XW),$set(releasecountry,[Worldwide]))
   $if($eq(%releasecountry%,XG),$set(releasecountry,DDR))

Ideally, someone will add some helper functions for this, such as a ``$countryname()`` function that could be used to easily convert the code into a readable name.

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

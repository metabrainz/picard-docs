.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


I'm trying to load a release, but all I see is "Couldn't load album errors". What's up?
=============================================================================================================

If you get "Couldn't load album errors" for releases in Picard, this can occur for a number of reasons. Check the
following:

**1. Is the problem persistent for a given release?**

   Try waiting a minute or two, or even a bit longer and then try again with a right-click, "Refresh". Sometimes
   the servers are just overloaded and temporarily reject requests.

**2. Has the release been deleted from MusicBrainz?**

   If you are re-tagging files previously tagged with Picard, and get this error, the release has possibly been
   deleted. Try to right-click and use the "Lookup in browser" option to view the release on the website. If you can't
   find it, it may have been deleted. This could be because you tagged a pending release that was voted down, or tagged
   against a release that was deleted because editors decided it wasn't a valid release. This can happen for homebrew
   compilations, bad torrent or pirate rips, "advance" releases or very poorly added releases. Usually there will be an
   alternate release you can tag against, which you can find by searching or doing another clustered lookup from Picard.
   If you can't find a replacement and believe it has been deleted unfairly, `submit a new release
   <https://musicbrainz.org/doc/How_to_Add_a_Release>`_, supplying evidence of the tracklisting and as much information
   as possible to prove it is genuine and it may be accepted again.

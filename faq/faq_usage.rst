.. MusicBrainz Picard Documentation Project

Using Picard
============

How do I tag files with Picard?
--------------------------------

There is a separate section that explains the tagging process.  Please see :doc:`../usage/using` for details.


The green "Tagger" :index:`icon <tagger icon, icon; tagger>` disappeared from MusicBrainz.org, how do I get it back?
----------------------------------------------------------------------------------------------------------------------

This icon shows up when a manual lookup is performed via Picard using :menuselection:`"Tools --> Lookup"`.

Alternatively the parameter ``?tport=8000`` can be added to the end of almost any MusicBrainz URL and the green
tagger icons will continue to show up from then on.


I'm trying to :index:`load a release <release; load error, album; load error, error; couldn't load album>` in Picard, but all I'm seeing is "Couldn't load album errors". What's up?
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you get "Couldn't load album errors" for releases in Picard, this can occur for a number of reasons. Check the
following:

1. **Is the problem persistent for a given release?**

   |  Try waiting a minute or two, or even a bit longer and then try again with a right-click, "Refresh". Sometimes
      the servers are just overloaded and temporarily reject requests.

2. **Has the release been deleted from MusicBrainz?**

   |  If you are re-tagging files previously tagged with Picard, and get this error, the release has possibly been
      :index:`deleted <release; deleted>`. Try to right-click and use the "Lookup in browser" option to view the release on the website. If you can't
      find it, it may have been deleted. This could be because you tagged a pending release that was voted down, or tagged
      against a release that was deleted because editors decided it wasn't a valid release. This can happen for homebrew
      compilations, bad torrent or pirate rips, "advance" releases or very poorly added releases. Usually there will be an
      alternate release you can tag against, which you can find by searching or doing another clustered lookup from Picard.
      If you can't find a replacement and believe it has been deleted unfairly, `submit a new release
      <https://musicbrainz.org/doc/How_to_Add_a_Release>`_, supplying evidence of the track listing and as much information
      as possible to prove it is genuine and it may be accepted again.


I'm using macOS, where are my :index:`network folders <macos; network folders>` or drives?
---------------------------------------------------------------------------------------------

These should show up in the add file and add folder dialogs, but they aren't visible by default in the file browser
pane. If you want to see them in the file browser pane, right click in the pane and select "show hidden files". They
should then be visible in the :file:`/Volumes` folder.


macOS shows the app is :index:`damaged <macos; app damaged>`. How can I run Picard?
--------------------------------------------------------------------------------------

On macOS 10.12 and 10.13 there have been reports that sometimes the MusicBrainz Picard app
cannot be started and macOS shows an error message:

   "MusicBrainz Picard.app" is damaged and can't be opened. You should move it to the Trash.

This mostly seems to happen after moving the file to the Applications folder and seems to be
caused by Gatekeeper mistakenly marking the app as damaged.  To solve the issue open a terminal
and run::

    xattr -c "/Applications/MusicBrainz Picard.app"

This will clear the app being marked as damaged.  If you have placed the app in a different
location than :file:`/Applications` adjust the path in the command above accordingly.


Picard is installed on Linux as a Snap, how can I access removable media?
-------------------------------------------------------------------------

Picard installed as a Snap is running inside a sandbox and thus it does not have full access to all files and
folders on your system.  By default Picard has access to your home folder.  You can additionally give it access to
removable media by running the following command on a terminal:

.. code-block:: bash

   snap connect picard:removable-media


How do I manually add lyrics to a file?
---------------------------------------

Select the file that you want to edit and then right click in the metadata view at the bottom of the main screen.
Select "Add tag..." from the context menu displayed. This will open a new dialog for entering the tag information.
Select "lyrics" as the tag and enter the lyrics into the text box.

.. image:: /faq/images/add_lyrics.png
   :width: 100%

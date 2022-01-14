.. MusicBrainz Picard Documentation Project

.. _tutorial_naming_script:

Writing a :index:`File Naming Script <script; file naming, file naming script>`
==================================================================================

Writing a script to organize and name your files is actually not that hard -- just don’t get intimidated by all the
'$', '%' and parentheses. If you can write down a pattern like "**ARTIST - (YEAR) ALBUM NAME/TRACK - SONG TITLE**"
of how you want the files and folders named, you can quite easily translate this to the proper script.

To get started, first open the :doc:`/config/options_filerenaming_editor`, either by selecting :menuselection:`"Options --> Open file naming script editor..."`
from Picard's main menu bar or by clicking the :guilabel:`Edit script...` button on the :doc:`/config/options_filerenaming` configuration page.
From this screen, you can start a new script for your work.

Note that the use of a '/' in the formatting string separates the output directory from the file name. The formatting
string is allowed to contain any number of '/' characters. Everything before the last '/' is the directory location,
and everything after the last '/' becomes the file's name.  In our example, we only have one '/' character, meaning
that we will have one directory level for the album which will contain the songs for that album.

First, let's have a look at what we need. You see a list of the available tags in the :doc:`../variables/tags_basic` section.
We want the **ARTIST** name, so available tags for this could be ``albumartist`` or ``artist``. This should be the
name for an album folder, so ``albumartist`` sounds like what we need. To get the actual value for a tag you need to enclose
its name in percent signs. So let’s start:

.. code-block:: taggerscript

   %albumartist%

Now we want the **YEAR**. There is no ``year`` tag, but there is ``date``. Let’s use this for now. If we want to add
extra text like the "**-**" just write it down. We need to be careful with the parentheses, because those are special
variables in scripting. We need to prefix them with a backslash. Let’s add this all:

.. code-block:: taggerscript

   %albumartist% - \(%date%\)

Now we want the **ALBUM NAME**. That’s simple, just use ``album``:

.. code-block:: taggerscript

   %albumartist% - \(%date%\) %album%

That takes care of the directory portion of the renaming.  The next part is the **TRACK** number and **SONG TITLE**.  The
track number is available as ``tracknumber`` and the title of the track is simply ``title``.  Adding these to our script
we get:

.. code-block:: taggerscript

   %albumartist% - \(%date%\) %album%/%tracknumber% - %title%

You can see that this looks nearly like the pattern that we said we wanted at the start. It’s not perfect yet for a few
reasons.  What if there are 10 or more tracks on the album and they don't sort properly in the directory listing?  Also,
we get a full date instead of just the year. Finally, sometimes if you tag existing files they might not have the
``albumartist`` set, just ``artist``.

Let’s fix the track number first. We can take care of that by using the :ref:`func_num` function to add a leading zero to the
number shown for tracks 1 through 9:

.. code-block:: taggerscript

   %albumartist% - \(%date%\) %album%/$num(%tracknumber%,2) - %title%

Now let’s fix the **ARTIST**. We can fallback to using ``artist`` if ``albumartist`` is not available by using:

.. code-block:: taggerscript

   $if2(%albumartist%,%artist%) - \(%date%\) %album%/$num(%tracknumber%,2) - %title%

The :ref:`func_if2` function uses the first value that is not empty, so if ``albumartist`` is empty it uses ``artist`` instead.

For the ``date`` tag the dates from MusicBrainz are always formatted as YYYY-MM-DD. We only need the year, so let’s get
just the first 4 characters with the :ref:`func_left` function:

.. code-block:: taggerscript

   $if2(%albumartist%,%artist%) - \($left(%date%,4)\) %album%/$num(%tracknumber%,2) - %title%

What happens if there is no ``date`` tag information? Sometimes MusicBrainz does not have the release date of an album
set as it is not yet known or hasn't been entered into the database. It would be great to omit the entire date with the
parentheses in this case. Let’s use the :ref:`func_if` function to check whether the date is set:

.. code-block:: taggerscript

   $if2(%albumartist%,%artist%) - $if(%date%,\($left(%date%,4)\) )%album%/$num(%tracknumber%,2) - %title%

Alternately, we can enter a placeholder such a "**0000**" if the date is missing:

.. code-block:: taggerscript

   $if2(%albumartist%,%artist%) - \($if(%date%,$left(%date%,4),0000)\) %album%/$num(%tracknumber%,2) - %title%

And there you have it -- the final script for naming your files developed from the pattern that we used as our starting point.

.. seealso::

   For additional information about the available tags and variables please see the :doc:`../variables/variables` section.
   For information about the script functions available please see the :doc:`../functions/list_by_type` section.

.. raw:: latex

   \clearpage

..   \pagebreak
..   \newpage
..   \clearpage

.. MusicBrainz Picard Documentation Project

:index:`Scripts <scripts>`
===========================

There are two types of scripts used in Picard: the file naming script and tagging scripts. These are
managed from the "File Naming" and "Scripting" sections of the :menuselection:`"Options --> Options..."` menu. All scripts are written
using the :doc:`Picard scripting language <scripting>`. Scripts are often discussed in the
`MetaBrainz Community Forum <https://community.metabrainz.org/c/picard>`_, and there is a thread specific to
`file naming and script snippets <https://community.metabrainz.org/t/repository-for-neat-file-name-string-patterns-and-tagger-script-snippets/2786/>`_.

:index:`File Naming Script <pair: file naming; scripts>`
---------------------------------------------------------

There is only one file naming script defined in a user’s settings, although it can vary from a simple
one-line script such as ``%album%/%title%`` to a very complex script using different file naming formats
based on different criteria. In all cases, the files will be saved using the text output by the script.

.. note::

   Any new tags set or tags modified by the file naming script will not be written to the output
   files' metadata.

:index:`Tagging Scripts <pair: tagging; scripts>`
--------------------------------------------------

There can be multiple tagging scripts defined in a user’s settings. Individual scripts can be enabled or
disabled, and the order of execution of the scripts can be set. Whenever a script is run automatically (i.e.:
when an album is loaded), it is processed once for each track in the album that triggered the
run. For example, if there are two tagging scripts enabled (A and B) and an album with three tracks is
loaded, the scripts will be processed in the following order:

1. Script A Track 1;
2. Script A Track 2;
3. Script A Track 3;
4. Script B Track 1;
5. Script B Track 2;
6. Script B Track 3.

Metadata updates are not shared between tracks, so you cannot append data from one track to a tag in another
track.

Any new tags set or tags modified by the tagging scripts will be written to the output files' metadata,
unless the tag name begins with an underscore. These "hidden" tags are typically used as variables to hold
temporary values that are used later in either the tagging or file naming scripts. Tagging scripts are run
once for each track in the data, using the metadata for that track.

Tagging scripts can also be run manually by right-clicking either an album or a track in the right-hand pane
in Picard. If run from the album entry, the script is run for each track in the album. If run from an
individual track, the script is only run for that track.


Tagging Script Examples
-----------------------

The following scripting examples show how tagger scripts can be used to solve some specific use cases.
Please refer to :doc:`Picard scripting language <scripting>` for a detailed description of the variables and
functions used in these examples.


Move disambiguation to album title
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Append the disambiguation comment of a release to the album title:

.. code-block:: taggerscript

   $set(album,%album%$if(%_releasecomment%, \(%_releasecomment%\)))


Release language as language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``%_releaselanguage%`` variable specifies the language of the track listing, whereas the
``%language%`` variable is supposed to be the lyrics language.  The following script will use the
``%_releaselanguage%`` instead if ``%language%`` is empty:

.. code-block:: taggerscript

   $if($not(%language%),$set(language,%_releaselanguage%))


Use original release date
^^^^^^^^^^^^^^^^^^^^^^^^^

By default Picard provides a tag ``date`` which holds the release date of a specific release and
``originaldate`` which provides the earliest release date of this release.  For example you might have
a 2020 reissue of an album that originally was released in 1992.  In this case ``date`` will be set
to "2020" and ``originaldate`` to "1992".  If you prefer to have always the original release date
as the primary date in your file's tags you could use the following script:

.. code-block:: taggerscript

   $set(date,$if2(%originaldate%,%date%))

The use of :ref:`func_if2` ensures that if ``originaldate`` is empty it will fall back to ``date``.

In addition Picard provides a variable ``%_recording_firstreleasedate%``, which tries to provide
the first release date per recording (which can be different for each track in a release).
If you prefer this you can use the following script:

.. code-block:: taggerscript

   $set(date,$if2(%_recording_firstreleasedate%,%originaldate%,%date%))

Or if you want to keep the ``date`` for the actual release date of the specific release, but use
the recording's first release date as ``originaldate``:

.. code-block:: taggerscript

   $set(originaldate,$if2(%_recording_firstreleasedate%,%originaldate%))


Set album sort name
^^^^^^^^^^^^^^^^^^^

The ``albumsort`` tag is not filled by Picard by default.  You can set it to a meaningful value
with prefixes "The" and "A" moved to the end with the following script:

.. code-block:: taggerscript

   $set(albumsort,$swapprefix(%album%))

This will e.g. set the sort name for the release "The Best of Muddy Waters" to "Best of Muddy Waters, The".


Set compilation for multi artist releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default the ``compilation`` tag will be set to 1 only for Various Artists releases.  The following script will
set it for all releases with more than one artist (as it was default behavior in Picard 1.2 and earlier):

.. code-block:: taggerscript

   $if(%_multiartist%,$set(compilation,1))


Remove featuring from album artist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This always removes featuring artists from the album artist:

.. code-block:: taggerscript

   $set(albumartist,$rreplace(%albumartist%,\\s+feat\\..*,))


Move featuring from artist to title
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

According to MusicBrainz guidelines featuring artists are part of the artist name, e.g.
"Artist A feat. Artist B".  Some users prefer to have featuring added to the album or track title
instead.  The following script moves featured track artists to the track title:

.. code-block:: taggerscript

   $set(_feat_title,$rsearch(%artist%,\\s+\\\(?\(f\(ea\)?t\\.[^\)]*\)))
   $set(artist,$rreplace(%artist%,\\s+\\\(?f\(ea\)?t\\.[^\)]*\\\)?,))
   $set(title,$if(%_feat_title%,%title% \(%_feat_title%\),%title%))

The same can be done for moving featured artists from the album artist to the album title:

.. code-block:: taggerscript

   $set(_feat_album,$rsearch(%albumartist%,\\s+\\\(?\(f\(ea\)?t\\.[^\)]*\)))
   $set(albumartist,$rreplace(%albumartist%,\\s+\\\(?f\(ea\)?t\\.[^\)]*\\\)?,))
   $set(album,$if(%_feat_album%,%album% \(%_feat_album%\),%album%))


Preserve original filename
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``originalfilename`` tag is supposed to hold the filename the file originally had.  By default
Picard does not set or modify this tag.  If you want to save this information the following Script
can be used:

.. code-block:: taggerscript

   $set(originalfilename,$if2(%originalfilename%,%_filename%.%_extension%))

This will keep any existing ``originalfilename`` tag.  But if this tag is not yet present
the tag will be set to the current filename.  As this happens before the file is being saved
the original name of the file before Picard modifies it can be preserved.

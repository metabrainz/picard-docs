..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

.. index::
   single: troubleshooting; files not saved

Files are not being saved
=========================

There are two typical scenarios where files are not being saved:

**After selecting files in the right-hand pane you see a red stop like icon**

    This indicates an error occurred during saving. In the majority of times people see this it is because the files they
    want to save are write protected (either have the readonly flag set or have wrong permissions).  Check that the files
    are not write protected and that you have the appropriate permissions before trying again.

    Permission problems seem to be more common when Picard has been installed using Flatpak, or when the files are being read
    from or written to a samba share on the network.

    Another possibility is that the total length of the destination path and file name exceeds the maximum length allowed by
    the operating system.  If you have an extremely long path and file name, try shortening it to see it it allows the file
    to be saved.

**In the right-hand pane you see just a musical note icon in front of the tracks**

    That means that this is just the track data from MusicBrainz, but no file has been associated with it. In that case the
    save button is disabled.  Check to make sure that the files are properly matched to the tracks before trying to save
    again.  Please see the :doc:`../usage/match` and :doc:`../usage/save` sections for more information.

A third possibility, although very rare, is that you are trying to set a tag with an invalid key.  If the two solutions above
don't resolve your problem, try reviewing all of the tags to be written to see if there are any that don't appear to be valid.

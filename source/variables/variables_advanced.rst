..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Advanced Variables
==================

If you enable tagging with :ref:`Advanced Relationships <advanced_relationships>`, you get these extra variables:

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

**_performance_attributes**

    List of performance attributes for the work (e.g.: "live", "cover", "medley"). Use ``$inmulti`` to check for
    a specific type (i.e.: ``$if($inmulti(%_performance_attributes%,medley), (Medley),)``). (*since Picard 1.3*)

**_recordingcomment**

    Recording disambiguation comment. (*since Picard 0.15*)

**_recordingtitle**

    Recording title - normally the same as the Track title, but can be different.

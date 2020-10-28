.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0

.. TODO: Expand definitions

.. TODO: Note which tags are not provided by Picard

Advanced Variables
==================

.. index::
   single: variables; advanced

If you enable tagging with :ref:`Advanced Relationships <advanced_relationships>`, you get these extra variables:

.. note::

   Variables will not be created if there was no value retrieved for the variable from the MusicBrainz database.

**_performance_attributes**

    List of performance attributes for the work (e.g.: "live", "cover", "medley"). Use ``$inmulti`` to check for
    a specific type (i.e.: ``$if($inmulti(%_performance_attributes%,medley), (Medley),)``) (*since Picard 1.3*).

**_recordingcomment**

    Recording disambiguation comment (*since Picard 0.15*).

**_recordingtitle**

    Recording title - normally the same as the Track title, but can be different.

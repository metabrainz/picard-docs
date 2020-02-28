..  Picard Scripting Variables

Advanced Variables
==================

If you enable tagging with Advanced Relationships, you get these extra variables:

**_performance_attributes**

    List of performance attributes for the work e.g. "live", "cover", "medley" etc. Use ``$inmulti`` to check for a specific type, i.e. ``$if($inmulti(%_performance_attributes%,medley), (Medley),)`` (since Picard 1.3)

**_recordingcomment**

    Recording disambiguation comment (since Picard 0.15)

**_recordingtitle**

    Recording title - normally the same as the Track title, but can be different.

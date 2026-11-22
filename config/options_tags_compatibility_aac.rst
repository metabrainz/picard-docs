.. MusicBrainz Picard Documentation Project

:index:`AAC Files <configuration; aac tag options>`
===================================================

Picard can save APEv2 tags to pure AAC files, which by default do not support tagging. APEv2 tags in AAC are supported by some players, but players not supporting AAC files with APEv2 tags can have issues loading and playing those files. To deal with this you can choose whether to save tags to those files.

.. only:: not latex

   .. image:: images/options-tags-compatibility-aac.png
      :align: center

.. only:: latex

   .. image:: images/options-tags-compatibility-aac.png
      :width: 70%
      :align: center

.. _opt_tags_compatibility_aac_save_apev2_tags:

**Save APEv2 tags**

   Picard will save APEv2 tags to the files.

.. _opt_tags_compatibility_aac_do_not_save_tags:

**Do not save tags**

   Picard will not save any tags to the files, but you can still use Picard to rename them. By default existing APEv2 tags will be kept in the file.

.. _opt_tags_compatibility_aac_remove_apev2_tags:

**Remove APEv2 tags**

   If you have "Do not save tags" enabled checking this option will cause Picard to remove existing APEv2 tags from the file on saving.

Regardless of how you have configured saving tags Picard will always read existing APEv2 tags in AAC files.

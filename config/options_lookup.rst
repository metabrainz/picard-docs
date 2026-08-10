.. MusicBrainz Picard Documentation Project

:index:`Lookup Options <configuration; lookup options>`
=========================================================

.. only:: not latex

   .. image:: images/options-lookup.png
      :align: center

.. only:: latex

   .. image:: images/options-lookup.png
      :width: 70%
      :align: center

**Automatically scan all new files**

   Check this box if you want Picard to scan each music file you add and look for an :index:`AcoustID <pair: AcoustID; automatic scan>` fingerprint. This takes time, but may be helpful for you and MusicBrainz. Leave it unchecked if you don't want Picard to do this scan automatically. In any case, you can direct Picard to scan a particular music file at any time using :menuselection:`"Tools --> Scan"`. See also :ref:`Scan Files <ref_scan_files>` and :ref:`ref_tutorial_acoustid`.

**Automatically cluster all new files**

   Check this box if you want Picard to automatically group all loaded files into album :index:`clusters <pair: cluster; automatic clustering>`. Leave it unchecked if you don't want Picard to do this automatically. In any case, you can direct Picard to cluster files any time using :menuselection:`"Tools --> Cluster"`. See also :ref:`Lookup Files <ref_lookup_files>`.

.. note::

   You can either enable "Automatically scan all new files" or "Automatically cluster all new files", but not both.

**Ignore MBIDs when loading new files**

   If you enable this option Picard will not use MusicBrainz identifiers (MBIDs) stored in the files to automatically load the corresponding MusicBrainz release and match the loaded file to the correct track. Leaving this option disabled is useful when re-processing files that have been previously tagged with incorrect information.

**Maximum number of entities to return per MusicBrainz query**

   This sets the maximum number of results returned for queries made to the MusicBrainz website. The default value is 50 results. On Picard v2.8.1 and earlier, this value was fixed at a maximum of 25 responses.

**Use builtin search rather than looking in browser**

   If you enable this option, Picard will use its own search system rather than using the browser for searching the MusicBrainz database.

**Use advanced query syntax**

   When this option is enabled, searches will be performed using the advanced query syntax rather than the simple query syntax.


.. toctree::
   :hidden:

   options_cdlookup
   options_fingerprinting

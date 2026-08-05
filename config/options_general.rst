.. MusicBrainz Picard Documentation Project

:index:`General Options <configuration; general options>`
=========================================================

.. only:: not latex

   .. image:: images/options-general.png
      :align: center

.. only:: latex

   .. image:: images/options-general.png
      :width: 70%
      :align: center

**Server address**

   The domain name for the MusicBrainz database server used by Picard to get details of your music. Default value: musicbrainz.org (for the main MusicBrainz server).

   In addition to the standard MusicBrainz servers provided in the drop down list, you can manually enter an alternate address, such as "localhost" if you are running a local copy of the server. When an alternate server host name is entered, a warning will be displayed and you will be asked to confirm that you want to submit all data to this alternate server.

   .. only:: not latex

      .. image:: images/options-alternate-server-confirmation.png
         :align: center

   .. only:: latex

      .. image:: images/options-alternate-server-confirmation.png
         :width: 70%
         :align: center

**Port**

   The port number for the server. Default value: 443 (for the main MusicBrainz server).

**Username**

   Your MusicBrainz website username, used to submit acoustic fingerprints, retrieve and save items to your collections, and retrieve personal folksonomy tags.

**Password**

   Your MusicBrainz website password.

**Automatically scan all new files**

   Check this box if you want Picard to scan each music file you add and look for an :index:`AcoustID <pair: AcoustID; automatic scan>` fingerprint. This takes time, but may be helpful for you and MusicBrainz. Leave it unchecked if you don't want Picard to do this scan automatically. In any case, you can direct Picard to scan a particular music file at any time using :menuselection:`"Tools --> Scan"`. See also :ref:`Scan Files <ref_scan_files>` and :ref:`ref_tutorial_acoustid`.

**Automatically cluster all new files**

   Check this box if you want Picard to automatically group all loaded files into album :index:`clusters <pair: cluster; automatic clustering>`. Leave it unchecked if you don't want Picard to do this automatically. In any case, you can direct Picard to cluster files any time using :menuselection:`"Tools --> Cluster"`. See also :ref:`Lookup Files <ref_lookup_files>`.

.. note::

   You can either enable "Automatically scan all new files" or "Automatically cluster all new files", but not both.

**Ignore MBIDs when loading new files**

   If you enable this option Picard will not use MusicBrainz identifiers (MBIDs) stored in the files to automatically load the corresponding MusicBrainz release and match the loaded file to the correct track. Leaving this option disabled is useful when re-processing files that have been previously tagged with incorrect information.

**Remove complete albums after saving**

   With this option enabled, Picard will remove complete albums from the Album pane after they have been saved. This can help reduce clutter in the user interface, especially when working with large collections. If you disable this option, albums will remain in the Album pane after saving, and you will need to remove them manually.

   Albums will be removed only after files have been matched to all tracks on the album, and all files in the album have been saved.

.. only:: html and not epub

   .. seealso::

      Please see :doc:`options_startup` for options related to checking for updates and log level at startup.

.. toctree::
   :hidden:

   options_startup

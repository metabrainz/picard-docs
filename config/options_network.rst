.. MusicBrainz Picard Documentation Project

:index:`Network <configuration; network>`
=========================================

These settings allow you to configure the network settings used by Picard.

.. only:: not latex

   .. image:: images/options-network.png
      :align: center

.. only:: latex

   .. image:: images/options-network.png
      :width: 75%
      :align: center

**Web Proxy**

   If you need a proxy to make an outside network connection you may specify one here. You can choose between HTTP and SOCKS proxy. The required settings are **Server Address** and **Port**. If the proxy requires authentication also enter **Username** and **Password**.

**Request timeout in seconds**

   By default Picard will abort running network requests after 30 seconds of inactivity. If needed you can change the timeout period here.

.. |lookup_tagger| image:: images/mblookup-tagger.png
   :height: 1em

**Browser Integration**

   The browser integration allows you to load releases and recordings into Picard directly from the MusicBrainz website. Once you have opened musicbrainz.org in your browser from Picard, the website will show the green tagger button |lookup_tagger| next to releases and recordings. Clicking on this button will load the corresponding release or recording into Picard.

**Default listening port**

   This identifies the default port Picard will listen on for the browser integration. If the port is not available Picard will try to increase the port number by one until it finds a free port.

**Listen only on localhost**

   By default Picard will limit access to the browser integration port to your local machine. Deactivating this option will expose the port on your network, allowing you to request Picard to load a specific release or recording via the network. For example, this would be used for the `Picard Barcode Scanner <https://play.google.com/store/apps/details?id=org.musicbrainz.picard.barcodescanner>`_ Android app.

   .. warning::

      Only expose the port externally when you actually need it and only on networks you trust. Exposing application ports via the network can open potential security holes on your system.

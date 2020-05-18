..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Network
=======

.. image:: ../images/options-network.png
   :width: 100 %

**Web Proxy**

    If you need a proxy to make an outside network connection you may specify one here.  The required
    settings are **Server Address**, **Port**, **Username** and **Password**.

.. |lookup_tagger| image:: ../images/mblookup-tagger.png
   :height: 1em

**Browser Integration**

    The browser integration allows you to load releases and recordings into Picard directly from the
    MusicBrainz website. Once you have opened musicbrainz.org in your browser from Picard, the website
    will show the green tagger button |lookup_tagger| next to releases and recordings.  Clicking on
    this button will load the corresponding release or recording into Picard.

**Default listening port**

    This identifies the default port Picard will listen on for the browser integration. If the port
    is not available Picard will try to increase the port number by one until it finds a free port.

**Listen only on localhost**

    By default Picard will limit access to the browser integration port to your local machine.
    Deactivating this option will expose the port on your network, allowing you to request Picard to
    load a specific release or recording via the network. For example, this would be used for the
    `Picard Barcode Scanner <https://play.google.com/store/apps/details?id=org.musicbrainz.picard.barcodescanner>`_
    Android app.

    .. warning::

        Only expose the port externally when you actually need it and only on networks you trust.
        Exposing application ports via the network can open potential security holes on your system.

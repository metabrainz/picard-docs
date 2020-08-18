.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


I am using Fedora. Why doesn't acoustic fingerprinting work?
======================================================================

.. index::
   single: acoustic fingerprint
   single: fingerprint; acoustic

Acoustic fingerprinting in Picard uses a tool called ``fpcalc``, which is not available in Fedora. You can get it by installing the chromaprint-toolspackage
from the `RPM Fusion repository <https://rpmfusion.org/>`_. This functionality is not contained in the main Fedora ``picard`` package because it requires
the ``ffmpeg`` package which `cannot be distributed by Fedora <https://fedoraproject.org/wiki/Forbidden_items>`_. After `enabling the "rpmfusion-free" RPM
Fusion repository <https://rpmfusion.org/Configuration>`_, install the package using (as root)::

   yum install chromaprint-tools

.. MusicBrainz Picard Documentation Project
.. Prepared in 2020 by Bob Swift (bswift@rsds.ca)
.. This MusicBrainz Picard User Guide is licensed under CC0 1.0
.. A copy of the license is available at https://creativecommons.org/publicdomain/zero/1.0


Status Icons
============

.. index::
   single: icons; status

When albums and tracks are displayed in the right-hand pane, each line begins with an icon
to indicate the status of the item.

.. index::
   single: icons; album
   single: icons; release

Album / Release Icons
---------------------

.. |img-release| image:: ../images/release.png
   :width: 24pt
   :height: 24pt

|img-release|

   | This icon indicates that the information for the release has been successfully retrieved from the MusicBrainz database.  Some, but not all, tracks may have been matched to files and the information has not been modified.
   |

.. |img-release-modified| image:: ../images/release-modified.png
   :width: 24pt
   :height: 24pt

|img-release-modified|

   | This icon indicates that some of the tracks have been matched and that the information for the release has been modified.
   |

.. |img-release-matched| image:: ../images/release-matched.png
   :width: 24pt
   :height: 24pt

|img-release-matched|

   | This icon indicates that all of the tracks have been matched and that the information has not been modified.
   |

.. |img-release-matched-modified| image:: ../images/release-matched-modified.png
   :width: 24pt
   :height: 24pt

|img-release-matched-modified|

   | This icon indicates that all of the tracks have been matched and that the information for the release has been modified.
   |

.. |img-release-error| image:: ../images/release-error.png
   :width: 24pt
   :height: 24pt

|img-release-error|

   | This icon indicates that Picard has encountered an error with the release, typically while retrieving the information from the MusicBrainz database.
   |


.. index::
   single: icons; track

Track Icons
-----------

.. |img-track-audio| image:: ../images/track-audio.png
   :width: 24pt
   :height: 24pt

|img-track-audio|

   | This icon indicates that the track is an audio track and that there is no file currently matched.
   |

.. |img-track-video| image:: ../images/track-video.png
   :width: 24pt
   :height: 24pt

|img-track-video|

   | This icon indicates that the track is a video track and that there is no file currently matched.
   |

.. |img-track-data| image:: ../images/track-data.png
   :width: 24pt
   :height: 24pt

|img-track-data|

   | This icon indicates that the track is a data track and that there is no file currently matched.
   |

.. |img-match-50| image:: ../images/track-match-50.png
   :width: 24pt
   :height: 24pt

.. |img-match-60| image:: ../images/track-match-60.png
   :width: 24pt
   :height: 24pt

.. |img-match-70| image:: ../images/track-match-70.png
   :width: 24pt
   :height: 24pt

.. |img-match-80| image:: ../images/track-match-80.png
   :width: 24pt
   :height: 24pt

.. |img-match-90| image:: ../images/track-match-90.png
   :width: 24pt
   :height: 24pt

.. |img-match-100| image:: ../images/track-match-100.png
   :width: 24pt
   :height: 24pt

|img-match-50| |img-match-60| |img-match-70| |img-match-80| |img-match-90| |img-match-100|

   | These icons indicates the quality of match between the information from the file and the information for the track as provided from the MusicBrainz database.  Red indicates a poor match, progressing to all green which indicates a very good match.
   |

.. |img-track-saved| image:: ../images/track-saved.png
   :width: 24pt
   :height: 24pt

|img-track-saved|

   | This icon indicates that the track has been saved successfully.
   |

.. |img-track-error| image:: ../images/track-error.png
   :width: 24pt
   :height: 24pt

|img-track-error|

   This icon indicates that Picard encountered an error while trying to save the track.  This is typically due to the file being marked as read-only, or you do not have sufficient permission to save the file in the specified directory.


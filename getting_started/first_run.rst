.. MusicBrainz Picard Documentation Project

:index:`First Run Wizard <wizard; first run>`
======================================================

Starting with version 3.0, Picard includes a "First Run Wizard" that is displayed the first time Picard is run after installation. The wizard allows the user to configure some basic settings and to choose whether to enable or disable certain features. These settings can be changed later in the Options dialog, but the wizard provides a convenient way to configure some basic settings when Picard is first run.


Initial Warning
----------------

The first screen displays a warning that Picard is a powerful tool that can modify your music files.

.. only:: not latex

   .. image:: images/initial_warning.png
      :align: center

   |

.. only:: latex

   .. image:: images/initial_warning.png
      :align: center
      :width: 75%

This screen provides some recommendations, including a link to the on-line documentation. There is an option to display this warning again, each time Picard is started.


Setup Wizard
-------------

Once the initial warning screen is acknowledged, the setup wizard is displayed the first time Picard is started. This wizard allows the user to configure some basic settings and to choose whether to enable or disable certain features.

.. only:: not latex

   .. image:: images/first_run_wizard_1.png
      :align: center

   |

.. only:: latex

   .. image:: images/first_run_wizard_1.png
      :align: center
      :width: 75%

This initial setup wizard screen also provides a link to the documentation.


Setup Wizard - File Organization
+++++++++++++++++++++++++++++++++

This is the first setting screen of the setup wizard, which allows the user to configure how Picard will organize music files.

.. only:: not latex

   .. image:: images/first_run_wizard_2.png
      :align: center

   |

.. only:: latex

   .. image:: images/first_run_wizard_2.png
      :align: center
      :width: 75%

This screen allows the user to choose whether tagged files should be renamed based upon the metadata tags in the files, and whether the files should be moved to a different location. The file location folder structure is determined using a :doc:`file naming script <../extending/scripts>`, and the user can specify the main directory under which the folder structure is created.


Setup Wizard - Cover Art
+++++++++++++++++++++++++

The next screen of the setup wizard allows the user to configure how Picard should handle cover art.

.. only:: not latex

   .. image:: images/first_run_wizard_3.png
      :align: center

   |

.. only:: latex

   .. image:: images/first_run_wizard_3.png
      :align: center
      :width: 75%

This screen allows the user to choose whether tagged files should have cover art images embedded in the audio files, and if the cover art image files should be saved in the folder with the audio files.

It also allows the user to choose if release group cover art is used instead of cover art for the specific release. Release group cover art usually provides higher quality images, but they may not exactly match the cover for your specific release.


Setup Wizard - Updates
+++++++++++++++++++++++

The final screen of the setup wizard allows the user to configure how Picard should handle checking for updates.

.. only:: not latex

   .. image:: images/first_run_wizard_4.png
      :align: center

   |

.. only:: latex

   .. image:: images/first_run_wizard_4.png
      :align: center
      :width: 75%

Picard can be configured to automatically check for the following updates:

- New versions of Picard. Note that this option will not be available if Picard was installed from a package manager, as the package manager will handle updates.
- New versions of installed plugins.
- New versions of the documentation, including available translations of the documentation. Picard will automatically try to display the appropriate version of the documentation in the user's preferred language, if a translation is available. If a translation is not available, Picard will display the documentation in English.

.. note::

   The update checks will only be performed if the computer is connected to the Internet. The update checks for new versions of the program and installed plugins will provide notifications when updates are available, but will **not** automatically download and install them.

.. raw:: latex

   \clearpage

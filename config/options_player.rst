.. MusicBrainz Picard Documentation Project

:index:`Audio Player Options <triple: configuration; audio player; listenbrainz>`
=================================================================================

.. only:: not latex

   .. image:: images/options-player.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-player.png
      :width: 75%
      :align: center

.. _opt_player_enable_audio_player_now_playing_notifications:

**Enable audio player "now playing" notifications**

    When enabled, Picard will send "now playing" notifications from the internal audio player. The availability of this option depends on the operating system. Currently this is available for macOS and on Linux.

.. _opt_player_submit_listens_to_listenbrainz:

**Submit listens to ListenBrainz**

    When enabled, Picard will submit listened tracks to your `ListenBrainz <https://listenbrainz.org>`_ profile.

.. _opt_player_submit_only_tagged_files:

**Submit only tagged files**

    When enabled, Picard will only submit tracks that have been tagged with MusicBrainz metadata. This option is enabled by default, as untagged files often have missing or incorrect metadata.

.. _opt_player_listenbrainz_user_token:

**ListenBrainz user token**

    Enter your ListenBrainz user token here to enable listen submission to your profile. You can find your token on your
    `ListenBrainz settings page <https://listenbrainz.org/settings/>`_.

.. note::

    The Audio Player options are only available if the built-in audio player is available. The player can be unavailable if the system is missing the required Qt Multimedia libraries. It can also be disabled with the ``--no-player`` command line option.

.. seealso::

    :doc:`../appendices/command_line`

.. MusicBrainz Picard Documentation Project

.. Master File for Building HTML Documents

:orphan:

.. only:: html and not latex

   MusicBrainz Picard
   ==================

   **User Guide for MusicBrainz Picard, the next generation tagger.**

   MusicBrainz Picard is a cross-platform music file tagger. This User Guide is intended to augment the information provided on the `Picard website <https://picard.musicbrainz.org/>`_ and to provide an alternate format for the documentation, including a PDF document suitable for printing. Links to additional information such as scripts, plugins and tutorials are provided when available rather than trying to reproduce the information in this document.

   .. include:: copyright_notice.txt

.. only:: html and not epub and not latex

   .. toctree::
      :caption: About Picard
      :hidden:

      about_picard/introduction
      about_picard/contributing
      about_picard/acknowledgements
      about_picard/glossary


   .. toctree::
      :caption: Getting Started
      :titlesonly:
      :hidden:

      getting_started/download
      getting_started/starting
      getting_started/screen_main
      getting_started/status_icons
      config/configuration
      variables/variables
      extending/scripting
      functions/list_by_type

   .. toctree::
      :caption: Using Picard
      :hidden:

      General Usage <usage/using>
      usage/other
      usage/option_profiles
      usage/command_processing
      extending/extending
      faq/faq


   .. toctree::
      :caption: Workflow Recommendations
      :hidden:

      General Recommendations <workflows/workflows>
      workflows/workflow_cd
      workflows/workflow_extractor_log
      workflows/workflow_album
      workflows/workflow_metadata
      workflows/workflow_no_info


   .. toctree::
      :caption: Troubleshooting
      :hidden:

      troubleshooting/troubleshooting
      troubleshooting/does_not_start
      troubleshooting/no_coverart
      troubleshooting/missing_tags
      troubleshooting/not_saving
      troubleshooting/stopped_working
      troubleshooting/macos_startup_error


   .. toctree::
      :caption: Tutorials
      :hidden:
      :maxdepth: 0
      :titlesonly:

      tutorials/naming_script
      tutorials/acoustid
      tutorials/multiple_release_countries
      tutorials/write_plugin


   .. toctree::
      :caption: Video Tutorials
      :hidden:
      :maxdepth: 0
      :titlesonly:

      tutorials/v_introduction
      tutorials/v_attach_disc_id
      tutorials/v_submit_acoustid


   .. toctree::
      :caption: Appendices
      :hidden:
      :maxdepth: 0
      :titlesonly:

      appendices/plugins_api
      appendices/tag_mapping
      appendices/command_line
      appendices/keyboard_shortcuts
      functions/list_by_name

.. MusicBrainz Picard Documentation Project

:index:`Preferred Releases <configuration; release preferences>`
================================================================

These settings allow you to configure Picard to prefer certain types of releases, countries, and formats when matching files or clusters to releases. In each case, you can add one or more values to the list of preferred values, and Picard will prioritize matching to releases with those values. You can set the relative matching priority of the values by adjusting their order in the list. The higher a value is in the list, the more likely Picard will be to match releases with that value.

**Preferred Release Types**

   This setting allows you to configure the preferred release types to use. The top section sets the release types to prefer, while the bottom section sets the release types to avoid. The release types are listed in order of preference, with the most preferred release type at the top of the list. The types to avoid are not listed in any particular order because they are all treated equally.

   Types not specifically listed in either section are treated as neutral, and will be considered only after the preferred types and before the avoided types. This allows you to configure Picard to prefer certain release types, while avoiding others, without having to list every possible release type.

   .. only:: not latex

      .. image:: images/options-metadata-releases-types.png
         :align: center

   .. only:: latex

      .. image:: images/options-metadata-releases-types.png
         :width: 70%
         :align: center

   For example, you can use this to decrease the likelihood of Picard matching a file or album to a Compilation or Live version.

**Preferred Release Countries**

   This setting allows you to configure the preferred release countries to use when matching files or clusters to releases. The release countries are listed in order of preference, with the most preferred release country at the top of the list. This list is also used to prioritize files in the "Other Releases" context menu.

   Countries not specifically listed are treated as neutral, and will be considered only after the preferred countries. This allows you to configure Picard to prefer certain release countries without having to list every possible country.

   .. only:: not latex

      .. image:: images/options-metadata-releases-countries.png
         :align: center

   .. only:: latex

      .. image:: images/options-metadata-releases-countries.png
         :width: 70%
         :align: center

**Preferred Medium Formats**

   This setting allows you to configure the preferred medium formats to use when matching files or clusters to releases. The medium formats are listed in order of preference, with the most preferred format at the top of the list. This list is also used to prioritize files in the "Other Releases" context menu.

   Formats not specifically listed are treated as neutral, and will be considered only after the preferred formats. This allows you to configure Picard to prefer certain medium formats without having to list every possible format.

   .. only:: not latex

      .. image:: images/options-metadata-releases-formats.png
         :align: center

   .. only:: latex

      .. image:: images/options-metadata-releases-formats.png
         :width: 70%
         :align: center

.. MusicBrainz Picard Documentation Project

:index:`Plugins Options <pair: configuration; plugins>`
=======================================================

This section allows you to manage the plugins used by Picard. You can install new plugins or enable, disable or uninstall plugins that are currently installed. Picard provides a list of plugins that have been submitted to the project. A list of the standard plugins is available on the `plugins page <https://picard.musicbrainz.org/plugins/>`_ on the Picard website. You are also presented with a list of the registered plugins when you choose to install a plugin.

.. only:: not latex

   .. image:: images/options-plugins.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins.png
      :width: 80%
      :align: center

The screen is divided into three sections. The top section includes the general plugin management action buttons, the middle section is the list of currently installed plugins, and the bottom section displays a brief log of the most recent plugin management actions executed.

.. note::

   When a plugin is installed, uninstalled, enabled or disabled, the action is processed immediately. These actions are not impacted by clicking either the  :guilabel:`Make It So!` or :guilabel:`Cancel` buttons. For example, clicking :guilabel:`Cancel` will not undo the action, and clicking :guilabel:`Restore Defaults` or :guilabel:`Restore all Defaults` will not make any changes to the status of the plugins.

   When a new plugin is installed, it is automatically set as enabled.


Plugin Management
-----------------

The general plugin management actions are :guilabel:`Install Plugin...` and :guilabel:`Refresh All`. In addition, there is a "Search plugins..." box that allows you to filter the list of plugins displayed in the plugin list.


Installing a Plugin
+++++++++++++++++++

When the :guilabel:`Install Plugin...` button is clicked, a new dialog window will open to allow selecting the plugin to install. There are three tabs, which allow you to select the plugin from: the official plugin registry; a URL pointing to a third-party plugin; or a plugin on a local drive.

Installing from the registry
''''''''''''''''''''''''''''

When installing a plugin from the official plugin registry, you are presented with a list of available plugins not already installed from which to select. The list can be filtered by selecting a category or entering search text. Search text will be applied to the plugin name or description. Hovering your mouse pointer over a plugin will display a brief description of the plugin, and double-clicking a plugin will display additional information such as the plugin author, trust level, and a link to the plugin repository.

Each plugin in the official registry is assigned a trust level from:

* **official** 🛡️ - Maintained by the MusicBrainz Picard team
* **trusted** ✓ - Well-known authors with an established reputation
* **community** ⚠️ - Other plugins (This is the default for new submissions)

.. only:: not latex

   .. image:: images/options-plugins-install-registry.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-install-registry.png
      :width: 60%
      :align: center

Once you have selected a plugin and click :guilabel:`Install...`, you are asked to confirm the installation, and are able to select the version of the plugin to install. This can be a specific version number (tag), a branch such as "main" or "development" (if available), or a particular commit to the repository.

Installing from a URL
'''''''''''''''''''''

Sometimes plugin authors choose not to include one or more of their plugins in the official plugin registry. You can still install these plugins by providing the URL of the plugin repository to the installation dialog. The URL can usually be obtained directly from the plugin author, from a discussion on the `MetaBrainz Community Forum <https://community.metabrainz.org>`_, from a user-maintained list in a blog or wiki, or by searching a Git repository provider such as GitHub. The MusicBrainz Picard team recommends that plugin repository names on GitHub (and other providers) begin with ``picard-plugin-`` to help with their discovery when searching those platforms.

.. only:: not latex

   .. image:: images/options-plugins-install-url.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-install-url.png
      :width: 60%
      :align: center

When installing a plugin from a URL, you must enter the URL to the repository of the plugin, and optionally the version of the plugin to install. The version can be a specific version number (tag), a branch such as "main" or "development" (if available), or a particular commit to the repository. If no verion is specified, you can select it from the confirmation dialog displayed.

.. warning::

   Be careful when installing plugins from unknown sources, as plugins may pose security risks. Only install plugins from sources you trust.

Installing from a local repository
''''''''''''''''''''''''''''''''''

You can also install a plugin from a local repository. This would typically be the case while testing a plugin during development.

.. only:: not latex

   .. image:: images/options-plugins-install-local.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-install-local.png
      :width: 60%
      :align: center

When installing a plugin from a local repository, you must enter the path to the repository of the plugin, and optionally the version of the plugin to install. The version can be a specific version number (tag), a branch such as "main" or "development" (if available), or a particular commit to the repository. If no verion is specified, you can select it from the confirmation dialog displayed.


Checking for Updates
++++++++++++++++++++

You can refresh the registry and check for updates to installed plugins by clicking the :guilabel:`Refresh All` button. If an update is found for an installed plugin it will be identified in the plugins list.

.. only:: not latex

   .. image:: images/options-plugins-updates.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-updates.png
      :width: 75%
      :align: center

You can select which updates to apply and click the :guilabel:`Update All` button to perform the updates.


Plugins List
------------

The enabled status of a plugin can be toggled by using the check box to the left of the plugin name.

When a plugin in the list is selected, some details are displayed in a side panel for the selected plugin.

.. only:: not latex

   .. image:: images/options-plugins-details.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-details.png
      :width: 75%
      :align: center

The display of this panel can be toggled using the :guilabel:`Show Details` / :guilabel:`Hide Details` button.

From the details panel you have the option to update the plugin (if an update is found to be available by using the :guilabel:`Refresh All` button) or uninstalling the plugin.

If you right-click on a plugin in the list, a context menu will be displayed.

.. only:: not latex

   .. image:: images/options-plugins-context-menu.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-context-menu.png
      :width: 75%
      :align: center

From this menu, you can toggle the enabled status of the plugin, uninstall, reinstall or change the installed version (reference), view detailed information, open the plugin repository in your browser, or :doc:`manually set the order in which the plugins are executed <options_plugin_execution_order>`. The detailed information includes additional items such as the license, the link to the homepage for the plugin if available, and the directory that the plugin resides on your file system.

.. only:: not latex

   .. image:: images/options-plugins-information.png
      :align: center

   |

.. only:: latex

   .. image:: images/options-plugins-information.png
      :width: 75%
      :align: center

.. note::

   Some plugins have their own option page which will typically appear under the "Plugins" section of the Options.

.. only:: html and not epub

   .. seealso::

      Please see the :doc:`options_plugin_execution_order` section for more information about manually setting the order in which plugins are executed.

.. toctree::
   :hidden:

   options_plugin_execution_order

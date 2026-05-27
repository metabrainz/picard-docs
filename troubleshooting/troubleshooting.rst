.. MusicBrainz Picard Documentation Project

:index:`General Troubleshooting <troubleshooting; general>`
===========================================================

Getting Help
------------

If you have problems using Picard, please first check the following resources:

* For general usage information see the :doc:`../usage/using` documentation and the `illustrated quick start guide <https://picard.musicbrainz.org/quick-start/>`_.
* Read the :doc:`FAQ section <../faq/faq>` for common questions and problems.
* Consult the `community forums <https://community.metabrainz.org/c/picard>`_.
* Check the `download page <https://picard.musicbrainz.org/downloads/>`_ for a newer version of Picard which might solve your problem.
* If the problem is to do with a plugin, check the `Picard Plugins <https://picard.musicbrainz.org/plugins/>`_ for updated plugin versions.


:index:`Reporting a Bug <troubleshooting; reporting a bug>`
-----------------------------------------------------------

Plugin Issues
+++++++++++++

If you think you have found a bug in a plugin, you should first check whether you are using the latest version of the plugin. This can be done by going to the :menuselection:`"Options --> Plugins"` page and clicking the :guilabel:`Refresh All` button. If an update is found for any of your plugins, you can update them from the plugins options page. If there was no update available or you have updated the plugin and are still experiencing the problem, you should report the issue to the plugin author.

If the plugin author has provided a link to report issues, right-clicking the plugin will provide an option to "Report a Bug". If there is no such option available, you can find the contact information for the plugin author by right-clicking on the plugin in the list and selecting :guilabel:`Information` from the context menu. This will show you a link to the plugin homepage. When reporting the issue to the plugin author, please provide the following information:

* Which version of Picard do you use?
* Which version of the plugin do you use?
* Which operating system do you use?
* What did you do when the bug occurred?
* What actually happened, and what did you expect to happen?
* The **"Debug"** level log from the Picard session demonstrating the problem.

Picard Issues
+++++++++++++

If you think you have found a bug with Picard itself, please check whether you are using the latest version of Picard and whether the bug has already been reported in the `bug tracker <https://tickets.musicbrainz.org/browse/PICARD>`_. If you're not sure or don't want to look through the existing tickets, ask on the community forums first.

If you're still convinced you have found a new bug, open a `new ticket <https://tickets.musicbrainz.org/secure/CreateIssue.jspa?pid=10042&issuetype=1>`_ providing the following information:

* Which version of Picard do you use? ("Affects Version" in the form)
* Which operating system do you use? ("Environment" in the form)
* What did you do when the bug occurred?
* What actually happened, and what did you expect to happen?
* If you're using plugins, which plugins do you have enabled?
* The **"Debug"** level log from the Picard session demonstrating the problem.

.. warning::

   Please remember to first remove any personal and confidential information like user id, passwords or authorization tokens before posting or submitting any log output.


:index:`Getting a Debug Log <troubleshooting; get debug log>`
-------------------------------------------------------------

For many bugs, it helps developers to have a debug log from Picard. You can see the log by going to :menuselection:`Help --> View Error/Debug Log`. You can also get a full debug log, which is better because it contains more detailed information. Pasting this log into your forum post or bug ticket can help developers and other users to resolve your issue more quickly. To retrieve the full debug log:

1. Start Picard.
2. Open the log viewer by going to :menuselection:`Help --> View Error/Debug Log`.
3. Set the log level to **Debug** using the dropdown control at the bottom of the log viewer window. This will cause all log entries to be captured in the log, including detailed debug information that is not included at higher log levels.
4. Repeat the action that caused the problem being reported.
5. From the log viewer, copy the log output to paste into the forum post or bug ticket. Alternately, you can save the log to a file to attach to your bug report by using the :guilabel:`Save As…` button.
6. Close the log viewer, and close Picard.

Please see :doc:`../appendices/log_viewer` for more information about the log viewer and how to use it.


:index:`Getting Logs in Case of Crashes <troubleshooting; getting log for crashes>`
-----------------------------------------------------------------------------------

In some cases the problem will cause Picard to crash and not allow you to access the resulting log from the log viewer. You can still generate a log output to attach to your report by starting Picard with the ``--debug`` command line option from a command / terminal window (or set the ``PICARD_DEBUG`` environment variable) and copying the log output information from the terminal. The steps to follow for each of the supported platforms are:

Windows Systems
+++++++++++++++

First open a command window by clicking the search icon on the Windows Taskbar and enter "cmd". Then start Picard by entering the following in the command window:

.. code-block:: bash

   "C:\Program Files\MusicBrainz Picard\picard.exe" --debug

This will display all log entries in the command window, and allow you to copy the information to the clipboard to paste into your report.

.. note::

   This method will only work with the installed version of Picard. It will not work with the portable or Windows Store versions.


macOS Systems
+++++++++++++

First open a terminal window by doing one of the following:

- Click the Launchpad icon in the Dock, type "Terminal" in the search field, then click :guilabel:`Terminal`.

- In the Finder, open the "/Applications/Utilities" folder, then double-click "Terminal".

Assuming Picard was put into the system wide Applications folder when installed, it can then be started by entering the following in the terminal window:

.. code-block:: bash

   "/Applications/MusicBrainz Picard.app/Contents/MacOS/picard-run" --debug

This will display all log entries in the terminal window, and allow you to copy the information to the clipboard to paste into your report.


Linux Systems
+++++++++++++

First open a Terminal window in your desktop environment, either from the Applications menu or by pressing :kbd:`Ctrl+Alt+T` on most systems. Then start Picard by entering the following in the terminal window:

.. code-block:: bash

   picard --debug

This will display all log entries in the terminal window, and allow you to copy the information to the clipboard to paste into your report.


.. only:: html and not epub

   .. seealso::

      Specific situations:
      :doc:`does_not_start` /
      :doc:`no_coverart` /
      :doc:`missing_tags` /
      :doc:`not_saving` /
      :doc:`stopped_working`

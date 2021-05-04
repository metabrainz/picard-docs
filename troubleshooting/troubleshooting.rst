.. MusicBrainz Picard Documentation Project

:index:`General Troubleshooting <troubleshooting; general>`
============================================================

Getting Help
------------

If you have problems using Picard, please first check the following resources:

* For general usage information see the :doc:`../usage/using` documentation and the `illustrated quick start guide
  <https://picard.musicbrainz.org/docs/guide/>`_.
* Read the :doc:`FAQ section <../faq/faq>` for common questions and problems.
* Consult the `community forums <https://community.metabrainz.org/c/picard>`_.
* Check the `download page <https://picard.musicbrainz.org/downloads/>`_ for a newer version of Picard which might
  solve your problem.
* If the problem is to do with a plugin, check the `Picard Plugins <https://picard.musicbrainz.org/plugins/>`_ for
  updated plugin versions.


:index:`Reporting a Bug <troubleshooting; reporting a bug>`
------------------------------------------------------------

If you think you have found a bug please check whether you are using the latest version of Picard and whether the
bug has already been reported in the `bug tracker <https://tickets.musicbrainz.org/browse/PICARD>`_. If you're not
sure or don't want to look through the existing tickets, ask on the community forums first.

If you're still convinced you have found a new bug, open a `new ticket
<https://tickets.musicbrainz.org/secure/CreateIssue.jspa?pid=10042&issuetype=1>`_ providing the following information:

* Which version of Picard do you use? ("Affects Version" in the form)
* Which operating system do you use? ("Environment" in the form)
* What did you do when the bug occurred?
* What actually happened and what did you expect to happen?
* If you're using plugins, which plugins do you have enabled?


:index:`Getting Logs <troubleshooting; logs>`
----------------------------------------------

For many bugs, it helps developers to have a log from Picard. You can see the log by going to :menuselection:`"Help --> View Log"`.
You can also get a full debug log (better because it contains more detailed information) by starting Picard with :option:`-d` as a
command-line argument. If you're using Windows, you can change your shortcut's Target (:menuselection:`right click shortcut -->
Properties`) to::

    "C:\Program Files\MusicBrainz Picard\picard.exe" -d

Pasting this log into your forum post or bug ticket can help developers and other users to resolve your issue more quickly.

.. warning::

   Please remember to first remove any personal and confidential information like user id, passwords or authorization tokens
   before posting or submitting any log output.

.. only:: html

   .. seealso::

      Specific situations:
      :doc:`does_not_start` /
      :doc:`no_coverart` /
      :doc:`missing_tags` /
      :doc:`not_saving` /
      :doc:`stopped_working` /
      :doc:`macos_startup_error`

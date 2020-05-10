..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.


Troubleshooting
===============

Getting Help
------------

If you have problems using Picard, please first check the following resources:

* For general usage information see the :doc:`usage/usage` documentation and the `illustrated quick start guide
  <https://picard.musicbrainz.org/docs/guide/>`_.
* Read the :doc:`FAQ section <faq/faq>` for common questions and problems.
* Consult the `community forums <https://community.metabrainz.org/c/picard>`_.
* Check the `download page <https://picard.musicbrainz.org/downloads/>`_ for a newer version of Picard which might
  solve your problem.
* If the problem is to do with a plugin, check the `Picard Plugins <https://picard.musicbrainz.org/plugins/>`_ for
  updated plugin versions.


Reporting a Bug
---------------

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


Getting Logs
------------

For many bugs, it helps developers to have a log from Picard. You can see the log by going to :menuselection:`"Help --> View Log"`.
You can also get a full debug log (better because it contains more detailed information) by starting Picard with `-d` as a
command-line argument. If you're using Windows, you can change your shortcut's Target (:menuselection:`right click shortcut -->
Properties`) to::

    "C:\Program Files\MusicBrainz Picard\picard.exe" -d

Pasting this log into your forum post or bug ticket can help developers and other users to resolve your issue more quickly.  Please
remember to first remove any personal and confidential information like user id, passwords or authorization tokens.

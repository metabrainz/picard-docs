.. MusicBrainz Picard Documentation Project

:index:`Picard won't start <troubleshooting; program won't start>`
========================================================================

If you find that Picard won't start there are a few common possible reasons, and things to try to correct the issue.
Before doing anything drastic, it is recommended that you try to start Picard from the command line with the ``-d`` option
to generate the debug logging.  This process is described in the :doc:`troubleshooting` section.  If the resulting logs
don't provide any clues as to the problem, it may be one of the following:

**The program files have become corrupted**

   If you suspect that this may be the problem, the first (and simplest) thing to try is to reinstall the program.  This
   should address any potential file corruption issues.  If Picard still won't start then it is unlikely that this was
   the problem.

**A plugin file has become corrupted or is incompatible**

   To check whether one of the plugin files has become corrupted or, in the case of a recent upgrade to a plugin or Picard,
   a plugin is not compatible, you should try removing all of the plugins and then start Picard.  Since you won't be able
   to disable or remove the plugins using Picard's 'Option' settings, you will need to remove them manually.  The plugins
   may be located in a ``plugins`` subdirectory of the directory where the Picard program file is stored, or in a user-specific
   directory:

   - *Windows*: :file:`C:\\Users\\\\{user}\\AppData\\Local\\MusicBrainz\\Picard\\plugins`
   - *macOS*: :file:`~/Library/Preferences/MusicBrainz/Picard/plugins`
   - *Linux*: :file:`~/.config/MusicBrainz/Picard/plugins`

   Once you have located the plugin files, they should be removed from the ``plugins`` directory and moved to a temporary
   directory.  Then try to start Picard.  If the program starts, you should try restoring the plugin files from your temporary
   directory one at a time, and check if Picard will start.  This will help identify the plugin that was causing the problem.

**The option settings file has become corrupted or is incompatible**

   To check whether Picard's option settings file has become corrupted or, in the case of a recent upgrade to Picard, it is
   not compatible, you should try removing the settings file and then start Picard.  If Picard is started without finding its
   configuration settings file, it will create a new one using the default settings.  The settings file is called
   :file:`Picard.ini` and can be found in a user-specific directory:

   - *Windows*: :file:`C:\\Users\\\\{user}\\AppData\\Roaming\\MusicBrainz`
   - *macOS*: :file:`~/Library/Preferences/MusicBrainz`
   - *Linux*: :file:`~/.config/MusicBrainz`

   Again, it is recommended that you move the file to a temporary directory so that it can be recovered if this turns out not
   to be the cause of the problem.

**There really is a bug in Picard**

   If this problem started just after updating Picard, in spite of all the testing that is performed prior to releasing a new
   version, it may be possible that this is indeed a bug.  In that case, you should first try to reinstall the previous version
   to ensure that it works and that the problem is only occurring with the new version.  Then you should report the issue,
   following the steps outlined in the "Reporting a Bug" topic of the :doc:`troubleshooting` section.  Please be sure to include
   as much information as possible, which will help the developers to locate and fix the problem.

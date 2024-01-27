.. MusicBrainz Picard Documentation Project

:index:`External hard drive is not recognized <troubleshooting; external drive not recognized>`
===============================================================================================

There are some cases where Picard will not recognize an external hard drive connected to your system. Usually this is because Picard is using the custom file selector provided by the Qt library, rather than the native one provided by the operating system.

This can happen if the ":doc:`Allow selection of multiple directories </config/options_interface>`" option is selected. Because multi-directory selection is not possible in Qt when using the native operating system file selector, Picard then falls back to Qt's own file selector in this case.

If that's the issue then you only have the choice between either enabling multiple directory selection and not see the external drive, or disable this option and only select one directory at a time.

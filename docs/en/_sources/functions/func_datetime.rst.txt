..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

$datetime
=========

| Usage: **$datetime([format])**
| Category: information
| Implemented: Picard 2.3

**Description:**

Returns the current date and time in the specified format, which is based on the
standard Python ``strftime`` `format codes <https://strftime.org>`_. If no format is specified
the date and time will be returned in the form '2020-02-05 14:26:32'.  Note that any special
characters such as '%', '$', '(', ')' and '\\' will need to be escaped as shown in the
examples below.

**Note:** Platform-specific formatting codes should be avoided to help ensure the portability
of scripts across the different platforms.  These codes include: remove zero-padding (e.g.:
``%-d`` and ``%-m`` on Linux or macOS, and their equivalent ``%#d`` and ``%#m`` on Windows);
element length specifiers (e.g.: ``%3Y``); and hanging '%' at the end of the format string.


**Example:**

The following statements will return the values indicated::

    $datetime()                         ==>  "2020-02-05 14:26:32"
    $datetime(\%Y-\%m-\%d \%H:\%M:\%S)  ==>  "2020-02-05 14:26:32"
    $datetime(\%Y-\%m-\%d)              ==>  "2020-02-05"
    $datetime(\%H:\%M:\%S)              ==>  "14:26:32"
    $datetime(\%B \%d, \%Y)             ==>  "February 05, 2020"

.. MusicBrainz Picard Documentation Project

.. _func_datetime:

$datetime
=========

| Usage: **$datetime([format])**
| Category: information
| Implemented: Picard 2.3

**Description:**

Returns the current date and time in the specified format, which is based on the standard Python ``strftime`` `format codes <https://strftime.org>`_. If no format is specified the date and time will be returned in the form '2020-02-15 14:26:32'.

.. note::

   Any special characters such as '%', '$', '(', ')' and '\\' will need to be escaped as shown in the examples below.

.. warning::

   Platform-specific formatting codes should be avoided to help ensure the portability of scripts across the different platforms.  These codes include: remove zero-padding (e.g.: ``%-d`` and ``%-m`` on Linux or macOS, and their equivalents ``%#d`` and ``%#m`` on Windows); element length specifiers (e.g.: ``%3Y``); and hanging '%' at the end of the format string.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $datetime()                         ==>  "2020-02-15 14:26:32"
   $datetime(\%Y-\%m-\%d \%H:\%M:\%S)  ==>  "2020-02-15 14:26:32"
   $datetime(\%Y-\%m-\%d)              ==>  "2020-02-15"
   $datetime(\%H:\%M:\%S)              ==>  "14:26:32"
   $datetime(\%B \%d, \%Y)             ==>  "February 15, 2020"

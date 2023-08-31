.. MusicBrainz Picard Documentation Project

.. _func_dateformat:

$dateformat
===========

| Usage: **$dateformat(date,[format],[date order])**
| Category: information
| Implemented: Picard 2.7

**Description:**

Returns the input ``date`` in the specified ``format``, which is based on the standard Python ``strftime`` `format codes <https://strftime.org>`_. If no ``format`` is specified the date will be returned in the form '2020-02-15' (year, month, day).

The "year", "month" and "day" portions of the date must be entered as numbers, and can be separated by any non-numeric characters.  The default order for the input date is "ymd" (year, month, day).  This can be changed by specifying a ``date order``.

Valid entries for ``date order`` are:

- **ymd** - year, month, day (This is the default order.)
- **dmy** - day, month, year
- **mdy** - month, day, year

If either the ``date`` or ``format`` are invalid an empty string will be returned.  If an invalid ``date order`` is specified, the default order "ymd" will be used.

.. note::

   Any special characters such as '%', '$', '(', ')' and '\\' will need to be escaped as shown in the examples below.

.. warning::

   Platform-specific formatting codes should be avoided to help ensure the portability of scripts across the different platforms.  These codes include: remove zero-padding (e.g.: ``%-d`` and ``%-m`` on Linux or macOS, and their equivalents ``%#d`` and ``%#m`` on Windows); element length specifiers (e.g.: ``%3Y``); and hanging '%' at the end of the format string.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,07.21.2021)
   $set(bar,mdy)
   $set(format,\%Y.\%m.\%d)
   $dateformat(%foo%,%format%,%bar%)     ==>  "2021.07.21"

   $dateformat(2021 07 21)               ==>  "2021-07-21"
   $dateformat(2021.07.21)               ==>  "2021-07-21"
   $dateformat(2021-07-21)               ==>  "2021-07-21"
   $dateformat(2021-7-21)                ==>  "2021-07-21"
   $dateformat(2021-7-21,\%B \%d\, \%Y)  ==>  "July 21, 2021"

   $dateformat(2021-07-21,,myd)          ==>  "2021-07-21"
   $dateformat(2021-07-21,,dmy)          ==>  ""
   $dateformat(2021-07-21,,mdy)          ==>  ""
   $dateformat(2021-July-21)             ==>  ""
   $dateformat(2021)                     ==>  ""
   $dateformat(2021-07)                  ==>  ""
   $dateformat(,)                        ==>  ""

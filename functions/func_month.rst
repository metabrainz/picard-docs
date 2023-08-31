.. MusicBrainz Picard Documentation Project

.. _func_month:

$month
======

| Usage: **$month(date[,date order])**
| Category: information
| Implemented: Picard 2.7

**Description:**

Returns the "month" portion of the input ``date``.

The "year", "month" and "day" portions of the date must be entered as numbers, and can be separated by any non-numeric characters.  The default order for the input date is "ymd" (year, month, day).  This can be changed by specifying a ``date order``.

Valid entries for ``date order`` are:

- **ymd** - year, month, day (This is the default order.)
- **dmy** - day, month, year
- **mdy** - month, day, year

If the ``date`` is invalid an empty string will be returned.  If an invalid ``date order`` is specified, the default order "ymd" will be used.


**Examples:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,07.21.2020)
   $set(bar,mdy)
   $month(%foo%,%bar%)          ==>  "07"

   $month(2020 07 21)           ==>  "07"
   $month(2020.07.21)           ==>  "07"
   $month(2020-07-21)           ==>  "07"
   $month(2020-7-21)            ==>  "7"

   $noop( Invalid date order )
   $month(2020-07-21,dym)       ==>  "07"

   $month(,)                    ==>  ""
   $month(-21-2020,mdy)         ==>  ""

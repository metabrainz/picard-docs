.. MusicBrainz Picard Documentation Project

.. _func_month:

$month
======

| Usage: **$month(date[,date_order])**
| Category: information
| Implemented: Picard 2.7

**Description:**

Returns the "month" portion of the input ``date``.

The "year", "month" and "day" portions of the date must be entered as numbers, and can be separated
by any non-numeric characters.  The default order for the input date is "ymd".  This can be changed
by specifying a ``date_order`` of either "dmy" or "mdy".  If anything other than "ymd", "dmy" or
"mdy" is specified, the default order "ymd" will be used.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,07.21.2020)
   $set(bar,mdy)
   $month(%foo%,%bar%)     ==>  "07"

   $month(2020 07 21)      ==>  "07"
   $month(2020.07.21)      ==>  "07"
   $month(2020-07-21)      ==>  "07"
   $month(2020-7-21)       ==>  "7"

   $month(2020-07-21,dym)  ==>  "07" (invalid date order)

   $month(,)               ==>  ""
   $month(-21-2020,mdy)    ==>  ""

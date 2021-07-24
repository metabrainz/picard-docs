.. MusicBrainz Picard Documentation Project

.. _func_year:

$year
=====

| Usage: **$year(date[,date_order])**
| Category: information
| Implemented: Picard 2.7

**Description:**

Returns the "year" portion of the input ``date``.

The "year", "month" and "day" portions of the date must be entered as numbers, and can be separated
by any non-numeric characters.  The default order for the input date is "ymd".  This can be changed
by specifying a ``date_order`` of either "dmy" or "mdy".  If anything other than "ymd", "dmy" or
"mdy" is specified, the default order "ymd" will be used.


**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

   $set(foo,07.21.2020)
   $set(bar,mdy)
   $year(%foo%,%bar%)       ==>  "2020"

   $year(2020 07 21)        ==>  "2020"
   $year(2020.07.21)        ==>  "2020"
   $year(2020-07-21)        ==>  "2020"
   $year(20-7-21)           ==>  "20"

   $year(2020-07-21,dym)    ==>  "2020" (invalid date order)

   $month(,)                 ==>  ""
   $month(07-21,mdy)         ==>  ""
   $month(21-07,dmy)         ==>  ""
   $month(21-July-2020,dmy)  ==>  "" (month is not numeric)

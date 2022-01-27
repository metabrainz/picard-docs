.. MusicBrainz Picard Documentation Project

:index:`Scripting Functions <scripting; functions>`
====================================================

The following is a list of the Picard scripting functions grouped by function type.


:index:`Assignment Functions <scripting functions; assignment>`
----------------------------------------------------------------

These functions are used to assign (or unassign) a value to a tag or variable. The assignment
scripting functions are:

.. toctree::
   :maxdepth: 1

   func_copy
   func_copymerge
   func_delete
   func_set
   func_setmulti
   func_unset


:index:`Text Functions <scripting functions; text>`
----------------------------------------------------

These functions are used to manage text (e.g.: extract, replace or format) in tags or variables.
The text scripting functions are:

.. toctree::
   :maxdepth: 1

   func_delprefix
   func_find
   func_firstalphachar
   func_firstwords
   func_get
   func_initials
   func_left
   func_len
   func_lower
   func_num
   func_pad
   func_replace
   func_reverse
   func_right
   func_rreplace
   func_rsearch
   func_strip
   func_substr
   func_swapprefix
   func_title
   func_trim
   func_truncate
   func_upper


:index:`Multi-Value Functions <scripting functions; multi-value>`
------------------------------------------------------------------

These functions are used to manage multi-value tags or variables.  The multi-value scripting
functions are:

.. toctree::
   :maxdepth: 1

   func_cleanmulti
   func_getmulti
   func_join
   func_lenmulti
   func_map
   func_performer
   func_replacemulti
   func_reversemulti
   func_slice
   func_sortmulti
   func_unique


:index:`Mathematical Functions <scripting functions; mathematical>`
--------------------------------------------------------------------

These functions are used to perform arithmetic operations on tags or variables.  The mathematical
scripting functions are:

.. toctree::
   :maxdepth: 1

   func_add
   func_div
   func_mod
   func_mul
   func_sub


:index:`Conditional Functions <scripting functions; conditional>`
------------------------------------------------------------------

These functions are used to test for various conditions and take appropriate actions depending on
the results of the test.

.. warning::

   Formatting the code in your scripts by adding things like spaces, tabs and newlines could affect
   the results of conditional tests because these characters are not ignored. For example,

   .. code-block:: taggerscript

      $set(test,)
      $if(
         %test%,
         $set(test1,Not Empty),
         $set(test1,Empty)
      )
      $if(%test%,$set(test2,Not Empty),$set(test2,Empty))

   will return "Not Empty" for ``%test1%``, but "Empty" for ``%test2%``. The different values are a
   result of the indentation in the formatted code.

The conditional scripting functions are:

.. toctree::
   :maxdepth: 1

   func_and
   func_endswith
   func_eq
   func_eq_all
   func_eq_any
   func_gt
   func_gte
   func_if
   func_if2
   func_in
   func_inmulti
   func_is_audio
   func_is_complete
   func_is_multi
   func_is_video
   func_lt
   func_lte
   func_ne
   func_ne_all
   func_ne_any
   func_not
   func_or
   func_startswith


:index:`Information Functions <scripting functions; information>`
------------------------------------------------------------------

These functions provide additional system or data information. The information scripting functions are:

.. toctree::
   :maxdepth: 1

   func_countryname
   func_dateformat
   func_datetime
   func_day
   func_matchedtracks
   func_month
   func_year


:index:`Loop Functions <scripting functions; loop>`
----------------------------------------------------

These functions provide the ability to repeat actions based on the contents of a multi-value variable or
the result of a conditional test.  The loop scripting functions are:

.. toctree::
   :maxdepth: 1

   func_foreach
   func_while


:index:`Miscellaneous Functions <scripting functions; miscellaneous>`
----------------------------------------------------------------------

The miscellaneous scripting functions are:

.. toctree::
   :maxdepth: 1

   func_noop


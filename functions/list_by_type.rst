.. MusicBrainz Picard Documentation Project

:index:`Scripting Functions <scripting; functions>`
====================================================

The following is a list of the Picard scripting functions grouped by function type.


:index:`Assignment Functions <scripting functions; assignment>`
----------------------------------------------------------------

These functions are used to assign (or unassign) a value to a tag or variable. The assignment
scripting functions are:

.. only:: not epub

   .. toctree::
      :maxdepth: 1

      func_copy
      func_copymerge
      func_delete
      func_set
      func_setmulti
      func_unset

.. only:: epub

   | :doc:`func_copy`
   | :doc:`func_copymerge`
   | :doc:`func_delete`
   | :doc:`func_set`
   | :doc:`func_setmulti`
   | :doc:`func_unset`

:index:`Text Functions <scripting functions; text>`
----------------------------------------------------

These functions are used to manage text (e.g.: extract, replace or format) in tags or variables.
The text scripting functions are:

.. only:: not epub

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

.. only:: epub

   | :doc:`func_delprefix`
   | :doc:`func_find`
   | :doc:`func_firstalphachar`
   | :doc:`func_firstwords`
   | :doc:`func_get`
   | :doc:`func_initials`
   | :doc:`func_left`
   | :doc:`func_len`
   | :doc:`func_lower`
   | :doc:`func_num`
   | :doc:`func_pad`
   | :doc:`func_replace`
   | :doc:`func_reverse`
   | :doc:`func_right`
   | :doc:`func_rreplace`
   | :doc:`func_rsearch`
   | :doc:`func_strip`
   | :doc:`func_substr`
   | :doc:`func_swapprefix`
   | :doc:`func_title`
   | :doc:`func_trim`
   | :doc:`func_truncate`
   | :doc:`func_upper`


:index:`Multi-Value Functions <scripting functions; multi-value>`
------------------------------------------------------------------

These functions are used to manage multi-value tags or variables.  The multi-value scripting
functions are:

.. only:: not epub

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

.. only:: epub

   | :doc:`func_cleanmulti`
   | :doc:`func_getmulti`
   | :doc:`func_join`
   | :doc:`func_lenmulti`
   | :doc:`func_map`
   | :doc:`func_performer`
   | :doc:`func_replacemulti`
   | :doc:`func_reversemulti`
   | :doc:`func_slice`
   | :doc:`func_sortmulti`
   | :doc:`func_unique`


:index:`Mathematical Functions <scripting functions; mathematical>`
--------------------------------------------------------------------

These functions are used to perform arithmetic operations on tags or variables.  The mathematical
scripting functions are:

.. only:: not epub

   .. toctree::
      :maxdepth: 1

      func_add
      func_div
      func_mod
      func_mul
      func_sub

.. only:: epub

   | :doc:`func_add`
   | :doc:`func_div`
   | :doc:`func_mod`
   | :doc:`func_mul`
   | :doc:`func_sub`


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

.. only:: not epub

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

.. only:: epub

   | :doc:`func_and`
   | :doc:`func_endswith`
   | :doc:`func_eq`
   | :doc:`func_eq_all`
   | :doc:`func_eq_any`
   | :doc:`func_gt`
   | :doc:`func_gte`
   | :doc:`func_if`
   | :doc:`func_if2`
   | :doc:`func_in`
   | :doc:`func_inmulti`
   | :doc:`func_is_audio`
   | :doc:`func_is_complete`
   | :doc:`func_is_multi`
   | :doc:`func_is_video`
   | :doc:`func_lt`
   | :doc:`func_lte`
   | :doc:`func_ne`
   | :doc:`func_ne_all`
   | :doc:`func_ne_any`
   | :doc:`func_not`
   | :doc:`func_or`
   | :doc:`func_startswith`


:index:`Information Functions <scripting functions; information>`
------------------------------------------------------------------

These functions provide additional system or data information. The information scripting functions are:

.. only:: not epub

   .. toctree::
      :maxdepth: 1

      func_countryname
      func_dateformat
      func_datetime
      func_day
      func_matchedtracks
      func_max
      func_min
      func_month
      func_year

.. only:: epub

   | :doc:`func_countryname`
   | :doc:`func_dateformat`
   | :doc:`func_datetime`
   | :doc:`func_day`
   | :doc:`func_matchedtracks`
   | :doc:`func_max`
   | :doc:`func_min`
   | :doc:`func_month`
   | :doc:`func_year`


:index:`Loop Functions <scripting functions; loop>`
----------------------------------------------------

These functions provide the ability to repeat actions based on the contents of a multi-value variable or
the result of a conditional test.  The loop scripting functions are:

.. only:: not epub

   .. toctree::
      :maxdepth: 1

      func_foreach
      func_while

.. only:: epub

   | :doc:`func_foreach`
   | :doc:`func_while`


:index:`Miscellaneous Functions <scripting functions; miscellaneous>`
----------------------------------------------------------------------

The miscellaneous scripting functions are:

.. only:: not epub

   .. toctree::
      :maxdepth: 1

      func_noop

.. only:: epub

   :doc:`func_noop`


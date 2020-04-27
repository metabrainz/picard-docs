..  MusicBrainz Picard Documentation Project
..  Copyright (C) 2020  Bob Swift (rdswift).
..  Permission is granted to copy, distribute and/or modify this document
..  under the terms of the GNU Free Documentation License, Version 1.3
..  or any later version published by the Free Software Foundation;
..  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
..  A copy of the license is available at https://www.gnu.org/licenses/fdl-1.3.html.

Scripting Functions
===================

The following is a list of the Picard scripting functions grouped by function type.


Assignment Functions
--------------------
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


Text Functions
--------------
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


Multi-Value Functions
---------------------
These functions are used to manage multi-value tags or variables.  The multi-value scripting
functions are:

.. toctree::
   :maxdepth: 1

   func_getmulti
   func_join
   func_lenmulti
   func_map
   func_performer
   func_reversemulti
   func_slice
   func_sortmulti


Mathematical Functions
----------------------
These functions are used to perform arithmetic operations on tags or variables.  The mathematical
scripting functions are:

.. toctree::
   :maxdepth: 1

   func_add
   func_div
   func_mod
   func_mul
   func_sub


Conditional Functions
---------------------
These functions are used to test for various conditions and take appropriate actions depending on
the results of the test. The conditional scripting functions are:

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
   func_is_video
   func_lt
   func_lte
   func_ne
   func_ne_all
   func_ne_any
   func_not
   func_or
   func_startswith


Information Functions
---------------------
These functions provide additional system or data information. The information scripting functions are:

.. toctree::
   :maxdepth: 1

   func_datetime
   func_matchedtracks


Loop Functions
--------------
These functions provide the ability to repeat actions based on the contents of a multi-value variable or
the result of a conditional test.  The loop scripting functions are:

.. toctree::
   :maxdepth: 1

   func_foreach
   func_while


Miscellaneous Functions
-----------------------
The miscellaneous scripting functions are:

.. toctree::
   :maxdepth: 1

   func_noop


.. MusicBrainz Picard Documentation Project

$map
====

| Usage: **$map(name,code[,separator])**
| Category: multi-value
| Implemented: Picard 2.3

**Description:**

Iterates over each element found in the multi-value variable ``name`` and updates the value
of the element to the value returned by ``code``, returning the updated multi-value variable.
A literal value representing a multi-value can be substituted for ``name``, using the
``separator`` (or a semicolon followed by a space "; " if not passed) to coerce the value
into a proper multi-valued variable.

For each loop, the element value is first stored in the variable ``_loop_value`` and the count
is stored in the variable ``_loop_count``. This allows the element or count value to be
accessed within the code script.

Empty elements are automatically removed from the output.

.. note::

    You cannot save the ``code`` to a variable and then pass the variable to the function
    as ``%code%`` because it will be evaluated when it is assigned to the variable rather than
    during the loop.


**Example:**

.. only:: html

   The following statements will return the values indicated::

       $set(foo,First:A; Second:B)
       $map(%foo%,$upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; SECOND:B"
       $map(%foo%,$upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"

       $setmulti(bar,First:A; Second:B)
       $map(%bar%,$upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B"
       $map(%bar%,$upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"

       $setmulti(baz,A; B; x; C)
       $map(%baz%,$if($eq(%_loop_value%,x),,%_loop_count%=%_loop_value%))
                                                          ==> "1=A; 2=B; 4=C"
       $map(First:A; Second:B,
           $upper(%_loop_count%=%_loop_value%))           ==>  "1=FIRST:A; 2=SECOND:B"

       $map(First:A; Second:B,
           $upper(%_loop_count%=%_loop_value%),:)         ==>  "1=FIRST:2=A; SECOND:3=B"

.. only:: latex

   The following statements will return the values indicated::

       $set(foo,First:A; Second:B)
       $map(%foo%,
           $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; SECOND:B"
       $map(%foo%,
           $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"

       $setmulti(bar,First:A; Second:B)
       $map(%bar%,
           $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B"
       $map(%bar%,
           $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"

       $setmulti(baz,A; B; x; C)
       $map(%baz%,$if($eq(%_loop_value%,x),,%_loop_count%=%_loop_value%))
                                                   ==> "1=A; 2=B; 4=C"
       $map(First:A; Second:B,
           $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B"

..    $map(First:A; Second:B,
..        $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"
..
..    $set(foo,First:A; Second:B)
..    $map(%foo%,
..        $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; SECOND:B"
..    $map(%foo%,
..        $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"
..
..    $setmulti(bar,First:A; Second:B)
..    $map(%bar%,
..        $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B"
..    $map(%bar%,
..        $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"
..
..    $map(First:A; Second:B,
..        $upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B"
..
..    $map(First:A; Second:B,
..        $upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B"

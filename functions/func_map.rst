.. Picard Function

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

Note that you cannot save the ``code`` to a variable and then pass the variable to the function
as ``%code%`` because it will be evaluated when it is assigned to the variable rather than
during the loop.


**Example:**

The following statements will return the values indicated::

    $set(foo,First:A; Second:B; Third:C)
    $map(%foo%,$upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; SECOND:B; THIRD:C"
    $map(%foo%,$upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B; THIRD:4=C"

    $setmulti(bar,First:A; Second:B; Third:C)
    $map(%bar%,$upper(%_loop_count%=%_loop_value%))    ==>  "1=FIRST:A; 2=SECOND:B; 3=THIRD:C"
    $map(%bar%,$upper(%_loop_count%=%_loop_value%),:)  ==>  "1=FIRST:2=A; SECOND:3=B; THIRD:4=C"

    $map(First:A; Second:B; Third:C,$upper(%_loop_count%=%_loop_value%))  ==>
                                                            "1=FIRST:A; 2=SECOND:B; 3=THIRD:C"

    $map(First:A; Second:B; Third:C,$upper(%_loop_count%=%_loop_value%),:)  ==>
                                                            "1=FIRST:2=A; SECOND:3=B; THIRD:4=C"

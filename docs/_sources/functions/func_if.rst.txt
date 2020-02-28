.. Picard Function

$if
===

| Usage: **$if(condition,then[,else])**
| Category: conditional

**Description:**

If ``condition`` is not empty it returns ``then``, otherwise it returns ``else``.  If ``else``
is not provided, it will be assumed to be "".  In addition to (or instead of) returning values,
``then`` and ``else`` can be used to conditionally execute other functions.


**Example:**

The following statements will return the values indicated::

    $set(foo,This is foo)
    $set(bar,)
    $if(%foo%,%foo%,No foo)                   ==>  "This is foo"
    $if(%bar%,%bar%,No bar)                   ==>  "No bar"
    $if(%bar%,This is bar,No bar)             ==>  "No bar"
    $if(%bar%,This is bar,)                   ==>  ""
    $if(%bar%,This is bar)                    ==>  ""
    $if(,True,False)                          ==>  "False"
    $if( ,True,False)                         ==>  "True"
    $if(,$set(value,True),$set(value,False))  ==>  Sets %value% to "False"
    $set(value,$if(%bar%,True,False))         ==>  Sets %value% to "False"

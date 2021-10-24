.. MusicBrainz Picard Documentation Project

.. _func_if:

$if
===

| Usage: **$if(condition,then[,else])**
| Category: conditional

**Description:**

If ``condition`` is not empty it returns ``then``, otherwise it returns ``else``.  If ``else``
is not provided, it will be assumed to be an empty string.  In addition to (or instead of) returning values,
``then`` and ``else`` can be used to conditionally execute other functions.

.. note::

   Spaces, tabs or newlines in the ``condition`` will make it not register as empty.  For example,

   .. code-block:: taggerscript

      $set(test,)
      $if(
         %test%,
         $set(test1,Not Empty),
         $set(test1,Empty)
      )
      $if(%test%,$set(test2,Not Empty),$set(test2,Empty))

   will return "Not Empty" for ``%test1%`` and "Empty" for ``%test2%``.

**Example:**

The following statements will return the values indicated:

.. code-block:: taggerscript

    $set(foo,This is foo)
    $set(bar,)
    $if(%foo%,%foo%,No foo)                   ==>  "This is foo"
    $if(%bar%,%bar%,No bar)                   ==>  "No bar"
    $if(%bar%,This is bar,No bar)             ==>  "No bar"
    $if(%bar%,This is bar,)                   ==>  ""
    $if(%bar%,This is bar)                    ==>  ""
    $if(,True,False)                          ==>  "False"
    $if( ,True,False)                         ==>  "True"
    $if(,$set(value,True),$set(value,False))  ==>  Sets "value" to "False"
    $set(value,$if(%bar%,True,False))         ==>  Sets "value" to "False"

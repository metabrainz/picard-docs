.. Picard Function

$strip
======

| Usage: **$strip(text)**
| Category: text

**Description:**

Replaces all whitespace in ``text`` with a single space, and removes leading and trailing spaces.
Whitespace characters include multiple consecutive spaces, and various other unicode characters.
Characters such as newlines "\n", tabs "\t" and returns "\r" are treated as spaces.


**Example:**

The following statements will each return "This text has been stripped."::

    $strip(This text has been stripped.)
    $strip(This text has been stripped.  )
    $strip(  This text has been stripped.  )
    $strip(  This  text has been stripped.)
    $strip(  This  text has been stripped.  )
    $strip(This  text  has  been  stripped.)
    $strip(This  text\rhas\nbeen\tstripped.)

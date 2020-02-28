.. Picard Function

$datetime
=========

| Usage: **$datetime([format])**
| Category: information
| Implemented: Picard 2.3

**Description:**

Returns the current date and time in the specified format, which is based on the
standard Python ``strftime`` `format codes <https://strftime.org>`_. If no format is specified
the date/time will be returned in the form '2020-02-05 14:26:32'.  Note that any special
characters such as '%', '$', '(', ')' and '\' will need to be escaped as shown in the
examples below.


**Example:**

The following statements will return the values indicated::

    $datetime()                         ==>  "2020-02-05 14:26:32"
    $datetime(\%Y-\%m-\%d \%H:\%M:\%S)  ==>  "2020-02-05 14:26:32"
    $datetime(\%Y-\%m-\%d)              ==>  "2020-02-05"
    $datetime(\%H:\%M:\%S)              ==>  "14:26:32"
    $datetime(\%B \%d, \%Y)             ==>  "February 05, 2020"

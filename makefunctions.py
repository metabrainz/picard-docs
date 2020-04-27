#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

FUNCTIONS = """\
$if(if,then,else)
conditional
If if is not empty, it returns then, otherwise it returns else.
$if2(a1,a2,a3,...)
conditional
Returns first non empty argument.
$lower(text)
text
Returns text in lower case.
$upper(text)
text
Returns text in upper case.
$reverse(text)
text
Returns text> in reverse order.
$left(text,num)
text
Returns the first num characters from text.
$right(text,num)
text
Returns the last num characters from text.
$substr(text,start,end)
text
Returns the substring beginning with the character at the start index, up to (but not including) the character at the end index. Indexes are zero-based. Negative numbers will be counted back from the end of the string. If the start or end indexes are left blank, they will default to the start and end of the string respectively.
$find(haystack,needle)
text
Finds the location of one string within another. Returns the index of the first occurrance of needle in haystack, or -1 if needle was not found.
$matchedtracks()
information
Returns the number of matched tracks within a release.
Only works in File Naming scripts.
Added in version 0.12
$is_complete()
conditional
Returns true if every track in the album is matched to a single file.
Only works in File Naming scripts.
$num(num,len)
text
Returns num formatted to len digits, where len cannot be greater than 20.
$replace(text,search,replace)
text
Replaces occurrences of search in text with value of replace and returns the resulting string.
$rsearch(text,pattern)
text
Regular expression search. This function will return the first matching group.
$rreplace(text,pattern,replace)
text
Regular expression replace.
$in(x,y)
conditional
Returns true, if x contains y.
$inmulti(%x%,y)
conditional
Returns true if multi-value variable x contains exactly y as one of its values.
Since Picard 1.0
$set(name,value)
assignment
Sets the variable name to value.
Note: To create a variable which can be used for the file naming string, but which will not be written as a tag in the file, prefix the variable name with an underscore. %something% will create a "something" tag; %_something% will not.
$setmulti(name,value,separator="; ")
assignment
Sets the variable name to value, using the separator (or "; " if not passed) to coerce the value back into a proper multi-valued tag. This can be used to operate on multi-valued tags as a string, and then set them back as proper multi-valued tags, e.g $setmulti(genre,$lower(%genre%))
Since Picard 1.0
$unset(name)
assignment
Unsets the variable name.
Allows for wildcards to unset certain tags (works with 'performer:*', 'comment:*', and 'lyrics:*').
i.e. $unset(performer:*) would unset all performer tags.
$delete(name)
assignment
Unsets the variable name and marks the tag for deletion.
This is similar to $unset(name) but also marks the tag for deletion. E.g. running $delete(genre) will actually remove the genre tag from a file when saving.
Since Picard 2.1
$get(name)
text
Returns the variable name (equivalent to %name%).
$getmulti(name,index,separator="; ")
multi-value
Gets the element at index from the multi-value tag name. A literal value representing a multi-value can be substituted for name, using the separator (or "; " if not passed) to coerce the value into a proper multi-valued tag.
$slice(name,start,end,separator="; ")
multi-value
Returns a multi-value variable containing the elements between the start and end indexes from the multi-value tag name. A literal value representing a multi-value can be substituted for name, using the separator (or "; " if not passed) to coerce the value into a proper multi-valued tag. Indexes are zero based. Negative numbers will be counted back from the end of the list. If the start or end indexes are left blank, they will default to the start and end of the list respectively.
For example, the following will create a multi-value variable with all artists in %artists% except the first, which can be used to create a "feat." list. $setmulti(supporting_artists,$slice(%artists%,1,))
$join(name,text,separator="; ")
multi-value
Joins all elements in name, placing text between each element, and returns the result as a string.
$map(name,code,separator="; ")
multi-value
Iterates over each element found in the multi-value tag name and updates the value of the element to the value returned by code, returning the updated multi-value tag. For each loop, the element value is first stored in the tag _loop_value and the count is stored in the tag _loop_count. This allows the element or count value to be accessed within the code script.
$foreach(name,code,separator="; ")
loop
Iterates over each element found in the multi-value tag name, executing code. For each loop, the element value is first stored in the tag _loop_value and the count is stored in the tag _loop_count. This allows the element or count value to be accessed within the code script. A literal value representing a multi-value can be substituted for name, using the separator (or "; " if not passed) to coerce the value into a proper multi-valued tag.
$while(condition,code)
loop
Standard 'while' loop. Executes code repeatedly until condition no longer evaluates to True. For each loop, the count is stored in the tag _loop_count. This allows the count value to be accessed within the code script. The function limites the maximum number of iterations to 1000 as a safeguard against accidentally creating an infinite loop.
$copy(new,old)
assignment
Copies metadata from variable old to new. The difference between $set(new,%old%) is that $copy(new,old) copies multi-value variables without flattening them.
Since Picard 0.9
$copymerge(new,old)
assignment
Merges metadata from variable old into new, removing duplicates and appending to the end, so retaining the original ordering. Like $copy, this will also copy multi-valued variables without flattening them.
Since Picard 1.0
$pad(text,length,char)
text
Pads the text to the length provided by adding as many copies of char as needed to the beginning of the string.
$strip(text)
text
Replaces all whitespace in text with a single space, and removes leading and trailing spaces. Whitespace characters include multiple consecutive spaces, and various other unicode characters.
$trim(text[,char])
text
Trims all leading and trailing whitespaces from text. The optional second parameter specifies the character to trim.
$add(x,y,*args)
mathematical
Add y to x.
Can be used with an arbitrary number of arguments.
i.e. $add(x,y,z) = ((x + y) + z)
$sub(x,y,*args)
mathematical
Subtracts y from x.
Can be used with an arbitrary number of arguments.
i.e. $sub(x,y,z) = ((x - y) - z)
$div(x,y,*args)
mathematical
Divides x by y.
Can be used with an arbitrary number of arguments.
i.e. $div(x,y,z) = ((x / y) / z)
$mod(x,y,*args)
mathematical
Returns the remainder of x divided by y.
Can be used with an arbitrary number of arguments.
i.e. $mod(x,y,z) = ((x % y) % z)
$mul(x,y,*args)
mathematical
Multiplies x by y.
Can be used with an arbitrary number of arguments.
i.e. $mul(x,y,z) = ((x * y) * z)
$or(x,y,*args)
conditional
Returns true if either x or y not empty.
Can be used with an arbitrary number of arguments. The result is true if ANY of the arguments is not empty.
$and(x,y,*args)
conditional
Returns true if both x and y are not empty.
Can be used with an arbitrary number of arguments. The result is true if ALL of the arguments are not empty.
$not(x)
conditional
Returns true if x is empty.
$eq(x,y)
conditional
Returns true if x equals y.
$ne(x,y)
conditional
Returns true if x does not equal y.
$lt(x,y)
conditional
Returns true if x is less than y.
$lte(x,y)
conditional
Returns true if x is less than or equal to y.
$gt(x,y)
conditional
Returns true if x is greater than y.
$gte(x,y)
conditional
Returns true if x is greater than or equal to y.
$eq_any(x,a1,a2...)
conditional
Returns true if x equals a1 or a2 or ...
Functionally equivalent to $or($eq(x,a1),$eq(x,a2) ...).
Functionally equivalent to the eq2 plugin.
$eq_all(x,a1,a2...)
conditional
Returns true if x equals a1 and a2 and ...
Functionally equivalent to $and($eq(x,a1),$eq(x,a2) ...).
$ne_all(x,a1,a2...)
conditional
Returns true if x does not equal a1 and a2 and ...
Functionally equivalent to $and($ne(x,a1),$ne(x,a2) ...).
Functionally equivalent to the ne2 plugin.
$ne_any(x,a1,a2...)
conditional
Returns true if x does not equal a1 or a2 or ...
Functionally equivalent to $or($ne(x,a1),$ne(x,a2) ...).
$noop(...)
miscellaneous
Does nothing (useful for comments or disabling a block of code).
$len(text)
text
Returns the number of characters in text.
$lenmulti(name,separator="; ")
multi-value
Returns the number of elements in the multi-value tag name. A literal value representing a multi-value can be substituted for name, using the separator (or "; " if not passed) to coerce the value into a proper multi-valued tag.
For example, the following will return the value "3". $lenmulti(One; Two; Three)
$performer(pattern="",join=", ")
multi-value
Returns the performers where the performance type (e.g. "vocal") matches pattern, joined by join.
Since Picard 0.10
$title(text)
text
Returns text in title case (first character in every word capitalized).
Since Picard 2.1
$firstalphachar(text,nonalpha="#")
text
Returns the first character of text. If text is not an alphabetic character nonalpha is returned instead.
Since Picard 0.12
$initials(text)
text
Returns the first character of each word in text, if it is an alphabetic character.
Since Picard 0.12
$truncate(text,length)
text
Truncate text to length.
Since Picard 0.12
$firstwords(text,length)
text
Like $truncate except that it will only return the complete words from text which fit within length characters.
Since Picard 0.12
$swapprefix(text,*prefixes="a","the")
text
Moves the specified prefixes from the beginning to the end of text. If no prefix is specified 'A' and 'The' are used by default. $swapprefix(%albumartist%,A,An,The,Le)
Integrated since Picard 1.3, previously as a plugin since Picard 0.13
$delprefix(text,*prefixes="a","the")
text
Deletes the specified prefixes from the beginning of text. If no prefix is specified 'A' and 'The' are used by default.
Since Picard 1.3
$startswith(text,prefix)
conditional
Returns true if text starts with prefix.
Since Picard 1.4
$endswith(text,suffix)
conditional
Returns true if text ends with suffix.
Since Picard 1.4
$is_audio()
conditional
Returns true, if the file processed is an audio file.
Since Picard 2.2
$is_video()
conditional
Returns true, if the file processed is an video file.
Since Picard 2.2
$datetime(format="%Y-%m-%d %H:%M:%S")
information
Returns the current date and time in the specified format, which is based on the standard Python strftime format codes. If no format is specified the date/time will be returned in the form '2020-02-05 14:26:32'.
Since Picard 2.3
$sortmulti(name,separator="; ")
multi-value
Returns a copy of the multi-value tag ``name`` with the elements sorted in ascending order.
$reversemulti(name,separator="; ")
multi-value
Returns a copy of the multi-value tag ``name`` with the elements in reverse order. This can be used in conjunction with the ``$sortmulti``</code>`` function to sort in descending order.
""".splitlines()

function_dict = {}
filename = ''
counter = 0
linecount = len(FUNCTIONS)
content = ''
func = ''
while counter < linecount:
    line = FUNCTIONS[counter].replace('*', '\\*')
    if line.startswith('$') and line.endswith(')'):
        if filename and content:
            content += '\n\n**Example:**\n\nThe statement::\n\n    {0}\n\nwill...\n'.format(func)
            with open(filename, 'w', encoding='utf8') as f:
                f.write(content)
        func = line
        counter += 1
        category = FUNCTIONS[counter].lower()
        index = line.find('(')
        filename = os.path.join('functions', 'func_{0}.rst'.format(line[1:index]))
        title = line[:index]
        content = ".. Picard Function\n\n{0}\n{1}\n\n| Usage: **{3}**\n| Category: {2}\n| Implemented: Picard\n\n**Description:**\n".format(title, '=' * len(title), category, line)
        function_dict['func_{0}'.format(line[1:index])] = category
    else:
        content += "\n{0}\n".format(line)
    counter += 1

if filename and content:
    content += '\n\n**Example:**\n\nThe statement::\n\n    {0}\n\nwill...\n'.format(func)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(content)

cat_lists = {}
for value in function_dict.values():
    cat_lists[value] = []

filename = os.path.join('functions', 'alpha_list.txt')
with open(filename, 'w', encoding='utf8') as f:
    for key in sorted(function_dict.keys()):
        cat_lists[function_dict[key]].append(key)
        f.write(key + '\n')

filename = os.path.join('functions', 'cat_list.txt')
with open(filename, 'w', encoding='utf8') as f:
    for key in sorted(cat_lists.keys()):
        title = "{0} functions".format(key,).title()
        f.write("\n\n{0}\n{1}\n\n.. toctree::\n   :maxdepth: 0\n   :caption: The {2} scripting functions are:\n\n".format(title, '-' * len(title), key))
        value = cat_lists[key]
        for func in sorted(value):
            f.write("   {0}\n".format(func,))

saved = """
$if(condition,then,else)
========================

If ``condition`` is not empty it returns ``then``, otherwise it returns ``else``.

**Example:**

The statement::

    $if(%comment%,%comment%,No comment provided)

will return the content of the ``comment`` tag, or "No comment provided" if the ``comment`` tag is empty.
"""

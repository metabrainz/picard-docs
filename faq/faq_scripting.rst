.. MusicBrainz Picard Documentation Project

Picard Scripting
=================

Why won't my script run?
-------------------------

If you have a script that doesn't seem to be running or shows as having error in the editor, review the following common issues:

1. **Is the script enabled?**

   |  Make sure that the script is enabled in the scripting options. If the script is not enabled, it will not run automatically. You can run the script manually from the context menu for the track or album, but it will not run automatically when you load files or perform other actions.

2. **Is there a syntax error in the script?**

   |  If there is a syntax error in the script, it will not run and may show an error in the editor. Review the script for any syntax errors such as missing parentheses, incorrect function names, or other issues that may cause the script to not run.

3. **Are all the functions used in the script valid?**

   |  If you are using a function in your script that is not valid or does not exist, the script will not run. Make sure that all the functions you are using in your script are valid and exist in Picard. This can happen if the function is provided by a plugin that is not enabled or if the function name is misspelled.

4. **Have all reserved characters been escaped properly?**

   |  If your script includes reserved characters such as commas, parentheses, or other special characters as part of an argument, make sure they are escaped properly. If you want to include a comma in an argument's value, you should escape it with a backslash (e.g.: ``\,``) to prevent it from being interpreted as a separator between arguments. The same applies to other reserved characters that may be part of an argument's value. For example, if you want to check if the artist's name is "100%", you should use ``$eq(%artist%,100\%)``.

   If reserved characters are not escaped properly, it can cause the script to not run or to run with unexpected results. This is a common occurence when using AI to develop scripts, because it often includes reserved characters in the value arguments without escaping them.

   One of the most common issues with improperly escaped reserved characters is when using the regular expression functions ``$rsearch()`` and ``$rreplace()``. These can be especially tricky because the regular expression syntax itself includes reserved characters, so you may need to escape reserved characters both for the regular expression syntax and for the scripting syntax. For example, if you want to replace some text enclosed in square brackets ("Some \[enclosed text\]") in a track title with the text enclosed with parentheses ("Some (enclosed text)") where the Python regular expression statement would be:

   .. code-block:: python

      re.sub(r'\[([^\]]*)\]', r'(\1)', "Some [enclosed text]")

   you would need to use something like:

   .. code-block:: taggerscript

      $set(title,$rreplace(%title%,\\[\([^\\]]*\)\\],\(\\1\)))

   The reserved characters include: comma (``,``), parentheses (``(`` and ``)``), backslash (``\``), dollar sign (``$``), and percent sign (``%``). Make sure to review your script for any reserved characters in the argument values and escape them properly to ensure your script runs as expected.


Why don't matches work in my scripts?
--------------------------------------

If you have checks such as ``$eq(%artist%,My Artist)`` in your scripts, but they don't seem to be working, review the following common issues:

1. **Are you using the correct syntax?**

   |  Make sure you are using the correct tag or variable and value in the correct order, and that there are no typos.

2. **Are you using the correct tag or variable name?**

   |  Make sure you are using the correct tag or variable name in your script. For example, if you want to check the artist name, you should use ``%artist%`` and not ``%artist name%`` or any other variation.

3. **Is the tag or variable you are checking actually populated?**

   |  If the tag or variable you are checking is empty or not populated, the match will not work. Make sure that it has a value before the script runs. This can be an issue if the tag or variable is being populated by a different script, but the script with the match is running before the other script. In that case, you may need to adjust the order of your scripts or add a check to ensure the tag or variable is populated before running the match.

4. **Is the spelling and capitalization correct?**

   |  In general, the match tests are case-sensitive, so make sure that the spelling and capitalization of the value you are checking against matches exactly with the value in the tag or variable.

5. **Are you using the correct operator?**

   |  Make sure you are using the correct operator for your match. For example, if you want to check if a tag or variable contains a certain value, you should use ``$in(%tag_name%,value)`` instead of ``$eq(%tag_name%,value)``.

6. **Are there any leading or trailing spaces or unnecessary quotes in the value argument?**

   |  If there are leading or trailing spaces in the value or the value is enclosed within quotes, the match may not work as expected. This is a common occurence when using AI to develop scripts, because it often introduces extra spaces such as a space after the comma separating arguments or quotes around the value. Picard will consider both of these are part of the argument. For example, if you have a script that checks if the artist is "My Artist", but the check is ``$eq(%artist%,"My Artist")`` or ``$eq(%artist%, My Artist)``, the match will not work. The correct syntax should be ``$eq(%artist%,My Artist)`` without the quotes or extra spaces.

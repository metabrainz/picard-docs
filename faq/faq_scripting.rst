.. MusicBrainz Picard Documentation Project

Picard Scripting
=================

Why don't matches work in my scripts?
--------------------------------------

If you have checks such as ``$eq(%artist%,My Artist)`` in your scripts, but they don't seem to be working, check the following common issues:

1. **Are you using the correct syntax?**

   |  Make sure you are using the correct field name and value in the correct order, and that there are no typos.

2. **Is the field you are checking actually populated?**

   |  If the field you are checking is empty or not populated, the match will not work. Make sure that the field you are checking has a value before the script runs. This can be an issue if the field is being populated by a previous script, but the script with the match is running before the field is populated. In that case, you may need to adjust the order of your scripts or add a check to ensure the field is populated before running the match.

3. **Are you using the correct field name?**

   |  Make sure you are using the correct field name in your script. For example, if you want to check the artist name, you should use ``%artist%`` and not ``%artist name%`` or any other variation.

4. **Is the spelling and capitalization correct?**

   |  In general, the match tests are case-sensitive, so make sure that the spelling and capitalization of the value you are checking against matches exactly with the value in the field.

5. **Are you using the correct operator?**

   |  Make sure you are using the correct operator for your match. For example, if you want to check if a field contains a certain value, you should use ``$in(%field%,value)`` instead of ``$eq(%field%,value)``.

6. **Are there any leading or trailing spaces or unnecessary quotes in the field value?**

   |  If there are leading or trailing spaces in the field value or the value is enclosed within quotes, the match may not work as expected. This is a common occurence when using AI to develop scripts, because it often introduces extra spaces such as a space after the comma separating arguments or quotes around the value. For example, if you have a script that checks if the artist is "My Artist", but the check is ``$eq(%artist%,"My Artist")`` or ``$eq(%artist%, My Artist)``, the match will not work. The correct syntax should be ``$eq(%artist%,My Artist)`` without the quotes or extra spaces.

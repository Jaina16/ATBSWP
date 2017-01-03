####---------------- Automate the boring stuff with Python ----------------####

###### ================================================================= ######

1. What are escape characters?

Solution:
---------

Escape characters are a sequence of characters that allow inserting of 
characters that are otherwise difficult or impossible to type in.

For example, the new-line character '\n', a backslash '\\',
a carriage return '\r', a vertical tab '\v', a tab '\t', etc.

###### ================================================================= ######

2. What do the \n and \t escape characters represent?

Solution:
---------

The \n escape character reperesents a new-line character.
The \t escape character represents a tab (usually consists of 4 spaces).

###### ================================================================= ######

3. How can you put a \ backslash character in a string?

Solution:
---------

By using two backslashes, as in \\. 

###### ================================================================= ######

4. The string value "Howl's Moving Castle" is a valid string. Why isn't
it a problem that the single quote character in the word Howl's isn't
escaped?

Solution:
---------

This is legal Python syntax if you are using double quotes to create a
string literal.

###### ================================================================= ######

5. If you don't want to put \n in your string, how can you write a 
string with new lines in it?

Solution:
---------

You can create multi line string literals using triple quotes as in
''' or """. String literals that are created using a pair of these 
triple quotes, preserve the text formatting as it is. That is each
new line appears as is, without having to use any escape characters.
Other escape characters such a ' or " can also be included within
the string literal without using escape characters. Such string
literals are also referred to as "raw strings". 

Tip: A raw string can also be created by using single quotation marks
(' or "), but it has to be pre-fixed with r just before the string
literal begins as in r"this is a \ raw string!!". These are useful
while working with regular expressions.

###### ================================================================= ######

6. What do the following expressions eavaluate to?

    * 'Hello World!'[1]
    * 'Hello World!'[0:5]
    * 'Hello World!'[:5]
    * 'Hello World!'[3:]

Solution:
---------

>>> 'Hello World!'[1]
'e'
>>> 'Hello World'[0:5]
'Hello'
>>> 'Hello World!'[:5]
'Hello'
>>> 'Hello World!'[3:]
'lo World!'

###### ================================================================= ######

7. What do the following expressions evaluate to?

 *  'Hello'.upper()
 *  'Hello'.upper().isupper()
 *  'Hello'.upper().lower()

Solution:
---------

>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().isupper()
True
>>> 'Hello'.upper().lower()
'hello'

###### ================================================================= ######

8. What do the following expression evaluate to?

 *  'Remember, remember, the fifth of November.'.split()
 *  '-'.join('There can be only one.'.split())

Solution:
---------

>>> 'Remember, remember, the fifth of November.'.split()
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
>>> '-'.join('There can be only one.'.split())
'There-can-be-only-one.'

###### ================================================================= ######

9. What string methods can you use to right-justify, left-justify, and
center a string?

Solution:
---------

rjust() can be used to right-justify a string

ljust() can be used to left-justify a string

center() can be used to center a string

###### ================================================================= ######

10. How can you trim whitespace characters from the beginning or end of
a string?

Solution:
---------

lstrip() can be used to trim whitespace on the left side of a string

rstrip() can be used to trim whitespace on the right side of a string

strip() can be used to trim whitespace on both sides of a string

###### ================================================================= ######

####----------------------------- END OF FILE -----------------------------####

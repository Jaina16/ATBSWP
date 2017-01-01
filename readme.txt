####---------------- Automate the boring stuff with Python ----------------####

1. What does the code for an empty dictionary look like?

emptyDict = {}

###### ================================================================= ######

2. What does a dictionary value with a key 'foo' and a value 42? look like?

myDict = {'foo': 42}

###### ================================================================= ######

3. What is the main difference between a dictionary and a list?

Dictionaries have the capability to contain key and value pairs whereas
lists can only contain values.

###### ================================================================= ######

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

You get a KeyError error

###### ================================================================= ######

5. If a dictionary is stored in spam, what is the difference between the
   expressions 'cat' in spam and 'cat' in spam.keys()?

The expressions 'cat' in spam and 'cat' in spam.keys() tests if the
dictionary spam has a key that is labelled 'cat'. There is no difference
it is the same expression expressed more explicitly.

###### ================================================================= ######

6. If a dictionary is stored in spam, what is the difference between the
   expressions 'cat' in spam and 'cat' in spam.values()?

Solution:
---------

The expression 'cat' in spam is a condition that tests for a key labelled
'cat' in the dictionary spam, whereas the condition 'cat' in spam.values()
checks if the dictionary spam has a value of 'cat'.

###### ================================================================= ######

7. What is a shortcut for the following code?

    if 'color' not in spam:
        spam['color'] = 'black'

Solution:
---------

spam.setdefault('color', 'black')

refer: characterCount.py

###### ================================================================= ######

8. What module and function can be used to "pretty print" dictionary values?

Solution:
---------

import pprint

myDict = {'key': 'value', [keys: values]}

pprint.pprint()

refer: prettyCharacterCount.py

###### ================================================================= ######

####----------------------------- END OF FILE -----------------------------####

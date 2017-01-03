#!/usr/bin/env python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

'''

Input Constraints: Please provide text input from a simple
text editor or verify the input being provided for best
results. Otherwise you'll end up with unexpected results.

'''

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')

for i in range(len(lines)): # loop throgh all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

# Test String (Copy it to the clipboard):

'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

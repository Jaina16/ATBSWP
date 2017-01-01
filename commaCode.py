#!/usr/bin/env python3

'''
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with
and inserted before the last item.
'''

## Simple Approach

def commaCode2(itemsList):
    ''' Does the same thing as commaCode
        but employs a simpler approach '''
    # The idea behind this approach is to use list slicing
    items = itemsList[:-1] + ['and'] + itemsList[-1:]
    items = ', '.join(items)
    return items

## Complex Approach

def commaCode(itemsList):
    ''' This function returns a string
        that is made up of items contained
        in the itemsList, formatted with
        commas and spaces, and the word
        and inserted just before the last
        item in the list '''
    items = ''
    for item in itemsList:
        items += item + ', '
        itemsList.remove(item)
        if len(itemsList) == 2:
            items += item + ', and,'
    items += ' ' + itemsList[-1]
    return items

# Test Case

numbers = ['one', 'two', 'three', 'four']
spam = ['apples', 'bananas', 'tofu', 'cats']

print(commaCode2(spam))
print()
print(commaCode2(numbers))

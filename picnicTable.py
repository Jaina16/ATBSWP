#!/usr/bin/env python3

def printPicnic(itemsDict, leftWidth, rightWidth):
    ''' Prints the contents of a dictionary in a
        neatly formatted manner using built-in
        functions to manipulate strings '''
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

#!/usr/bin/env python3

# ------------------------------------------------------------------- #
#       Author:             Janeskumar Patel
#       Date & Time:        Mon Jan 02 2017 14:33:40
#       Practice Project:   Table Printer
#       Tutorial:           Automate the boring stuff with python
#       Tutor:              Al Sweigart  
# ------------------------------------------------------------------- #

'''
Write a function named printTable() that takes a list of lists
of strings and displays it in a well-organized table with each
column right-justified. Assume that all the inner list will 
contain the same number of strings.
'''

def printTable(tableContents):
    ''' This function processes a 2D list data
        into a fine table layout using Python's
        built-in methods for processing strings.
        Input: A 2D list (assume that the length
        of all inner lists is the same)
        Return Value: String (Containing a neatly
        organized table) '''
    colWidths = [0] * len(tableData)
    biggestWord = 0

    for row in tableContents:
        for item in row:
            if len(item) > biggestWord:
                biggestWord = len(item)

    table = ''
    for row in zip(*tableData):
        for item in row:
            table += item.rjust(biggestWord)
        table += '\n'
    
    print(table.rstrip('\n'))
    return None

# Test Data

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],]

if __name__ == '__main__':
    printTable(tableData)

#!/usr/bin/env python3

grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],]

# print the inverse of the grid above

## In simpler words print the first column as the first row and so on...

## The most simplest of approach is to use the built-in zip() function
## and pass in the list that needs to be rotated

for row in zip(*grid):
    print()
    for item in row:
        print(item, end='')

'''

Hint:

You will need to use a nested loop in order to print grid[0][0],
then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will fin-
ish the first row, so then print a newline. Then your program should print
grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your
program will print is grid[8][5].

'''

## The desired output for this program should look like:

'''

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''

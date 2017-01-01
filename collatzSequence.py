#!/usr/bin/env python3

# ------------------------------------------------------------- #
#  Author: Janes Patel
#  Practice Project: The Collatz Sequence
#  Date & Time: Wed Dec 28 12:18:05
#  Tutorial: Automate the Boring stuff with Python
#  Tutor: Al Sweigart
# ------------------------------------------------------------- #

## import your modules here

''' Write a function named collatz() that has one parameter
    named number. If number is even, then collatz() should
    print (number // 2) and return this value. If number is
    odd, then collatz() should print and return (3 * number + 1)'''

def collatz(number):
    ''' This function determines if a number
        is even or odd, then based upon the
        outcome of the determination, it 
        returns a value computed using an
        arithmetic expression '''
    
    isEven = (number % 2 == 0) # check if the number is even
    isOdd = (number % 2 == 1) # check if the number is odd
    
    if isEven:
        return (number // 2) ## return the desired value if even
    elif isOdd:
        return (3 * number + 1)
    else:
        return None

''' Write a program that lets the user type in an integer
    and that keeps calling collatz() on that number until
    the function returns the value 1. (Amazingly enough,
    this sequence works for any integer -- sooner or later,
    using this sequence, you'll arrive at 1! 
    
    EVEN MATHEMATICIANS AREN'T SURE WHY.)'''

# Get an integer from the user
# Please handle input errors gracefully

while True:
    try:
        getInt = int(input("Please type in an integer: "))
        if not getInt == None:
            break
    except ValueError:
        print("Invalid number! Please choose an integer.")

# keep calling collatz on the user input
# until the function returns 1.

collatzReturns = collatz(getInt)

while True:
    print(collatzReturns)
    collatzReturns = collatz(collatzReturns)
    if collatzReturns == 1:
        print(collatzReturns)
        break

''' Your program is exploring what's called the 
    Collatz Sequence, sometimes called:
    "the simplest impossible math problem" '''

## Test strings:
## print("The user typed:", getInt) 

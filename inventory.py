#!/usr/bin/env python3

'''

Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

'''

def displayInventory(inventory):
    ''' Takes a dictionary as input and
        displays a neatly formatted print
        of values and keys on a new line,
        and finally the total of the values
        in the inventory '''
    itemTotal = 0
    print('Inventory:')
    for key, value in inventory.items():
        print(value, key)
        itemTotal += value
    print('Total number of items:', itemTotal)
    return None

# Executes only when the module itself has been run

if __name__ == '__main__':
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    
    displayInventory(stuff)

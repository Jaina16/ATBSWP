#!/usr/bin/env python3

import inventory

'''
-------------------------------------------------------------------------------

Write a function named addToInventory(inventory, addedItems), 
where the inventory parameter is a dictionary representing the
player’s inventory (like in the previous project) and the addedItems
parameter is a list like dragonLoot.

The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.

The previous program (with your displayInventory() function from the
previous project) would output the following:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48

-------------------------------------------------------------------------------
'''

def addToInventory(inventory, addedItems):
    ''' Adds items to the inventory from
        the addedItems list, both given as
        parameters to the function and
        returns an updated inventory'''
    
    for item in addedItems:
        inventory.setdefault(item, 0)
        if item in inventory.keys():
            inventory[item] += 1
    
    return inventory

# Test case:

if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope':1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    inventory.displayInventory(inv)

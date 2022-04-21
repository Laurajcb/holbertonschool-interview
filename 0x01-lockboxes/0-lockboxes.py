#!/usr/bin/python3
""" 
Method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """ 
    Returns ture or false if all the boxes can be unlocked
    """

    unlocked = []
    keys = []
    
    for i in boxes:    
        unlocked.append(0)
    
    if len(boxes) > 0:
        unlocked[0] = 1    
        keys.append(0)

    while keys:
        key = keys.pop(0)
        new_keys = boxes[key]
        unlocked[key] = 1
        for new_key in new_keys:
            if unlocked[new_key] == 0:
                keys.append(new_key)

    for unlock in unlocked:
        if unlock != 1:
            return False
    return True

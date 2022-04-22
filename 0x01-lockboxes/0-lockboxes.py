#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
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
            if int(new_key) < len(unlocked) and unlocked[new_key] == 0:
                keys.append(new_key)
    for unlock in unlocked:
        if unlock != 1:
            return False
    return True

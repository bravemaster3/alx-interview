#!/usr/bin/python3
"""
This is the implementation of a lockbox
"""


def canUnlockAll(boxes):
    """Lockbox implementation"""
    num_boxes = len(boxes)
    opened = {i: False for i in range(num_boxes)}
    opened[0] = True
    my_keys = boxes[0]

    while True:
        unlockable = False
        for key in my_keys:
            if key < num_boxes and not opened[key]:
                opened[key] = True
                my_keys.extend(boxes[key])
                unlockable = True
        if not unlockable:
            break
    return all(opened.values())

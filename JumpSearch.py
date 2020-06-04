#********************************************************************
# Filename:  JumpSearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the jump search algorithm.
#*********************************************************************

import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1


if __name__ == "__main__":

    collection = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    print("List numbers: %s\n" % repr(collection))

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = jump_search(collection, target)
    
    if result is not None:
        print("%s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")


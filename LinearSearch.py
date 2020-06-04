#********************************************************************
# Filename:  LinearSearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the linear search algorithm.
#*********************************************************************

def linear_search(sequence, target):
    
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == "__main__":

    collection = [0, 5, 7, 10, 15]
    print("List numbers: %s\n" % repr(collection))

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = linear_search(collection, target)
    
    if result is not None:
        print("%s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")

#********************************************************************
# Filename:  SimpleBinarySearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the simple binary search algorithm.
#*********************************************************************

def binary_search(a_list, item):
    
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    if item < a_list[midpoint]:
        return binary_search(a_list[:midpoint], item)
    else:
        return binary_search(a_list[midpoint + 1 :], item)


if __name__ == "__main__":

    collection = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print("List numbers: %s\n" % repr(collection))

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = binary_search(collection, target)
    
    if result:
        print("Number found in list")
    else:
        print("Number not found in list")
#********************************************************************
# Filename:  SentinelLinearSearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the sentinel linear search algorithm.
#*********************************************************************

def sentinel_linear_search(sequence, target):
    
    sequence.append(target)

    index = 0
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == "__main__":

    collection = [0, 5, 7, 10, 15]
    print("List numbers: %s\n" % repr(collection))

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = sentinel_linear_search(collection, target)
    
    if result is not None:
        print("%s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")

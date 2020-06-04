#********************************************************************
# Filename:  TernarySearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the ternary search algorithm.
#*********************************************************************

import sys

precision = 10

# This is the linear search that will occur after the search space has become smaller.
def lin_search(left, right, A, target):
    for i in range(left, right + 1):
        if A[i] == target:
            return i

# This is the iterative method of the ternary search algorithm.
def ite_ternary_search(A, target):
    left = 0
    right = len(A) - 1
    while True:
        if left < right:

            if right - left < precision:
                return lin_search(left, right, A, target)

            oneThird = (left + right) / 3 + 1
            twoThird = 2 * (left + right) / 3 + 1

            if A[oneThird] == target:
                return oneThird
            elif A[twoThird] == target:
                return twoThird

            elif target < A[oneThird]:
                right = oneThird - 1
            elif A[twoThird] < target:
                left = twoThird + 1

            else:
                left = oneThird + 1
                right = twoThird - 1
        else:
            return None


# This is the recursive method of the ternary search algorithm.
def rec_ternary_search(left, right, A, target):
    if left < right:

        if right - left < precision:
            return lin_search(left, right, A, target)

        oneThird = (left + right) / 3 + 1
        twoThird = 2 * (left + right) / 3 + 1

        if A[oneThird] == target:
            return oneThird
        elif A[twoThird] == target:
            return twoThird

        elif target < A[oneThird]:
            return rec_ternary_search(left, oneThird - 1, A, target)
        elif A[twoThird] < target:
            return rec_ternary_search(twoThird + 1, right, A, target)

        else:
            return rec_ternary_search(oneThird + 1, twoThird - 1, A, target)
    else:
        return None


# This function is to check if the array is sorted.
def __assert_sorted(collection):
    if collection != sorted(collection):
        raise ValueError("Collection must be sorted")
    return True


if __name__ == "__main__":

    collection = [1, 2, 5, 7, 8, 10, 11, 15]
    print("List numbers: %s\n" % repr(collection))

    __assert_sorted(collection)

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = ite_ternary_search(collection, target)
     
    if result is not None:
        print("ITE ternary %s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")


    target_input = input("\nEnter a single number to be found in the list:\n")
    target = int(target_input)
    result = rec_ternary_search(0, len(collection) - 1, collection, target)
     
    if result is not None:
        print("REC ternary %s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")

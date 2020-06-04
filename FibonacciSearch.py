#********************************************************************
# Filename:  FibonacciSearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the fibonacci search algorithm.
#*********************************************************************

def fibonacci_search(arr, val):
      
    fib_N_2 = 0
    fib_N_1 = 1
    fibNext = fib_N_1 + fib_N_2
    length = len(arr)
    if length == 0:
        return 0
    while fibNext < len(arr):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2
    index = -1
    while fibNext > 1:
        i = min(index + fib_N_2, (length - 1))
        if arr[i] < val:
            fibNext = fib_N_1
            fib_N_1 = fib_N_2
            fib_N_2 = fibNext - fib_N_1
            index = i
        elif arr[i] > val:
            fibNext = fib_N_2
            fib_N_1 = fib_N_1 - fib_N_2
            fib_N_2 = fibNext - fib_N_1
        else:
            return i
    if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
        return index + 1
    return -1


if __name__ == "__main__":
    
    collection = [1, 6, 7, 0, 0, 0]
    print("List numbers: %s\n" % repr(collection))

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = fibonacci_search(collection, target)
    
    if result > 0:
        print("%s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")    
    
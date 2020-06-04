#********************************************************************
# Filename:  InterpolationSearch.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the interpolation search algorithm.
#*********************************************************************

def interpolation_search(sorted_collection, item):
    
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        # avoid divided by 0 during interpolation
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            else:
                return None

        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        # out of range check
        if point < 0 or point >= len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if point < left:
                right = left
                left = point
            elif point > right:
                left = right
                right = point
            else:
                if item < current_item:
                    right = point - 1
                else:
                    left = point + 1
    return None


def interpolation_search_by_recursion(sorted_collection, item, left, right):
        
    # avoid divided by 0 during interpolation
    if sorted_collection[left] == sorted_collection[right]:
        if sorted_collection[left] == item:
            return left
        else:
            return None

    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # out of range check
    if point < 0 or point >= len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    elif point < left:
        return interpolation_search_by_recursion(sorted_collection, item, point, left)
    elif point > right:
        return interpolation_search_by_recursion(sorted_collection, item, right, left)
    else:
        if sorted_collection[point] > item:
            return interpolation_search_by_recursion(
                sorted_collection, item, left, point - 1
            )
        else:
            return interpolation_search_by_recursion(
                sorted_collection, item, point + 1, right
            )


def __assert_sorted(collection):
    """Check if collection is ascending sorted, if not - raises :py:class:`ValueError`
    :param collection: collection
    :return: True if collection is ascending sorted
    :raise: :py:class:`ValueError` if collection is not ascending sorted
    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True
    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be ascending sorted
    """
    if collection != sorted(collection):
        raise ValueError("Collection must be ascending sorted")
    return True


if __name__ == "__main__":

    collection = [10, 30, 40, 45, 50, 66, 77, 93]
    print("List numbers: %s\n" % repr(collection))

    __assert_sorted(collection)

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = interpolation_search(collection, target)
    
    if result is not None:
        print("%s found at positions: %s" % (target, result))
    else:
        print("Number not found in list")

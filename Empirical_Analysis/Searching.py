def linear_search(arr, target):
    """
    Perform a linear search to find the target element in the given list.

    Args:
    arr (list): The list to search in.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Perform a binary search to find the target element in the sorted list.

    Args:
    arr (list): The sorted list to search in.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
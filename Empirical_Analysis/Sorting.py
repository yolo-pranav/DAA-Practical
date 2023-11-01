def bubble_sort(arr):
    """
    Sort a list using the bubble sort algorithm.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """
    Sort a list using the quick sort algorithm.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
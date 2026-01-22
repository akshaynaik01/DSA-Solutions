"""
Bubble Sort Algorithm
Simplest sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they're in wrong order.

Time Complexity: O(n^2)
Space Complexity: O(1)

Example:
    Input: [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Standard Bubble Sort - O(n^2) in worst and average case
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they're in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, array is already sorted
        if not swapped:
            break
    return arr


def bubble_sort_optimized(arr: List[int]) -> List[int]:
    """
    Optimized Bubble Sort with early termination
    Best case: O(n) when array is already sorted
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


def bubble_sort_descending(arr: List[int]) -> List[int]:
    """
    Bubble Sort in descending order
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Changed comparison for descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Test cases
if __name__ == "__main__":
    # Test case 1: Random array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr1}")
    print(f"Sorted: {bubble_sort(arr1.copy())}")
    
    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted: {arr2}")
    print(f"After sort: {bubble_sort_optimized(arr2.copy())}")
    
    # Test case 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print(f"\nReverse sorted: {arr3}")
    print(f"After sort: {bubble_sort(arr3.copy())}")
    
    # Test case 4: Descending order
    arr4 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nDescending: {bubble_sort_descending(arr4.copy())}")

"""
Reverse Array Problem
Reverse an array in-place without using extra space

Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""

from typing import List


def reverse_array_two_pointer(arr: List[int]) -> None:
    """
    Two pointer approach - O(n) time, O(1) space
    Swap elements from start and end moving towards center
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def reverse_array_slicing(arr: List[int]) -> List[int]:
    """
    Python slicing approach - Clean and Pythonic
    """
    return arr[::-1]


def reverse_array_recursion(arr: List[int], start: int = 0) -> None:
    """
    Recursive approach - O(n) time, O(n) space (due to recursion stack)
    """
    end = len(arr) - 1 - start
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array_recursion(arr, start + 1)


def reverse_array_stack(arr: List[int]) -> List[int]:
    """
    Using stack - O(n) time, O(n) space
    """
    stack = []
    for num in arr:
        stack.append(num)
    
    result = []
    while stack:
        result.append(stack.pop())
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 2, 3, 4, 5]
    reverse_array_two_pointer(arr1)
    print(f"Two Pointer: {arr1}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test case 2
    arr2 = [1, 2, 3, 4, 5]
    print(f"Slicing: {reverse_array_slicing(arr2)}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test case 3
    arr3 = [1, 2, 3, 4, 5]
    reverse_array_recursion(arr3)
    print(f"Recursion: {arr3}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test case 4
    arr4 = [1, 2, 3, 4, 5]
    print(f"Stack: {reverse_array_stack(arr4)}")  # Expected: [5, 4, 3, 2, 1]

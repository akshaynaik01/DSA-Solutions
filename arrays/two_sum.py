"""
Two Sum Problem
Given an array of integers nums and an integer target, return the indices 
of the two numbers that add up to target.
You may assume each input has exactly one solution.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
"""

from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute Force Approach - O(n^2) time complexity
    Check every pair of numbers
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Hash Map Approach - O(n) time complexity, O(n) space complexity
    Use a hash map to store seen numbers and their indices
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []


def two_sum_two_pointer(nums: List[int], target: int) -> List[int]:
    """
    Two Pointer Approach - O(n log n) time (due to sorting)
    Works if array is sorted; returns original indices
    """
    # Create list of (value, original_index) and sort by value
    indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][1] + indexed_nums[right][1]
        if current_sum == target:
            # Return original indices
            return sorted([indexed_nums[left][0], indexed_nums[right][0]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Hash Map: {two_sum_hash_map(nums, target)}")  # Expected: [0, 1]
    print(f"Brute Force: {two_sum_brute_force(nums, target)}")  # Expected: [0, 1]
    
    # Test case 2
    nums = [3, 2, 4]
    target = 6
    print(f"Hash Map: {two_sum_hash_map(nums, target)}")  # Expected: [1, 2]
    print(f"Brute Force: {two_sum_brute_force(nums, target)}")  # Expected: [1, 2]

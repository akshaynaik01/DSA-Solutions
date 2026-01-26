def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to search in
        target: Element to search for
    
    Returns:
        Index of the target element if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_all_occurrences(arr, target):
    """
    Linear Search to find all occurrences of target
    
    Args:
        arr: List of elements to search in
        target: Element to search for
    
    Returns:
        List of all indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 25]
    
    # Search for a single element
    target = 22
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
    
    # Search for element not in array
    target = 100
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
    
    # Find all occurrences
    target = 25
    indices = linear_search_all_occurrences(arr, target)
    if indices:
        print(f"\nElement {target} found at indices: {indices}")
    else:
        print(f"\nElement {target} not found in the array")
    
    # Edge cases
    print("\nEdge Cases:")
    print("Empty array:", linear_search([], 5))
    print("Single element (found):", linear_search([5], 5))
    print("Single element (not found):", linear_search([5], 10))

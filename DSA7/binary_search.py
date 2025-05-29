def binary_search(arr: list, target: int) -> int:
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

# Example usage
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9, 11],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1]
    ]
    
    test_targets = [3, 7, 9, 8, 1]
    
    for arr, target in zip(test_arrays, test_targets):
        result = binary_search(arr, target)
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Index: {result}")
        print("-" * 30) 
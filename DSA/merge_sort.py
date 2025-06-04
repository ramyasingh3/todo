def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort an array using the merge sort algorithm.
    
    Args:
        arr (list[int]): Input array to be sorted
        
    Returns:
        list[int]: Sorted array
    """
    if len(arr) <= 1:
        return arr
        
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left (list[int]): First sorted array
        right (list[int]): Second sorted array
        
    Returns:
        list[int]: Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    result.extend(left[i:])
    
    # Add remaining elements from right array
    result.extend(right[j:])
    
    return result

# Example usage
if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 12, 1, 3],
        [1],
        [],
        [1, 1, 1, 1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [10, 7, 8, 9, 1, 5],
        [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    ]
    
    for arr in test_cases:
        sorted_arr = merge_sort(arr.copy())
        print(f"Original array: {arr}")
        print(f"Sorted array: {sorted_arr}\n") 
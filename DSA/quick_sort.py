def quick_sort(arr: list[int]) -> list[int]:
    """
    Sort an array using the quick sort algorithm.
    
    Args:
        arr (list[int]): Input array to be sorted
        
    Returns:
        list[int]: Sorted array
    """
    if len(arr) <= 1:
        return arr
        
    # Choose pivot (using middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition elements
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_in_place(arr: list[int], low: int, high: int) -> None:
    """
    Sort an array in-place using quick sort algorithm.
    
    Args:
        arr (list[int]): Input array to be sorted
        low (int): Starting index
        high (int): Ending index
    """
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the array around a pivot.
    
    Args:
        arr (list[int]): Input array
        low (int): Starting index
        high (int): Ending index
        
    Returns:
        int: Index of the pivot after partitioning
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

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
    
    print("Testing Quick Sort (with new array):")
    for arr in test_cases:
        sorted_arr = quick_sort(arr.copy())
        print(f"Original array: {arr}")
        print(f"Sorted array: {sorted_arr}\n")
    
    print("\nTesting Quick Sort (in-place):")
    for arr in test_cases:
        arr_copy = arr.copy()
        if arr_copy:
            quick_sort_in_place(arr_copy, 0, len(arr_copy) - 1)
        print(f"Original array: {arr}")
        print(f"Sorted array: {arr_copy}\n") 
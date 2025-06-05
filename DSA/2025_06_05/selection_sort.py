# Selection Sort Implementation
# Time Complexity: O(n²) for all cases (best, average, worst)
# Space Complexity: O(1) - in-place sorting

def selection_sort_basic(arr):
    """Basic selection sort implementation"""
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def selection_sort_with_comparison_count(arr):
    """Selection sort with comparison and swap counting"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps

def selection_sort_recursive(arr, start=0):
    """Recursive selection sort implementation"""
    n = len(arr)
    
    # Base case: if we've processed all elements
    if start >= n - 1:
        return arr
    
    # Find the minimum element in the unsorted portion
    min_idx = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    # Swap if minimum is not already in position
    if min_idx != start:
        arr[start], arr[min_idx] = arr[min_idx], arr[start]
    
    # Recursively sort the remaining elements
    return selection_sort_recursive(arr, start + 1)

def selection_sort_visualization(arr):
    """Selection sort with step-by-step visualization"""
    n = len(arr)
    print(f"Original array: {arr}")
    
    for i in range(n):
        min_idx = i
        print(f"\nPass {i + 1}:")
        print(f"  Looking for minimum in unsorted portion: {arr[i:]}")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"    Found new minimum: {arr[j]} at index {j}")
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  Swapped {arr[i]} with {arr[min_idx]}: {arr}")
        else:
            print(f"  No swap needed, {arr[i]} is already in correct position")
    
    return arr

def selection_sort_stable(arr):
    """Stable selection sort (maintains relative order of equal elements)"""
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Move the minimum element to its correct position
        # by shifting elements instead of swapping
        min_val = arr[min_idx]
        for k in range(min_idx, i, -1):
            arr[k] = arr[k - 1]
        arr[i] = min_val
    
    return arr

def selection_sort_optimized(arr):
    """Optimized selection sort with early termination for sorted arrays"""
    n = len(arr)
    swaps = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        
        # If no swaps in this pass, array might be sorted
        if swaps == 0 and i > 0:
            break
    
    return arr

def find_kth_smallest_selection(arr, k):
    """Find kth smallest element using selection sort approach"""
    n = len(arr)
    
    if k < 1 or k > n:
        return None
    
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr[k - 1]

def is_sorted(arr):
    """Check if array is sorted"""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1],  # Single element
        [],   # Empty array
        [3, 3, 3, 3],  # Duplicate elements
        [1, 5, 2, 8, 3, 9, 7, 4, 6]
    ]
    
    print("Selection Sort Algorithm Analysis")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        original = arr.copy()
        
        # Test basic selection sort
        result_basic = selection_sort_basic(arr.copy())
        print(f"Basic: {result_basic}")
        
        # Test with comparison counting
        result_count, comps, swaps = selection_sort_with_comparison_count(arr.copy())
        print(f"Comparisons: {comps}, Swaps: {swaps}")
        
        # Test recursive selection sort
        result_rec = selection_sort_recursive(arr.copy())
        print(f"Recursive: {result_rec}")
        
        # Test stable selection sort
        result_stable = selection_sort_stable(arr.copy())
        print(f"Stable: {result_stable}")
        
        # Verify sorting
        print(f"Correctly sorted: {is_sorted(result_basic)}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Comparison:")
    
    import time
    import random
    
    # Generate large test array
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    # Test basic selection sort
    start = time.time()
    selection_sort_basic(large_array.copy())
    basic_time = time.time() - start
    
    # Test optimized selection sort
    start = time.time()
    selection_sort_optimized(large_array.copy())
    opt_time = time.time() - start
    
    print(f"Basic selection sort time: {basic_time:.6f}s")
    print(f"Optimized selection sort time: {opt_time:.6f}s")
    
    # Visualization example
    print("\n" + "=" * 50)
    print("Step-by-step visualization:")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    selection_sort_visualization(demo_array.copy())
    
    # Kth smallest element example
    print("\n" + "=" * 50)
    print("Finding kth smallest element:")
    test_array = [7, 10, 4, 3, 20, 15]
    for k in range(1, len(test_array) + 1):
        kth_smallest = find_kth_smallest_selection(test_array.copy(), k)
        print(f"{k}th smallest element: {kth_smallest}") 
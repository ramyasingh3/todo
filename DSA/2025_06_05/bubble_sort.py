# Bubble Sort Implementation
# Time Complexity: O(n²) worst/average case, O(n) best case
# Space Complexity: O(1) - in-place sorting

def bubble_sort_basic(arr):
    """Basic bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_optimized(arr):
    """Optimized bubble sort with early termination"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr

def bubble_sort_recursive(arr, n=None):
    """Recursive bubble sort implementation"""
    if n is None:
        n = len(arr)
    
    # Base case: if array has 1 element, it's sorted
    if n == 1:
        return arr
    
    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively sort the remaining n-1 elements
    return bubble_sort_recursive(arr, n - 1)

def bubble_sort_with_comparison_count(arr):
    """Bubble sort with comparison and swap counting"""
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps

def bubble_sort_visualization(arr):
    """Bubble sort with step-by-step visualization"""
    n = len(arr)
    print(f"Original array: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swap {arr[j+1]} and {arr[j]}: {arr}")
        
        if not swapped:
            print("  No swaps needed - array is sorted!")
            break
    
    return arr

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
    
    print("Bubble Sort Algorithm Analysis")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        original = arr.copy()
        
        # Test basic bubble sort
        result_basic = bubble_sort_basic(arr.copy())
        print(f"Basic: {result_basic}")
        
        # Test optimized bubble sort
        result_opt = bubble_sort_optimized(arr.copy())
        print(f"Optimized: {result_opt}")
        
        # Test recursive bubble sort
        result_rec = bubble_sort_recursive(arr.copy())
        print(f"Recursive: {result_rec}")
        
        # Test with comparison counting
        result_count, comps, swaps = bubble_sort_with_comparison_count(arr.copy())
        print(f"Comparisons: {comps}, Swaps: {swaps}")
        
        # Verify sorting
        print(f"Correctly sorted: {is_sorted(result_basic)}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Comparison:")
    
    import time
    import random
    
    # Generate large test array
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    # Test basic bubble sort
    start = time.time()
    bubble_sort_basic(large_array.copy())
    basic_time = time.time() - start
    
    # Test optimized bubble sort
    start = time.time()
    bubble_sort_optimized(large_array.copy())
    opt_time = time.time() - start
    
    print(f"Basic bubble sort time: {basic_time:.6f}s")
    print(f"Optimized bubble sort time: {opt_time:.6f}s")
    print(f"Optimization improvement: {((basic_time - opt_time) / basic_time * 100):.2f}%")
    
    # Visualization example
    print("\n" + "=" * 50)
    print("Step-by-step visualization:")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_visualization(demo_array.copy()) 
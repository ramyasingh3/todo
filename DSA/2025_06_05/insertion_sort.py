# Insertion Sort Implementation
# Time Complexity: O(n²) worst/average case, O(n) best case
# Space Complexity: O(1) - in-place sorting

def insertion_sort_basic(arr):
    """Basic insertion sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def insertion_sort_with_comparison_count(arr):
    """Insertion sort with comparison and shift counting"""
    comparisons = 0
    shifts = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key
    
    return arr, comparisons, shifts

def insertion_sort_recursive(arr, n=None):
    """Recursive insertion sort implementation"""
    if n is None:
        n = len(arr)
    
    # Base case: if array has 1 element, it's sorted
    if n <= 1:
        return arr
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert last element at its correct position
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last
    return arr

def insertion_sort_visualization(arr):
    """Insertion sort with step-by-step visualization"""
    print(f"Original array: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"\nPass {i}: Inserting {key}")
        print(f"  Array before insertion: {arr[:i]} | {arr[i:]}")
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"  Array after insertion: {arr[:i+1]} | {arr[i+1:]}")
    
    return arr

def insertion_sort_binary_search(arr):
    """Insertion sort using binary search to find insertion position"""
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Find position to insert using binary search
        pos = binary_search_insertion_position(arr, 0, i - 1, key)
        
        # Shift elements to make space
        j = i - 1
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[pos] = key
    
    return arr

def binary_search_insertion_position(arr, left, right, key):
    """Binary search to find insertion position"""
    if left > right:
        return left
    
    mid = (left + right) // 2
    
    if arr[mid] == key:
        return mid + 1
    elif arr[mid] < key:
        return binary_search_insertion_position(arr, mid + 1, right, key)
    else:
        return binary_search_insertion_position(arr, left, mid - 1, key)

def insertion_sort_optimized(arr):
    """Optimized insertion sort with early termination"""
    for i in range(1, len(arr)):
        key = arr[i]
        
        # If key is already in correct position, skip
        if key >= arr[i - 1]:
            continue
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def insertion_sort_linked_list(head):
    """Insertion sort for linked list"""
    if not head or not head.next:
        return head
    
    # Initialize sorted list
    sorted_head = head
    current = head.next
    sorted_head.next = None
    
    while current:
        next_node = current.next
        
        # Insert current node into sorted list
        if current.val < sorted_head.val:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.val < current.val:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        
        current = next_node
    
    return sorted_head

def insertion_sort_partial(arr, start, end):
    """Insertion sort for a portion of the array"""
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
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
    
    print("Insertion Sort Algorithm Analysis")
    print("=" * 50)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        original = arr.copy()
        
        # Test basic insertion sort
        result_basic = insertion_sort_basic(arr.copy())
        print(f"Basic: {result_basic}")
        
        # Test with comparison counting
        result_count, comps, shifts = insertion_sort_with_comparison_count(arr.copy())
        print(f"Comparisons: {comps}, Shifts: {shifts}")
        
        # Test recursive insertion sort
        result_rec = insertion_sort_recursive(arr.copy())
        print(f"Recursive: {result_rec}")
        
        # Test binary search insertion sort
        result_binary = insertion_sort_binary_search(arr.copy())
        print(f"Binary Search: {result_binary}")
        
        # Verify sorting
        print(f"Correctly sorted: {is_sorted(result_basic)}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Comparison:")
    
    import time
    import random
    
    # Generate large test array
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    # Test basic insertion sort
    start = time.time()
    insertion_sort_basic(large_array.copy())
    basic_time = time.time() - start
    
    # Test optimized insertion sort
    start = time.time()
    insertion_sort_optimized(large_array.copy())
    opt_time = time.time() - start
    
    # Test binary search insertion sort
    start = time.time()
    insertion_sort_binary_search(large_array.copy())
    binary_time = time.time() - start
    
    print(f"Basic insertion sort time: {basic_time:.6f}s")
    print(f"Optimized insertion sort time: {opt_time:.6f}s")
    print(f"Binary search insertion sort time: {binary_time:.6f}s")
    
    # Visualization example
    print("\n" + "=" * 50)
    print("Step-by-step visualization:")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort_visualization(demo_array.copy())
    
    # Partial sorting example
    print("\n" + "=" * 50)
    print("Partial sorting example:")
    partial_array = [64, 34, 25, 12, 22, 11, 90, 45, 67, 23]
    print(f"Original: {partial_array}")
    insertion_sort_partial(partial_array, 2, 7)
    print(f"After sorting indices 2-7: {partial_array}") 
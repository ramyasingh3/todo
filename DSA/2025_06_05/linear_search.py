# Linear Search Implementation
# Time Complexity: O(n) worst/average case, O(1) best case
# Space Complexity: O(1) - constant space

def linear_search_basic(arr, target):
    """Basic linear search implementation"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_with_comparison_count(arr, target):
    """Linear search with comparison counting"""
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return -1, comparisons

def linear_search_recursive(arr, target, index=0):
    """Recursive linear search implementation"""
    # Base case: element not found
    if index >= len(arr):
        return -1
    
    # Base case: element found
    if arr[index] == target:
        return index
    
    # Recursive case: search in remaining array
    return linear_search_recursive(arr, target, index + 1)

def linear_search_sentinel(arr, target):
    """Linear search with sentinel technique"""
    n = len(arr)
    if n == 0:
        return -1
    
    # Store the last element
    last = arr[n - 1]
    
    # Set the last element as sentinel
    arr[n - 1] = target
    
    # Search for target
    i = 0
    while arr[i] != target:
        i += 1
    
    # Restore the last element
    arr[n - 1] = last
    
    # Check if target was found
    if i < n - 1 or arr[n - 1] == target:
        return i
    
    return -1

def linear_search_optimized(arr, target):
    """Optimized linear search with early termination"""
    n = len(arr)
    
    # Check first and last elements first
    if n > 0:
        if arr[0] == target:
            return 0
        if n > 1 and arr[n - 1] == target:
            return n - 1
    
    # Search from both ends
    left = 1
    right = n - 2
    
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        left += 1
        right -= 1
    
    return -1

def linear_search_multiple_occurrences(arr, target):
    """Find all occurrences of target in array"""
    occurrences = []
    
    for i in range(len(arr)):
        if arr[i] == target:
            occurrences.append(i)
    
    return occurrences

def linear_search_first_occurrence(arr, target):
    """Find first occurrence of target"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_last_occurrence(arr, target):
    """Find last occurrence of target"""
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1

def linear_search_conditional(arr, condition_func):
    """Linear search with custom condition function"""
    for i in range(len(arr)):
        if condition_func(arr[i]):
            return i
    return -1

def linear_search_range(arr, target, start, end):
    """Linear search in a specific range"""
    for i in range(start, min(end + 1, len(arr))):
        if arr[i] == target:
            return i
    return -1

def linear_search_2d_array(matrix, target):
    """Linear search in 2D array"""
    rows = len(matrix)
    if rows == 0:
        return (-1, -1)
    
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return (i, j)
    
    return (-1, -1)

def linear_search_string(text, pattern):
    """Linear search for pattern in string"""
    text_len = len(text)
    pattern_len = len(pattern)
    
    if pattern_len > text_len:
        return -1
    
    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            return i
    
    return -1

def linear_search_with_frequency(arr, target):
    """Linear search with frequency counting"""
    frequency = 0
    positions = []
    
    for i in range(len(arr)):
        if arr[i] == target:
            frequency += 1
            positions.append(i)
    
    return frequency, positions

def linear_search_approximate(arr, target, tolerance=0.1):
    """Linear search for approximate matches"""
    matches = []
    
    for i in range(len(arr)):
        if abs(arr[i] - target) <= tolerance:
            matches.append((i, arr[i]))
    
    return matches

def linear_search_visualization(arr, target):
    """Linear search with step-by-step visualization"""
    print(f"Searching for {target} in array: {arr}")
    print("=" * 50)
    
    for i in range(len(arr)):
        print(f"Step {i + 1}: Checking index {i} (value: {arr[i]})")
        
        if arr[i] == target:
            print(f"  ✓ Found {target} at index {i}!")
            return i
        else:
            print(f"  ✗ {arr[i]} != {target}, continue...")
    
    print(f"  ✗ {target} not found in array")
    return -1

def is_element_present(arr, target):
    """Check if element is present in array"""
    return linear_search_basic(arr, target) != -1

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
        [3, 3, 3, 3],
        [1, 5, 2, 8, 3, 9, 7, 4, 6]
    ]
    
    test_targets = [25, 6, 1, 10, 3, 90]
    
    print("Linear Search Algorithm Analysis")
    print("=" * 50)
    
    for arr in test_arrays:
        print(f"\nArray: {arr}")
        
        for target in test_targets:
            # Test basic linear search
            result_basic = linear_search_basic(arr, target)
            print(f"  Target {target}: Index {result_basic}")
            
            # Test with comparison counting
            result_count, comps = linear_search_with_comparison_count(arr, target)
            print(f"    Comparisons: {comps}")
            
            # Test recursive linear search
            result_rec = linear_search_recursive(arr, target)
            print(f"    Recursive: Index {result_rec}")
            
            # Test multiple occurrences
            if result_basic != -1:
                occurrences = linear_search_multiple_occurrences(arr, target)
                print(f"    All occurrences: {occurrences}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Comparison:")
    
    import time
    import random
    
    # Generate large test array
    large_array = [random.randint(1, 10000) for _ in range(10000)]
    target = random.choice(large_array)
    
    # Test basic linear search
    start = time.time()
    result = linear_search_basic(large_array, target)
    basic_time = time.time() - start
    
    # Test optimized linear search
    start = time.time()
    result_opt = linear_search_optimized(large_array, target)
    opt_time = time.time() - start
    
    # Test sentinel linear search
    start = time.time()
    result_sentinel = linear_search_sentinel(large_array.copy(), target)
    sentinel_time = time.time() - start
    
    print(f"Basic linear search time: {basic_time:.6f}s")
    print(f"Optimized linear search time: {opt_time:.6f}s")
    print(f"Sentinel linear search time: {sentinel_time:.6f}s")
    
    # Visualization example
    print("\n" + "=" * 50)
    print("Step-by-step visualization:")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    linear_search_visualization(demo_array, 25)
    
    # 2D array search example
    print("\n" + "=" * 50)
    print("2D array search example:")
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    target_2d = 7
    result_2d = linear_search_2d_array(matrix, target_2d)
    print(f"Matrix: {matrix}")
    print(f"Target {target_2d} found at: {result_2d}")
    
    # String search example
    print("\n" + "=" * 50)
    print("String search example:")
    text = "hello world programming"
    pattern = "world"
    result_str = linear_search_string(text, pattern)
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    print(f"Found at index: {result_str}")
    
    # Approximate search example
    print("\n" + "=" * 50)
    print("Approximate search example:")
    float_array = [1.1, 2.3, 3.7, 4.2, 5.8, 6.1]
    target_approx = 3.0
    tolerance = 0.5
    matches = linear_search_approximate(float_array, target_approx, tolerance)
    print(f"Array: {float_array}")
    print(f"Target: {target_approx} (tolerance: {tolerance})")
    print(f"Approximate matches: {matches}") 
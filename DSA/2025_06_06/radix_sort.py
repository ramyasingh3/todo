# Radix Sort Implementation
# Time Complexity: O(d * (n + b)), where d is number of digits, b is base
# Space Complexity: O(n + b)

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so that count[i] contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Example usage and testing
if __name__ == "__main__":
    test_arrays = [
        [170, 45, 75, 90, 802, 24, 2, 66],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [3, 3, 3, 3],
    ]
    for arr in test_arrays:
        print(f"Original: {arr}")
        sorted_arr = radix_sort(arr.copy())
        print(f"Sorted:   {sorted_arr}\n") 
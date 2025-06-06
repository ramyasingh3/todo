# Counting Sort Implementation
# Time Complexity: O(n + k) where n is array size and k is range of input
# Space Complexity: O(n + k)

def counting_sort(arr):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    
    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] so that count[i] contains actual position
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output

# Example usage and testing
if __name__ == "__main__":
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1],
        [1, 4, 1, 2, 7, 5, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [],
        [3, 3, 3, 3],
    ]
    for arr in test_arrays:
        print(f"Original: {arr}")
        sorted_arr = counting_sort(arr.copy())
        print(f"Sorted:   {sorted_arr}\n") 
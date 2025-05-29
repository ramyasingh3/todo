def max_subarray_sum(arr: list) -> tuple[int, list]:
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): Input array of integers
        
    Returns:
        tuple: (maximum sum, subarray with maximum sum)
    """
    if not arr:
        return 0, []
        
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
            
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
            
    return max_so_far, arr[start:end + 1]

# Example usage
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Maximum sum: 6, Subarray: [4, -1, 2, 1]
        [1, 2, 3, 4, 5],                  # Maximum sum: 15, Subarray: [1, 2, 3, 4, 5]
        [-1, -2, -3, -4],                 # Maximum sum: -1, Subarray: [-1]
        [2, -1, 3, -2, 4, -3],           # Maximum sum: 6, Subarray: [2, -1, 3, -2, 4]
        [0, 0, 0, 0],                     # Maximum sum: 0, Subarray: [0]
        [1],                              # Maximum sum: 1, Subarray: [1]
        [-5, -3, -1, -2],                 # Maximum sum: -1, Subarray: [-1]
        [3, -2, 5, -1, 4, -3, 2]         # Maximum sum: 9, Subarray: [3, -2, 5, -1, 4]
    ]
    
    for arr in test_arrays:
        max_sum, subarray = max_subarray_sum(arr)
        print(f"Array: {arr}")
        print(f"Maximum Sum: {max_sum}")
        print(f"Subarray: {subarray}")
        print("-" * 50) 
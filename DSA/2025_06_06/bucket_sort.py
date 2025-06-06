# Bucket Sort Implementation
# Time Complexity: O(n + k), where n is number of elements, k is number of buckets
# Space Complexity: O(n + k)

def bucket_sort(arr, bucket_size=5):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute input array values into buckets
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)
    
    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr

# Example usage and testing
if __name__ == "__main__":
    test_arrays = [
        [42, 32, 33, 52, 37, 47, 51],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [3, 3, 3, 3],
    ]
    for arr in test_arrays:
        print(f"Original: {arr}")
        sorted_arr = bucket_sort(arr.copy())
        print(f"Sorted:   {sorted_arr}\n") 
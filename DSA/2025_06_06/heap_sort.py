# Heap Sort Implementation
# Time Complexity: O(n log n)
# Space Complexity: O(1) - in-place sorting

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Example usage and testing
if __name__ == "__main__":
    test_arrays = [
        [12, 11, 13, 5, 6, 7],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [3, 3, 3, 3],
    ]
    for arr in test_arrays:
        print(f"Original: {arr}")
        sorted_arr = heap_sort(arr.copy())
        print(f"Sorted:   {sorted_arr}\n") 
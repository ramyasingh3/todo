def trap(height: list[int]) -> int:

    
    """
    Calculate how much water can be trapped after raining.
    
    Args:
        height: List of integers representing the height of bars
        
    Returns:
        Total amount of water that can be trapped
    """
    if not height:
        return 0
        
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # Calculate left max for each position
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
        
    # Calculate right max for each position
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
        
    # Calculate trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]
        
    return trapped_water

# Example usage
if __name__ == "__main__":
    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Input: {height1}")
    print(f"Output: {trap(height1)}")  # Expected: 6
    
    # Test case 2
    height2 = [4, 2, 0, 3, 2, 5]
    print(f"\nInput: {height2}")
    print(f"Output: {trap(height2)}")  # Expected: 9 
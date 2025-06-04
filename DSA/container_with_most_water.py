def max_area(height: list[int]) -> int:
    """
    Find the maximum area of water that can be contained between two vertical lines.
    
    Args:
        height: List of integers representing the height of vertical lines
        
    Returns:
        Maximum area of water that can be contained
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the current area
        current_height = min(height[left], height[right])
        current_width = right - left
        current_area = current_height * current_width
        
        # Update the maximum area
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

# Example usage
if __name__ == "__main__":
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: {height1}")
    print(f"Output: {max_area(height1)}")  # Expected: 49
    
    # Test case 2
    height2 = [1, 1]
    print(f"\nInput: {height2}")
    print(f"Output: {max_area(height2)}")  # Expected: 1 
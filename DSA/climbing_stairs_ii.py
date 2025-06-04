def climb_stairs(n: int) -> int:
    """
    Find the number of distinct ways to climb to the top of a staircase with n steps.
    You can climb either 1 or 2 steps at a time.
    
    Args:
        n: Total number of steps
        
    Returns:
        Number of distinct ways to reach the top
    """
    if n <= 2:
        return n
    
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example usage
if __name__ == "__main__":
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {climb_stairs(n1)}")  # Expected: 2
    
    # Test case 2
    n2 = 3
    print(f"\nInput: n = {n2}")
    print(f"Output: {climb_stairs(n2)}")  # Expected: 3 
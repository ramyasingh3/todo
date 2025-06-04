def climb_stairs(n: int) -> int:
    """
    Find the number of distinct ways to climb to the top of n stairs.
    You can climb either 1 or 2 steps at a time.
    
    Args:
        n: Number of stairs to climb
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
        
    # dp[i] represents ways to climb i stairs
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to climb 1 stair
    dp[2] = 2  # Two ways to climb 2 stairs (1+1 or 2)
    
    # Fill dp array
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {climb_stairs(n1)}")  # Expected: 3 (1+1+1, 1+2, 2+1)
    
    # Test case 2
    n2 = 4
    print(f"\nInput: n = {n2}")
    print(f"Output: {climb_stairs(n2)}")  # Expected: 5
    
    # Test case 3
    n3 = 1
    print(f"\nInput: n = {n3}")
    print(f"Output: {climb_stairs(n3)}")  # Expected: 1
    
    # Test case 4
    n4 = 2
    print(f"\nInput: n = {n4}")
    print(f"Output: {climb_stairs(n4)}")  # Expected: 2 
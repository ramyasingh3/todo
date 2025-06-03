def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs.
    You can climb either 1 or 2 steps at a time.
    
    Args:
        n: Number of stairs
        
    Returns:
        Number of distinct ways to climb the stairs
        
    Example:
        >>> climb_stairs(3)
        3
    """
    if n <= 2:
        return n
        
    # Initialize dp array
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # Fill dp array
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def climb_stairs_optimized(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs using constant space.
    
    Args:
        n: Number of stairs
        
    Returns:
        Number of distinct ways to climb the stairs
    """
    if n <= 2:
        return n
        
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    n1 = 3
    print("Test case 1:")
    print(f"Input: n = {n1}")
    print(f"Using DP: {climb_stairs(n1)}")
    print(f"Using optimized: {climb_stairs_optimized(n1)}")
    
    # Test case 2: Small number
    n2 = 2
    print("\nTest case 2:")
    print(f"Input: n = {n2}")
    print(f"Using DP: {climb_stairs(n2)}")
    print(f"Using optimized: {climb_stairs_optimized(n2)}")
    
    # Test case 3: Single step
    n3 = 1
    print("\nTest case 3:")
    print(f"Input: n = {n3}")
    print(f"Using DP: {climb_stairs(n3)}")
    print(f"Using optimized: {climb_stairs_optimized(n3)}")
    
    # Test case 4: Larger number
    n4 = 5
    print("\nTest case 4:")
    print(f"Input: n = {n4}")
    print(f"Using DP: {climb_stairs(n4)}")
    print(f"Using optimized: {climb_stairs_optimized(n4)}")
    
    # Test case 5: Zero steps
    n5 = 0
    print("\nTest case 5:")
    print(f"Input: n = {n5}")
    print(f"Using DP: {climb_stairs(n5)}")
    print(f"Using optimized: {climb_stairs_optimized(n5)}") 
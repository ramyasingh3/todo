def climbStairs(n: int) -> int:
    """
    Find the number of distinct ways to climb to the top of a staircase.
    You can climb either 1 or 2 steps at a time.
    
    Args:
        n: Number of steps in the staircase
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
        
    # dp[i] represents the number of ways to climb i steps
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to climb 1 step
    dp[2] = 2  # Two ways to climb 2 steps (1+1 or 2)
    
    for i in range(3, n + 1):
        # At each step, we can either:
        # 1. Take 1 step from i-1
        # 2. Take 2 steps from i-2
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {climbStairs(n1)}")  # Expected: 2 (1+1 or 2)
    
    # Test case 2
    n2 = 3
    print(f"\nInput: n = {n2}")
    print(f"Output: {climbStairs(n2)}")  # Expected: 3 (1+1+1, 1+2, or 2+1)
    
    # Test case 3
    n3 = 4
    print(f"\nInput: n = {n3}")
    print(f"Output: {climbStairs(n3)}")  # Expected: 5
    
    # Test case 4
    n4 = 1
    print(f"\nInput: n = {n4}")
    print(f"Output: {climbStairs(n4)}")  # Expected: 1 
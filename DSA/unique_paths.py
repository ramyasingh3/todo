def unique_paths(m: int, n: int) -> int:
    """
    Find the number of unique paths from top-left to bottom-right of a grid.
    You can only move right or down at any point.
    
    Args:
        m: Number of rows in the grid
        n: Number of columns in the grid
        
    Returns:
        Number of unique paths
    """
    # Create a 2D dp array where dp[i][j] represents paths to reach cell (i,j)
    dp = [[1] * n for _ in range(m)]
    
    # Fill the dp array
    for i in range(1, m):
        for j in range(1, n):
            # Paths to current cell = paths from top + paths from left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    m1, n1 = 3, 7
    print(f"Input: m = {m1}, n = {n1}")
    print(f"Output: {unique_paths(m1, n1)}")  # Expected: 28
    
    # Test case 2
    m2, n2 = 3, 2
    print(f"\nInput: m = {m2}, n = {n2}")
    print(f"Output: {unique_paths(m2, n2)}")  # Expected: 3
    
    # Test case 3
    m3, n3 = 1, 1
    print(f"\nInput: m = {m3}, n = {n3}")
    print(f"Output: {unique_paths(m3, n3)}")  # Expected: 1
    
    # Test case 4
    m4, n4 = 2, 2
    print(f"\nInput: m = {m4}, n = {n4}")
    print(f"Output: {unique_paths(m4, n4)}")  # Expected: 2 
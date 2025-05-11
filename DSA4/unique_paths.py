def uniquePaths(m: int, n: int) -> int:
    """
    Find the number of unique paths from top-left to bottom-right in a grid.
    You can only move either down or right at any point in time.
    
    Args:
        m: Number of rows
        n: Number of columns
        
    Returns:
        Number of unique paths
    """
    # Create a dp table to store number of paths for each cell
    dp = [[1] * n for _ in range(m)]
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            # Number of paths to current cell = paths from top + paths from left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[m-1][n-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    m1, n1 = 3, 7
    print(f"Input: m = {m1}, n = {n1}")
    print(f"Output: {uniquePaths(m1, n1)}")  # Expected: 28
    
    # Test case 2
    m2, n2 = 3, 2
    print(f"\nInput: m = {m2}, n = {n2}")
    print(f"Output: {uniquePaths(m2, n2)}")  # Expected: 3
    
    # Test case 3
    m3, n3 = 7, 3
    print(f"\nInput: m = {m3}, n = {n3}")
    print(f"Output: {uniquePaths(m3, n3)}")  # Expected: 28
    
    # Test case 4
    m4, n4 = 3, 3
    print(f"\nInput: m = {m4}, n = {n4}")
    print(f"Output: {uniquePaths(m4, n4)}")  # Expected: 6 
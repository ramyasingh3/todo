def unique_paths(m: int, n: int) -> int:
    """
    Find the number of unique paths from the top-left to the bottom-right of an m x n grid.
    You can only move either down or right at any point in time.
    
    Args:
        m: Number of rows
        n: Number of columns
        
    Returns:
        Number of unique paths
    """
    # Initialize a 2D dp array with 1s for the first row and first column
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
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
def min_path_sum(grid: list[list[int]]) -> int:
    """
    Find the path from top left to bottom right which minimizes the sum of all numbers along its path.
    You can only move either down or right at any point in time.
    
    Args:
        grid: 2D grid of non-negative numbers
        
    Returns:
        Minimum sum of the path
    """
    if not grid or not grid[0]:
        return 0
        
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Initialize first cell
    dp[0][0] = grid[0][0]
    
    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(f"Input: grid = {grid1}")
    print(f"Output: {min_path_sum(grid1)}")  # Expected: 7 (1→3→1→1→1)
    
    # Test case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(f"\nInput: grid = {grid2}")
    print(f"Output: {min_path_sum(grid2)}")  # Expected: 12 (1→2→3→6)
    
    # Test case 3
    grid3 = [
        [1, 2],
        [3, 4]
    ]
    print(f"\nInput: grid = {grid3}")
    print(f"Output: {min_path_sum(grid3)}")  # Expected: 7 (1→2→4) 
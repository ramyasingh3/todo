def minPathSum(grid: list[list[int]]) -> int:
    """
    Find the path from top-left to bottom-right which minimizes the sum of all numbers along its path.
    You can only move either down or right at any point in time.
    
    Args:
        grid: 2D grid of non-negative numbers
        
    Returns:
        Minimum sum of the path
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    
    # Create a dp table to store minimum path sum for each cell
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    
    # Fill first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    # Fill first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        
    # Fill rest of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[rows-1][cols-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(f"Input: {grid1}")
    print(f"Output: {minPathSum(grid1)}")  # Expected: 7 (1→3→1→1→1)
    
    # Test case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(f"\nInput: {grid2}")
    print(f"Output: {minPathSum(grid2)}")  # Expected: 12 (1→2→3→6)
    
    # Test case 3
    grid3 = [
        [1, 2],
        [1, 1]
    ]
    print(f"\nInput: {grid3}")
    print(f"Output: {minPathSum(grid3)}")  # Expected: 3 (1→2→1) 
def numIslands(grid: list[list[str]]) -> int:
    """
    Count the number of islands in a 2D grid.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    
    Args:
        grid: 2D grid where '1' represents land and '0' represents water
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r: int, c: int) -> None:
        # Check if current position is valid and is land
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
            
        # Mark current land as visited
        grid[r][c] = '#'
        
        # Explore all four directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left
    
    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
                
    return count

# Example usage
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Input: {grid1}")
    print(f"Output: {numIslands(grid1)}")  # Expected: 1
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"\nInput: {grid2}")
    print(f"Output: {numIslands(grid2)}")  # Expected: 3
    
    # Test case 3
    grid3 = [
        ["1","0","1","0","1"],
        ["0","1","0","1","0"],
        ["1","0","1","0","1"]
    ]
    print(f"\nInput: {grid3}")
    print(f"Output: {numIslands(grid3)}")  # Expected: 7 
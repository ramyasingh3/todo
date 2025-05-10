"""
Word Search

Problem:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Explanation: The word "ABCCED" can be found in the grid as shown.

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Explanation: The word "SEE" can be found in the grid as shown.

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Explanation: The word "ABCB" cannot be found in the grid.

Time Complexity: O(m * n * 4^L) where m and n are grid dimensions and L is word length
Space Complexity: O(L) for the recursion stack
"""

def exist(board: list[list[str]], word: str) -> bool:
    """
    Check if the word exists in the board by connecting adjacent characters.
    
    Args:
        board: 2D list of characters
        word: Word to search for
        
    Returns:
        True if word exists, False otherwise
    """
    if not board or not word:
        return False
        
    rows, cols = len(board), len(board[0])
    
    def dfs(r: int, c: int, index: int) -> bool:
        # If we've found all characters in the word
        if index == len(word):
            return True
            
        # Check if current position is valid
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] != word[index]):
            return False
            
        # Mark current cell as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Check all four directions
        found = (dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or dfs(r, c-1, index+1))
                
        # Restore the cell
        board[r][c] = temp
        
        return found
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
                
    return False

# Example usage
if __name__ == "__main__":
    # Test case 1
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word1 = "ABCCED"
    print(f"Input: board = {board1}, word = {word1}")
    print(f"Output: {exist(board1, word1)}")  # Expected: True
    
    # Test case 2
    board2 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word2 = "SEE"
    print(f"\nInput: board = {board2}, word = {word2}")
    print(f"Output: {exist(board2, word2)}")  # Expected: True
    
    # Test case 3
    board3 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word3 = "ABCB"
    print(f"\nInput: board = {board3}, word = {word3}")
    print(f"Output: {exist(board3, word3)}")  # Expected: False

    # Test case 4: Empty board
    assert exist([], "A") == False
    
    # Test case 5: Empty word
    assert exist([["A"]], "") == False
    
    # Test case 6: Single cell
    assert exist([["A"]], "A") == True
    
    # Test case 7: Word longer than grid
    board4 = [["A"]]
    assert exist(board4, "AB") == False
    
    print("All test cases passed!") 
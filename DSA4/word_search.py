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
    if not board or not word:
        return False
    
    m, n = len(board), len(board[0])
    
    def dfs(i: int, j: int, word_index: int) -> bool:
        # Base case: found the word
        if word_index == len(word):
            return True
        
        # Check boundaries and character match
        if (i < 0 or i >= m or j < 0 or j >= n or 
            board[i][j] != word[word_index]):
            return False
        
        # Mark current cell as visited
        temp = board[i][j]
        board[i][j] = '#'
        
        # Try all four directions
        found = (dfs(i + 1, j, word_index + 1) or
                dfs(i - 1, j, word_index + 1) or
                dfs(i, j + 1, word_index + 1) or
                dfs(i, j - 1, word_index + 1))
        
        # Restore the cell
        board[i][j] = temp
        
        return found
    
    # Try starting from each cell
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    
    return False

# Test cases
def test_word_search():
    # Test case 1: Basic case
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert exist(board1, "ABCCED") == True
    
    # Test case 2: Word exists
    board2 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert exist(board2, "SEE") == True
    
    # Test case 3: Word doesn't exist
    board3 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert exist(board3, "ABCB") == False
    
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

if __name__ == "__main__":
    test_word_search() 
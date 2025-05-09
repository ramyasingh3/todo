# Word Search

## Problem Description
Given an m x n grid of characters `board` and a string `word`, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples

### Example 1:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Explanation: The word "ABCCED" can be found in the grid as shown.
```

### Example 2:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Explanation: The word "SEE" can be found in the grid as shown.
```

### Example 3:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Explanation: The word "ABCB" cannot be found in the grid.
```

## Solution Approach

The solution uses Depth-First Search (DFS) with backtracking:

1. For each cell in the grid:
   - Start DFS from that cell
   - Try to match the word character by character
   - Mark visited cells to avoid reuse
   - Backtrack when a path doesn't lead to the word

2. DFS function:
   - Base case: found the word (word_index == len(word))
   - Check boundaries and character match
   - Mark current cell as visited
   - Try all four directions (up, down, left, right)
   - Restore the cell (backtrack)
   - Return true if any path leads to the word

The key insights are:
- Use DFS to explore all possible paths
- Mark visited cells to avoid cycles
- Backtrack to try different paths
- Start DFS from each cell in the grid

## Time and Space Complexity

- **Time Complexity**: O(m * n * 4^L)
  - m and n are grid dimensions
  - L is the length of the word
  - For each cell, we explore up to 4 directions
  - In worst case, we explore all possible paths

- **Space Complexity**: O(L)
  - L is the length of the word
  - This is the space needed for the recursion stack
  - We modify the board in-place to mark visited cells

## Edge Cases

1. Empty board
2. Empty word
3. Single cell grid
4. Word longer than grid
5. Word not in grid
6. Word with repeated characters
7. Word that requires backtracking

## Implementation Notes

- The solution uses in-place modification of the board to mark visited cells
- The solution handles all edge cases correctly
- The solution is case-sensitive
- The solution can be modified to find all occurrences of the word
- The solution can be extended to support diagonal movements

## Alternative Approaches

1. **BFS Approach**:
   - Use BFS to find the word
   - Keep track of visited cells
   - Time Complexity: O(m * n * 4^L)
   - Space Complexity: O(m * n)
   - Less efficient for this problem

2. **Trie-based Approach**:
   - Build a trie from the dictionary
   - Search multiple words simultaneously
   - Time Complexity: O(m * n * 4^L)
   - Space Complexity: O(L * W) where W is number of words
   - Better for multiple word search

3. **Dynamic Programming**:
   - Not suitable for this problem
   - Would require tracking all possible paths
   - Would be less efficient than DFS

## Common Applications
- Word games (Boggle, Word Search)
- Text recognition
- Pattern matching
- Game development
- Natural language processing
- Document processing
- Search algorithms 
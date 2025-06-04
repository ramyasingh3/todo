"""
Find the length of the longest increasing path in a matrix.
From each cell, you can move in four directions: left, right, up, or down.
You may not move diagonally or outside the boundary.

Example 1:
Input: matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6].

Time Complexity: O(m*n) where m and n are the dimensions of the matrix
Space Complexity: O(m*n) for storing the memoization table
"""

from typing import List, Tuple
from functools import lru_cache

def longest_increasing_path_dfs(matrix: List[List[int]]) -> int:
    """
    Solution using DFS with memoization.
    For each cell, we explore all possible paths and cache the results.
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    @lru_cache(maxsize=None)
    def dfs(i: int, j: int) -> int:
        max_length = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < m and 0 <= nj < n and 
                matrix[ni][nj] > matrix[i][j]):
                max_length = max(max_length, 1 + dfs(ni, nj))
        return max_length
    
    return max(dfs(i, j) for i in range(m) for j in range(n))

def get_longest_increasing_path(matrix: List[List[int]]) -> List[int]:
    """
    Helper function to get the actual longest increasing path.
    Uses DFS with memoization to find the path.
    """
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    @lru_cache(maxsize=None)
    def dfs(i: int, j: int) -> Tuple[int, List[int]]:
        max_length = 1
        max_path = [matrix[i][j]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < m and 0 <= nj < n and 
                matrix[ni][nj] > matrix[i][j]):
                length, path = dfs(ni, nj)
                if length + 1 > max_length:
                    max_length = length + 1
                    max_path = [matrix[i][j]] + path
        
        return max_length, max_path
    
    max_length = 0
    result_path = []
    
    for i in range(m):
        for j in range(n):
            length, path = dfs(i, j)
            if length > max_length:
                max_length = length
                result_path = path
    
    return result_path

def longest_increasing_path_bfs(matrix: List[List[int]]) -> int:
    """
    Solution using BFS with topological sort.
    We start from cells with no larger neighbors and work our way up.
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Calculate outdegree for each cell
    outdegree = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and 
                    matrix[ni][nj] > matrix[i][j]):
                    outdegree[i][j] += 1
    
    # Start with cells that have no larger neighbors
    queue = [(i, j) for i in range(m) for j in range(n) if outdegree[i][j] == 0]
    max_length = 0
    
    while queue:
        max_length += 1
        next_queue = []
        for i, j in queue:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and 
                    matrix[ni][nj] < matrix[i][j]):
                    outdegree[ni][nj] -= 1
                    if outdegree[ni][nj] == 0:
                        next_queue.append((ni, nj))
        queue = next_queue
    
    return max_length

# Test cases
def test_longest_increasing_path():
    test_cases = [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4, [1, 2, 6, 9]),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4, [3, 4, 5, 6]),
        ([[]], 0, []),
        ([[1]], 1, [1]),
        ([[1, 2], [3, 4]], 4, [1, 2, 4]),
        ([[1, 2, 3], [6, 5, 4], [7, 8, 9]], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, [1]),
        ([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 5, [1, 2, 3, 4, 5]),
        ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 2, 3], [6, 5, 4], [7, 8, 9]], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]
    
    for matrix, expected_length, expected_path in test_cases:
        # Test DFS solution
        result_dfs = longest_increasing_path_dfs(matrix)
        assert result_dfs == expected_length, \
            f"DFS solution failed for {matrix}. Expected length {expected_length}, got {result_dfs}"
        
        # Test BFS solution
        result_bfs = longest_increasing_path_bfs(matrix)
        assert result_bfs == expected_length, \
            f"BFS solution failed for {matrix}. Expected length {expected_length}, got {result_bfs}"
        
        # Test path reconstruction
        result_path = get_longest_increasing_path(matrix)
        assert len(result_path) == expected_length, \
            f"Path reconstruction failed for {matrix}. Expected length {expected_length}, got {len(result_path)}"
        assert result_path == expected_path, \
            f"Path reconstruction failed for {matrix}. Expected {expected_path}, got {result_path}"
        
        print(f"Test passed for matrix={matrix}")

if __name__ == "__main__":
    test_longest_increasing_path() 
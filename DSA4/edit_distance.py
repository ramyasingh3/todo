def minDistance(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations allowed:
    1. Insert a character
    2. Delete a character
    3. Replace a character
    
    Args:
        word1: First input string
        word2: Second input string
        
    Returns:
        Minimum number of operations required
    """
    m, n = len(word1), len(word2)
    # Create a dp table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # Delete
                    dp[i][j-1] + 1,    # Insert
                    dp[i-1][j-1] + 1   # Replace
                )
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    word1_1, word2_1 = "horse", "ros"
    print(f"Input: word1 = '{word1_1}', word2 = '{word2_1}'")
    print(f"Output: {minDistance(word1_1, word2_1)}")  # Expected: 3
    
    # Test case 2
    word1_2, word2_2 = "intention", "execution"
    print(f"\nInput: word1 = '{word1_2}', word2 = '{word2_2}'")
    print(f"Output: {minDistance(word1_2, word2_2)}")  # Expected: 5
    
    # Test case 3
    word1_3, word2_3 = "abc", "abc"
    print(f"\nInput: word1 = '{word1_3}', word2 = '{word2_3}'")
    print(f"Output: {minDistance(word1_3, word2_3)}")  # Expected: 0
    
    # Test case 4
    word1_4, word2_4 = "", "abc"
    print(f"\nInput: word1 = '{word1_4}', word2 = '{word2_4}'")
    print(f"Output: {minDistance(word1_4, word2_4)}")  # Expected: 3 
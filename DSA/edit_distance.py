def min_distance(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations allowed: insert, delete, or replace a character.
    
    Args:
        word1: First string
        word2: Second string
        
    Returns:
        Minimum number of operations required
    """
    m, n = len(word1), len(word2)
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
                # Take minimum of insert, delete, or replace operation
                dp[i][j] = min(
                    dp[i][j-1] + 1,    # insert
                    dp[i-1][j] + 1,    # delete
                    dp[i-1][j-1] + 1   # replace
                )
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    word1 = "horse"
    word2 = "ros"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: {min_distance(word1, word2)}")  # Expected: 3
    
    # Test case 2
    word1 = "intention"
    word2 = "execution"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: {min_distance(word1, word2)}")  # Expected: 5
    
    # Test case 3
    word1 = "abc"
    word2 = "abc"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Output: {min_distance(word1, word2)}")  # Expected: 0 
def minDistance(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations allowed: insert, delete, or replace a character.
    
    Args:
        word1: First input string
        word2: Second input string
        
    Returns:
        Minimum number of operations required
    """
    m, n = len(word1), len(word2)
    # dp[i][j] represents the minimum operations needed to convert word1[0:i] to word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters from word2
        
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                # Take minimum of three operations:
                # 1. Replace: dp[i-1][j-1] + 1
                # 2. Delete: dp[i-1][j] + 1
                # 3. Insert: dp[i][j-1] + 1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                
    return dp[m][n]

def getOperations(word1: str, word2: str) -> list[str]:
    """
    Get the sequence of operations needed to convert word1 to word2.
    
    Args:
        word1: First input string
        word2: Second input string
        
    Returns:
        List of operations performed
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # Reconstruct operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            operations.append(f"Keep '{word1[i-1]}'")
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Delete '{word1[i-1]}'")
            i -= 1
        else:
            operations.append(f"Insert '{word2[j-1]}'")
            j -= 1
            
    return list(reversed(operations))

# Example usage
if __name__ == "__main__":
    # Test case 1
    word1 = "horse"
    word2 = "ros"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum operations: {minDistance(word1, word2)}")  # Expected: 3
    print("Operations:")
    for op in getOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 2
    word1 = "intention"
    word2 = "execution"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum operations: {minDistance(word1, word2)}")  # Expected: 5
    print("Operations:")
    for op in getOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 3
    word1 = "abc"
    word2 = "abc"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum operations: {minDistance(word1, word2)}")  # Expected: 0
    print("Operations:")
    for op in getOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 4
    word1 = ""
    word2 = "abc"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum operations: {minDistance(word1, word2)}")  # Expected: 3
    print("Operations:")
    for op in getOperations(word1, word2):
        print(f"- {op}") 
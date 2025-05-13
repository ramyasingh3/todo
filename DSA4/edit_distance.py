def minDistance(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations: insert, delete, or replace a character.
    
    Args:
        word1: First input string
        word2: Second input string
        
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
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # delete
                    dp[i][j-1] + 1,    # insert
                    dp[i-1][j-1] + 1   # replace
                )
                
    return dp[m][n]

def minDistanceMemo(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations using memoization.
    
    Args:
        word1: First input string
        word2: Second input string
        
    Returns:
        Minimum number of operations required
    """
    m, n = len(word1), len(word2)
    memo = {}
    
    def editDistance(i: int, j: int) -> int:
        if i == 0:
            return j
        if j == 0:
            return i
            
        if (i, j) in memo:
            return memo[(i, j)]
            
        if word1[i-1] == word2[j-1]:
            memo[(i, j)] = editDistance(i-1, j-1)
        else:
            memo[(i, j)] = min(
                editDistance(i-1, j) + 1,    # delete
                editDistance(i, j-1) + 1,    # insert
                editDistance(i-1, j-1) + 1   # replace
            )
            
        return memo[(i, j)]
        
    return editDistance(m, n)

def getEditOperations(word1: str, word2: str) -> list[str]:
    """
    Get the sequence of operations to convert word1 to word2.
    
    Args:
        word1: First input string
        word2: Second input string
        
    Returns:
        List of operations performed
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
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # delete
                    dp[i][j-1] + 1,    # insert
                    dp[i-1][j-1] + 1   # replace
                )
    
    # Reconstruct the operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j-1] <= dp[i-1][j] and dp[i][j-1] <= dp[i-1][j-1]):
            operations.append(f"Insert '{word2[j-1]}'")
            j -= 1
        elif i > 0 and (j == 0 or dp[i-1][j] <= dp[i][j-1] and dp[i-1][j] <= dp[i-1][j-1]):
            operations.append(f"Delete '{word1[i-1]}'")
            i -= 1
        else:
            operations.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
            i -= 1
            j -= 1
            
    return list(reversed(operations))

def getAllPossibleEdits(word: str, max_distance: int = 1) -> list[str]:
    """
    Get all possible words that can be formed by performing at most max_distance operations.
    
    Args:
        word: Input string
        max_distance: Maximum edit distance allowed
        
    Returns:
        List of all possible words
    """
    def generateEdits(word: str) -> set[str]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        
        return set(deletes + transposes + replaces + inserts)
        
    edits = {word}
    for _ in range(max_distance):
        new_edits = set()
        for w in edits:
            new_edits.update(generateEdits(w))
        edits.update(new_edits)
        
    return sorted(edits)

# Example usage
if __name__ == "__main__":
    # Test case 1
    word1 = "horse"
    word2 = "ros"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 3
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 3
    print("Edit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 2
    word1 = "intention"
    word2 = "execution"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 5
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 5
    print("Edit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 3
    word1 = "kitten"
    word2 = "sitting"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 3
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 3
    print("Edit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 4
    word = "hello"
    print(f"\nInput: word = '{word}'")
    print("All possible edits (distance = 1):")
    for edit in getAllPossibleEdits(word, 1):
        print(f"- '{edit}'") 
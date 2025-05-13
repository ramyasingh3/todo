def minDistance(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations: insert, delete, replace
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        Minimum number of operations
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
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # replace
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1       # insert
                )
                
    return dp[m][n]

def minDistanceMemo(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations using memoization.
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        Minimum number of operations
    """
    memo = {}
    
    def dp(i: int, j: int) -> int:
        if (i, j) in memo:
            return memo[(i, j)]
            
        if i == 0:
            return j
        if j == 0:
            return i
            
        if word1[i - 1] == word2[j - 1]:
            memo[(i, j)] = dp(i - 1, j - 1)
        else:
            memo[(i, j)] = min(
                dp(i - 1, j - 1) + 1,  # replace
                dp(i - 1, j) + 1,      # delete
                dp(i, j - 1) + 1       # insert
            )
            
        return memo[(i, j)]
        
    return dp(len(word1), len(word2))

def getEditOperations(word1: str, word2: str) -> list[str]:
    """
    Get the sequence of operations to convert word1 to word2.
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        List of operations
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    operations = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
        operations[i][0] = ['delete ' + word1[j] for j in range(i)]
    for j in range(n + 1):
        dp[0][j] = j
        operations[0][j] = ['insert ' + word2[k] for k in range(j)]
        
    # Fill the dp table and track operations
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                operations[i][j] = operations[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1] + 1
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                
                if replace <= delete and replace <= insert:
                    dp[i][j] = replace
                    operations[i][j] = operations[i - 1][j - 1] + [f'replace {word1[i-1]} with {word2[j-1]}']
                elif delete <= replace and delete <= insert:
                    dp[i][j] = delete
                    operations[i][j] = operations[i - 1][j] + [f'delete {word1[i-1]}']
                else:
                    dp[i][j] = insert
                    operations[i][j] = operations[i][j - 1] + [f'insert {word2[j-1]}']
                    
    return operations[m][n]

def getAllPossibleEdits(word: str, max_distance: int = 2) -> set[str]:
    """
    Get all possible words that can be formed by applying at most max_distance operations.
    
    Args:
        word: Input string
        max_distance: Maximum edit distance allowed
        
    Returns:
        Set of possible words
    """
    def get_edits(word: str) -> set[str]:
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
        for word in edits:
            new_edits.update(get_edits(word))
        edits.update(new_edits)
    return edits

# Example usage
if __name__ == "__main__":
    # Test case 1
    word1 = "horse"
    word2 = "ros"
    print(f"Input: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 3
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 3
    print("\nEdit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 2
    word1 = "intention"
    word2 = "execution"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 5
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 5
    print("\nEdit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 3
    word1 = "kitten"
    word2 = "sitting"
    print(f"\nInput: word1 = '{word1}', word2 = '{word2}'")
    print(f"Minimum distance (DP): {minDistance(word1, word2)}")  # Expected: 3
    print(f"Minimum distance (Memo): {minDistanceMemo(word1, word2)}")  # Expected: 3
    print("\nEdit operations:")
    for op in getEditOperations(word1, word2):
        print(f"- {op}")
    
    # Test case 4
    word = "hello"
    print(f"\nInput: word = '{word}'")
    print("Possible edits (distance <= 2):")
    for edit in sorted(getAllPossibleEdits(word)):
        print(f"- '{edit}'") 
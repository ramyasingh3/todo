def wordBreak(s: str, wordDict: list[str]) -> list[str]:
    """
    Find all possible word break combinations of the string.
    
    Args:
        s: Input string
        wordDict: List of valid words
        
    Returns:
        List of all possible word break combinations
    """
    def backtrack(start: int, path: list[str], result: list[str]):
        if start == len(s):
            result.append(' '.join(path))
            return
            
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                path.append(word)
                backtrack(end, path, result)
                path.pop()
                
    result = []
    backtrack(0, [], result)
    return result

def wordBreakDP(s: str, wordDict: list[str]) -> list[str]:
    """
    Find all possible word break combinations using dynamic programming.
    
    Args:
        s: Input string
        wordDict: List of valid words
        
    Returns:
        List of all possible word break combinations
    """
    n = len(s)
    dp = [[] for _ in range(n + 1)]
    dp[0] = ['']
    
    for i in range(n):
        if not dp[i]:
            continue
            
        for word in wordDict:
            if i + len(word) <= n and s[i:i+len(word)] == word:
                for prev in dp[i]:
                    if prev:
                        dp[i + len(word)].append(prev + ' ' + word)
                    else:
                        dp[i + len(word)].append(word)
                        
    return dp[n]

def wordBreakMemo(s: str, wordDict: list[str]) -> list[str]:
    """
    Find all possible word break combinations using memoization.
    
    Args:
        s: Input string
        wordDict: List of valid words
        
    Returns:
        List of all possible word break combinations
    """
    memo = {}
    
    def dfs(s: str) -> list[str]:
        if s in memo:
            return memo[s]
            
        if not s:
            return ['']
            
        result = []
        for word in wordDict:
            if s.startswith(word):
                sub_results = dfs(s[len(word):])
                for sub in sub_results:
                    if sub:
                        result.append(word + ' ' + sub)
                    else:
                        result.append(word)
                        
        memo[s] = result
        return result
        
    return dfs(s)

def getValidWordBreaks(s: str, wordDict: list[str]) -> list[list[str]]:
    """
    Get all valid word break combinations as lists of words.
    
    Args:
        s: Input string
        wordDict: List of valid words
        
    Returns:
        List of word break combinations as lists
    """
    def backtrack(start: int, path: list[str], result: list[list[str]]):
        if start == len(s):
            result.append(path[:])
            return
            
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                path.append(word)
                backtrack(end, path, result)
                path.pop()
                
    result = []
    backtrack(0, [], result)
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    print(f"Input: s = '{s1}', wordDict = {wordDict1}")
    print("Word breaks (Backtracking):")
    for combo in wordBreak(s1, wordDict1):
        print(f"- '{combo}'")
    print("\nWord breaks (DP):")
    for combo in wordBreakDP(s1, wordDict1):
        print(f"- '{combo}'")
    print("\nWord breaks (Memo):")
    for combo in wordBreakMemo(s1, wordDict1):
        print(f"- '{combo}'")
    print("\nWord breaks as lists:")
    for combo in getValidWordBreaks(s1, wordDict1):
        print(f"- {combo}")
    
    # Test case 2
    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(f"\nInput: s = '{s2}', wordDict = {wordDict2}")
    print("Word breaks (Backtracking):")
    for combo in wordBreak(s2, wordDict2):
        print(f"- '{combo}'")
    print("\nWord breaks (DP):")
    for combo in wordBreakDP(s2, wordDict2):
        print(f"- '{combo}'")
    print("\nWord breaks (Memo):")
    for combo in wordBreakMemo(s2, wordDict2):
        print(f"- '{combo}'")
    print("\nWord breaks as lists:")
    for combo in getValidWordBreaks(s2, wordDict2):
        print(f"- {combo}")
    
    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"\nInput: s = '{s3}', wordDict = {wordDict3}")
    print("Word breaks (Backtracking):")
    for combo in wordBreak(s3, wordDict3):
        print(f"- '{combo}'")
    print("\nWord breaks (DP):")
    for combo in wordBreakDP(s3, wordDict3):
        print(f"- '{combo}'")
    print("\nWord breaks (Memo):")
    for combo in wordBreakMemo(s3, wordDict3):
        print(f"- '{combo}'")
    print("\nWord breaks as lists:")
    for combo in getValidWordBreaks(s3, wordDict3):
        print(f"- {combo}")
    
    # Test case 4
    s4 = "aaaaaaaa"
    wordDict4 = ["a", "aa", "aaa", "aaaa"]
    print(f"\nInput: s = '{s4}', wordDict = {wordDict4}")
    print("Word breaks (Backtracking):")
    for combo in wordBreak(s4, wordDict4):
        print(f"- '{combo}'")
    print("\nWord breaks (DP):")
    for combo in wordBreakDP(s4, wordDict4):
        print(f"- '{combo}'")
    print("\nWord breaks (Memo):")
    for combo in wordBreakMemo(s4, wordDict4):
        print(f"- '{combo}'")
    print("\nWord breaks as lists:")
    for combo in getValidWordBreaks(s4, wordDict4):
        print(f"- {combo}") 
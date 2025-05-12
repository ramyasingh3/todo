def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Check if a string can be segmented into a space-separated sequence of dictionary words.
    
    Args:
        s: Input string to check
        wordDict: List of valid words
        
    Returns:
        True if the string can be segmented, False otherwise
    """
    n = len(s)
    # dp[i] represents if s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
                
    return dp[n]

def wordBreakWithPath(s: str, wordDict: list[str]) -> list[str]:
    """
    Find all possible ways to break the string into valid words.
    
    Args:
        s: Input string to break
        wordDict: List of valid words
        
    Returns:
        List of all possible word break combinations
    """
    def backtrack(start: int, current: list[str], result: list[str]):
        if start == len(s):
            result.append(' '.join(current))
            return
            
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                current.append(word)
                backtrack(end, current, result)
                current.pop()
                
    result = []
    backtrack(0, [], result)
    return result

def wordBreakWithMemo(s: str, wordDict: list[str]) -> bool:
    """
    Check if a string can be segmented using memoization for better performance.
    
    Args:
        s: Input string to check
        wordDict: List of valid words
        
    Returns:
        True if the string can be segmented, False otherwise
    """
    memo = {}
    
    def canBreak(s: str) -> bool:
        if s in memo:
            return memo[s]
            
        if s in wordDict:
            memo[s] = True
            return True
            
        for i in range(1, len(s)):
            if s[:i] in wordDict and canBreak(s[i:]):
                memo[s] = True
                return True
                
        memo[s] = False
        return False
        
    return canBreak(s)

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(f"Input: s = '{s1}', wordDict = {wordDict1}")
    print(f"Can be segmented: {wordBreak(s1, wordDict1)}")  # Expected: True
    print(f"Using memoization: {wordBreakWithMemo(s1, wordDict1)}")  # Expected: True
    print("All possible segmentations:")
    for path in wordBreakWithPath(s1, wordDict1):
        print(f"- {path}")
    
    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(f"\nInput: s = '{s2}', wordDict = {wordDict2}")
    print(f"Can be segmented: {wordBreak(s2, wordDict2)}")  # Expected: True
    print(f"Using memoization: {wordBreakWithMemo(s2, wordDict2)}")  # Expected: True
    print("All possible segmentations:")
    for path in wordBreakWithPath(s2, wordDict2):
        print(f"- {path}")
    
    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"\nInput: s = '{s3}', wordDict = {wordDict3}")
    print(f"Can be segmented: {wordBreak(s3, wordDict3)}")  # Expected: False
    print(f"Using memoization: {wordBreakWithMemo(s3, wordDict3)}")  # Expected: False
    print("All possible segmentations:")
    for path in wordBreakWithPath(s3, wordDict3):
        print(f"- {path}")
    
    # Test case 4
    s4 = "pineapplepenapple"
    wordDict4 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(f"\nInput: s = '{s4}', wordDict = {wordDict4}")
    print(f"Can be segmented: {wordBreak(s4, wordDict4)}")  # Expected: True
    print(f"Using memoization: {wordBreakWithMemo(s4, wordDict4)}")  # Expected: True
    print("All possible segmentations:")
    for path in wordBreakWithPath(s4, wordDict4):
        print(f"- {path}") 
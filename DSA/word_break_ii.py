def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Determine if a string can be segmented into a space-separated sequence of dictionary words.
    
    Args:
        s: Input string to check
        word_dict: List of valid words
        
    Returns:
        True if the string can be segmented, False otherwise
    """
    n = len(s)
    # dp[i] represents whether s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    # Convert word_dict to set for O(1) lookup
    word_set = set(word_dict)
    
    for i in range(1, n + 1):
        for j in range(i):
            # If s[0:j] can be segmented and s[j:i] is in word_dict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "leetcode"
    word_dict1 = ["leet", "code"]
    print(f"Input: s = '{s1}', wordDict = {word_dict1}")
    print(f"Output: {word_break(s1, word_dict1)}")  # Expected: True
    
    # Test case 2
    s2 = "applepenapple"
    word_dict2 = ["apple", "pen"]
    print(f"\nInput: s = '{s2}', wordDict = {word_dict2}")
    print(f"Output: {word_break(s2, word_dict2)}")  # Expected: True
    
    # Test case 3
    s3 = "catsandog"
    word_dict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"\nInput: s = '{s3}', wordDict = {word_dict3}")
    print(f"Output: {word_break(s3, word_dict3)}")  # Expected: False 
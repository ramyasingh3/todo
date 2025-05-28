def isMatch(s: str, p: str) -> bool:
    """
    Check if string matches the pattern using dynamic programming.
    Pattern can contain '.' for any single character and '*' for zero or more of the preceding element.
    
    Args:
        s: Input string
        p: Pattern string
        
    Returns:
        True if string matches pattern, False otherwise
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
            
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Zero occurrence
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # One or more occurrence
                    
    return dp[m][n]

def isMatchMemo(s: str, p: str) -> bool:
    """
    Check if string matches the pattern using memoization.
    
    Args:
        s: Input string
        p: Pattern string
        
    Returns:
        True if string matches pattern, False otherwise
    """
    memo = {}
    
    def dp(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
            
        if j == len(p):
            return i == len(s)
            
        first_match = i < len(s) and (p[j] == '.' or p[j] == s[i])
        
        if j + 1 < len(p) and p[j + 1] == '*':
            memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
        else:
            memo[(i, j)] = first_match and dp(i + 1, j + 1)
            
        return memo[(i, j)]
        
    return dp(0, 0)

def getAllMatches(s: str, p: str) -> list[str]:
    """
    Get all possible matches of the pattern in the string.
    
    Args:
        s: Input string
        p: Pattern string
        
    Returns:
        List of all matching substrings
    """
    def is_valid_match(sub: str, pattern: str) -> bool:
        m, n = len(sub), len(pattern)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[j - 1] == '.' or pattern[j - 1] == sub[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if pattern[j - 2] == '.' or pattern[j - 2] == sub[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
        
    matches = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_valid_match(substring, p):
                matches.append(substring)
                
    return sorted(matches, key=len)

def getPatternMatches(s: str, p: str) -> list[tuple[str, str]]:
    """
    Get all pattern matches with their corresponding substrings.
    
    Args:
        s: Input string
        p: Pattern string
        
    Returns:
        List of tuples containing (substring, matched pattern)
    """
    def get_matched_pattern(sub: str, pattern: str) -> str:
        m, n = len(sub), len(pattern)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[j - 1] == '.' or pattern[j - 1] == sub[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if pattern[j - 2] == '.' or pattern[j - 2] == sub[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        if not dp[m][n]:
            return ""
            
        # Reconstruct the matched pattern
        matched = []
        i, j = m, n
        while i > 0 and j > 0:
            if pattern[j - 1] == '.' or pattern[j - 1] == sub[i - 1]:
                matched.append(pattern[j - 1])
                i -= 1
                j -= 1
            elif pattern[j - 1] == '*':
                if dp[i][j - 2]:
                    j -= 2
                else:
                    matched.append(pattern[j - 1])
                    i -= 1
                    
        return ''.join(reversed(matched))
        
    matches = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            matched_pattern = get_matched_pattern(substring, p)
            if matched_pattern:
                matches.append((substring, matched_pattern))
                
    return sorted(matches, key=lambda x: len(x[0]))

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "aa"
    p1 = "a"
    print(f"Input: s = '{s1}', p = '{p1}'")
    print(f"Match (DP): {isMatch(s1, p1)}")  # Expected: False
    print(f"Match (Memo): {isMatchMemo(s1, p1)}")  # Expected: False
    print("\nAll matches:")
    for match in getAllMatches(s1, p1):
        print(f"- '{match}'")
    
    # Test case 2
    s2 = "aa"
    p2 = "a*"
    print(f"\nInput: s = '{s2}', p = '{p2}'")
    print(f"Match (DP): {isMatch(s2, p2)}")  # Expected: True
    print(f"Match (Memo): {isMatchMemo(s2, p2)}")  # Expected: True
    print("\nAll matches:")
    for match in getAllMatches(s2, p2):
        print(f"- '{match}'")
    
    # Test case 3
    s3 = "ab"
    p3 = ".*"
    print(f"\nInput: s = '{s3}', p = '{p3}'")
    print(f"Match (DP): {isMatch(s3, p3)}")  # Expected: True
    print(f"Match (Memo): {isMatchMemo(s3, p3)}")  # Expected: True
    print("\nPattern matches:")
    for substring, pattern in getPatternMatches(s3, p3):
        print(f"- '{substring}' matches '{pattern}'")
    
    # Test case 4
    s4 = "aab"
    p4 = "c*a*b"
    print(f"\nInput: s = '{s4}', p = '{p4}'")
    print(f"Match (DP): {isMatch(s4, p4)}")  # Expected: True
    print(f"Match (Memo): {isMatchMemo(s4, p4)}")  # Expected: True
    print("\nPattern matches:")
    for substring, pattern in getPatternMatches(s4, p4):
        print(f"- '{substring}' matches '{pattern}'") 
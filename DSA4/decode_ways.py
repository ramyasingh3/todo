def numDecodings(s: str) -> int:
    """
    Find the number of ways to decode a string of digits into letters.
    'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"
    
    Args:
        s: String containing only digits
        
    Returns:
        Number of ways to decode the string
    """
    if not s or s[0] == '0':
        return 0
        
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way to decode
    dp[1] = 1  # First character has one way to decode if not '0'
    
    for i in range(2, n + 1):
        # Check if current digit is valid
        if s[i-1] != '0':
            dp[i] += dp[i-1]
            
        # Check if current and previous digit form a valid number
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "12"
    print(f"Input: s = '{s1}'")
    print(f"Output: {numDecodings(s1)}")  # Expected: 2 ("AB" or "L")
    
    # Test case 2
    s2 = "226"
    print(f"\nInput: s = '{s2}'")
    print(f"Output: {numDecodings(s2)}")  # Expected: 3 ("BZ", "VF", or "BBF")
    
    # Test case 3
    s3 = "06"
    print(f"\nInput: s = '{s3}'")
    print(f"Output: {numDecodings(s3)}")  # Expected: 0 (no valid decoding)
    
    # Test case 4
    s4 = "27"
    print(f"\nInput: s = '{s4}'")
    print(f"Output: {numDecodings(s4)}")  # Expected: 1 ("BG") 
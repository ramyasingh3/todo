# 17_find_anagrams.py

def find_anagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    
    # Initialize character counts
    p_count = [0] * 26
    s_count = [0] * 26
    
    # Count characters in pattern
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    result = []
    # Sliding window
    for i in range(len(s)):
        # Add character to window
        s_count[ord(s[i]) - ord('a')] += 1
        
        # Remove character from window if window size exceeds pattern length
        if i >= len(p):
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        
        # Compare counts
        if i >= len(p) - 1 and s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# Example usage
if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
    print(find_anagrams("abab", "ab"))  # Output: [0, 1, 2]
    print(find_anagrams("", "a"))  # Output: []
    print(find_anagrams("a", "a"))  # Output: [0]
    print(find_anagrams("aa", "a"))  # Output: [0, 1]
    print(find_anagrams("baa", "aa"))  # Output: [1]
    print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
    print(find_anagrams("ababababab", "aab"))  # Output: [0, 2, 4, 6] 
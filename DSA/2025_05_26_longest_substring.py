# 16_longest_substring.py

def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0
    
    char_pos = {}  # Store the last position of each character
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        if char in char_pos and char_pos[char] >= start:
            start = char_pos[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        char_pos[char] = end
    
    return max_length

# Example usage
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # Output: 3
    print(length_of_longest_substring("bbbbb"))  # Output: 1
    print(length_of_longest_substring("pwwkew"))  # Output: 3
    print(length_of_longest_substring(""))  # Output: 0
    print(length_of_longest_substring("a"))  # Output: 1
    print(length_of_longest_substring("au"))  # Output: 2
    print(length_of_longest_substring("dvdf"))  # Output: 3
    print(length_of_longest_substring("anviaj"))  # Output: 5
    print(length_of_longest_substring("tmmzuxt"))  # Output: 5 
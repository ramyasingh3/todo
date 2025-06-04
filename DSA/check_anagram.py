# 05_check_anagram.py

def are_anagrams(s1: str, s2: str) -> bool:
    # Convert to lowercase and remove spaces
    s1 = ''.join(c.lower() for c in s1 if c.isalnum())
    s2 = ''.join(c.lower() for c in s2 if c.isalnum())
    
    # Check if lengths are equal
    if len(s1) != len(s2):
        return False
    
    # Count characters in both strings
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        char_count[char] = char_count.get(char, 0) - 1
    
    # Check if all counts are 0
    return all(count == 0 for count in char_count.values())

# Example usage
if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))  # Output: True
    print(are_anagrams("hello", "world"))  # Output: False
    print(are_anagrams("anagram", "nagaram"))  # Output: True
    print(are_anagrams("rat", "car"))  # Output: False
    print(are_anagrams("", ""))  # Output: True
    print(are_anagrams("a", "a"))  # Output: True
    print(are_anagrams("A man, a plan, a canal: Panama", "Panama canal: a plan, a man, A"))  # Output: True 
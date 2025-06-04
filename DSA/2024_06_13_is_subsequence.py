# 19_is_subsequence.py

def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
        if i == len(s):
            return True
    return i == len(s)

# Example usage
if __name__ == "__main__":
    print(is_subsequence("abc", "ahbgdc"))  # Output: True
    print(is_subsequence("axc", "ahbgdc"))  # Output: False
    print(is_subsequence("", "ahbgdc"))  # Output: True
    print(is_subsequence("a", "a"))  # Output: True
    print(is_subsequence("abc", "abc"))  # Output: True
    print(is_subsequence("abc", "acb"))  # Output: False
    print(is_subsequence("ace", "abcde"))  # Output: True 
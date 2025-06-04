# 15_string_rotation.py

def is_rotation(s1: str, s2: str) -> bool:
    # If lengths are different, they can't be rotations
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself and check if s2 is a substring
    return s2 in (s1 + s1)

# Example usage
if __name__ == "__main__":
    print(is_rotation("waterbottle", "erbottlewat"))  # Output: True
    print(is_rotation("python", "thonpy"))  # Output: True
    print(is_rotation("hello", "world"))  # Output: False
    print(is_rotation("", ""))  # Output: True
    print(is_rotation("a", "a"))  # Output: True
    print(is_rotation("ab", "ba"))  # Output: True
    print(is_rotation("abc", "cab"))  # Output: True
    print(is_rotation("abcd", "dabc"))  # Output: True
    print(is_rotation("rotation", "tionrota"))  # Output: True 
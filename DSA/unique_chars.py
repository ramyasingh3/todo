# 03_unique_chars.py

def has_unique_chars(s: str) -> bool:
    # Using set to check for duplicates
    return len(s) == len(set(s))

# Example usage
if __name__ == "__main__":
    print(has_unique_chars("python"))  # Output: True
    print(has_unique_chars("hello"))  # Output: False
    print(has_unique_chars("algorithm"))  # Output: False
    print(has_unique_chars("unique"))  # Output: False
    print(has_unique_chars("abcdef"))  # Output: True
    print(has_unique_chars(""))  # Output: True
    print(has_unique_chars("a"))  # Output: True
    print(has_unique_chars("aa"))  # Output: False 
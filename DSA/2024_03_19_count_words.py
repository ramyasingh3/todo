# 09_count_words.py

def count_words(s: str) -> int:
    # Handle empty string
    if not s.strip():
        return 0
    
    # Split by whitespace and filter out empty strings
    words = [word for word in s.split() if word]
    return len(words)

# Example usage
if __name__ == "__main__":
    print(count_words("Hello World"))  # Output: 2
    print(count_words("   Hello   World   "))  # Output: 2
    print(count_words(""))  # Output: 0
    print(count_words("   "))  # Output: 0
    print(count_words("Hello"))  # Output: 1
    print(count_words("Hello, World!"))  # Output: 2
    print(count_words("Multiple    spaces    between    words"))  # Output: 4
    print(count_words("NoSpacesHere"))  # Output: 1
    print(count_words("  Leading and trailing spaces  "))  # Output: 4 
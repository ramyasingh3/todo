from collections import Counter

def most_frequent_char(s: str) -> str:
    if not s:
        return ''
    count = Counter(s)
    # Return the character with the highest frequency (first in case of tie)
    return max(count, key=lambda k: (count[k], -s.index(k)))

# Example usage
if __name__ == "__main__":
    print(most_frequent_char("hello"))  # Output: 'l'
    print(most_frequent_char("aabbbcccc"))  # Output: 'c'
    print(most_frequent_char("abcabcabc"))  # Output: 'a'
    print(most_frequent_char(""))  # Output: ''
    print(most_frequent_char("z"))  # Output: 'z'
    print(most_frequent_char("mississippi"))  # Output: 'i' 
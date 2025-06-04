# 21_remove_vowels.py

def remove_vowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join(c for c in s if c not in vowels)

# Example usage
if __name__ == "__main__":
    print(remove_vowels("hello world"))  # Output: 'hll wrld'
    print(remove_vowels("AEIOUaeiou"))  # Output: ''
    print(remove_vowels("Python"))  # Output: 'Pythn'
    print(remove_vowels(""))  # Output: ''
    print(remove_vowels("abcdefghijklmnopqrstuvwxyz"))  # Output: 'bcdfghjklmnpqrstvwxyz' 
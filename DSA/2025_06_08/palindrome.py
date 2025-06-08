# Palindrome Check Implementation
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s)) 
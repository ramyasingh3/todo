def reverse_string(s):
    """
    Reverse string in-place using two pointers.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)  # ['o', 'l', 'l', 'e', 'h']

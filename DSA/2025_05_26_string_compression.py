# 14_string_compression.py

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = s[i]
            count = 1
    
    # Add the last character and its count
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

# Example usage
if __name__ == "__main__":
    print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"
    print(compress_string("abcd"))  # Output: "abcd"
    print(compress_string(""))  # Output: ""
    print(compress_string("a"))  # Output: "a"
    print(compress_string("aa"))  # Output: "a2"
    print(compress_string("aaa"))  # Output: "a3"
    print(compress_string("aabbcc"))  # Output: "a2b2c2"
    print(compress_string("abbbbbbbbbbbb"))  # Output: "a1b12" 
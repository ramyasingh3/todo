from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    result = []
    p_count = Counter(p)
    s_count = Counter()
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# Example usage
if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]

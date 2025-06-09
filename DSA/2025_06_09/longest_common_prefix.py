# Longest Common Prefix - DSA Solution

def longest_common_prefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string amongst an array of strings.
    
    Args:
        strs: List of strings
    
    Returns:
        str: Longest common prefix
    """
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    # Find the shortest string length
    min_length = min(len(s) for s in strs)
    
    # Compare characters at each position
    for i in range(min_length):
        char = strs[0][i]
        for string in strs[1:]:
            if string[i] != char:
                return strs[0][:i]
    
    return strs[0][:min_length]

def longest_common_prefix_vertical(strs: list[str]) -> str:
    """
    Find the longest common prefix using vertical scanning.
    
    Args:
        strs: List of strings
    
    Returns:
        str: Longest common prefix
    """
    if not strs:
        return ""
    
    # Sort strings to find the shortest and lexicographically smallest
    strs.sort()
    
    # Compare first and last string
    first = strs[0]
    last = strs[-1]
    
    common_prefix = ""
    min_length = min(len(first), len(last))
    
    for i in range(min_length):
        if first[i] == last[i]:
            common_prefix += first[i]
        else:
            break
    
    return common_prefix

def longest_common_prefix_binary_search(strs: list[str]) -> str:
    """
    Find the longest common prefix using binary search.
    
    Args:
        strs: List of strings
    
    Returns:
        str: Longest common prefix
    """
    if not strs:
        return ""
    
    def is_common_prefix(length):
        prefix = strs[0][:length]
        return all(s.startswith(prefix) for s in strs)
    
    # Find the minimum length
    min_length = min(len(s) for s in strs)
    
    # Binary search
    left, right = 0, min_length
    
    while left < right:
        mid = (left + right + 1) // 2
        if is_common_prefix(mid):
            left = mid
        else:
            right = mid - 1
    
    return strs[0][:left]

# Example usage
if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],           # "fl"
        ["dog", "racecar", "car"],              # ""
        ["interspecies", "interstellar", "interstate"],  # "inters"
        ["throne", "throne"],                   # "throne"
        ["", "b"],                              # ""
        ["a"],                                  # "a"
        ["aa", "a"],                            # "a"
        ["aaa", "aa", "aaa"],                   # "aa"
        ["ab", "a"],                            # "a"
        ["abc", "abc", "abc"],                  # "abc"
    ]
    
    print("Method 1 - Horizontal scanning:")
    for strs in test_cases:
        result = longest_common_prefix(strs)
        print(f"{strs} -> '{result}'")
    
    print("\nMethod 2 - Vertical scanning:")
    for strs in test_cases:
        result = longest_common_prefix_vertical(strs)
        print(f"{strs} -> '{result}'")
    
    print("\nMethod 3 - Binary search:")
    for strs in test_cases:
        result = longest_common_prefix_binary_search(strs)
        print(f"{strs} -> '{result}'") 
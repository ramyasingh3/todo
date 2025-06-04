class Solution:
    def longest_common_prefix_vertical(self, strs: list[str]) -> str:
        """
        Vertical scanning solution
        Time Complexity: O(S), where S is the sum of all characters
        Space Complexity: O(1)
        """
        if not strs:
            return ""
            
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]

    def longest_common_prefix_horizontal(self, strs: list[str]) -> str:
        """
        Horizontal scanning solution
        Time Complexity: O(S), where S is the sum of all characters
        Space Complexity: O(1)
        """
        if not strs:
            return ""
            
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix

    def longest_common_prefix_divide(self, strs: list[str]) -> str:
        """
        Divide and conquer solution
        Time Complexity: O(S), where S is the sum of all characters
        Space Complexity: O(m log n), where m is the length of the longest string
        """
        def common_prefix(left: str, right: str) -> str:
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]
            
        def divide_and_conquer(strs: list[str], left: int, right: int) -> str:
            if left == right:
                return strs[left]
                
            mid = (left + right) // 2
            lcp_left = divide_and_conquer(strs, left, mid)
            lcp_right = divide_and_conquer(strs, mid + 1, right)
            return common_prefix(lcp_left, lcp_right)
            
        if not strs:
            return ""
            
        return divide_and_conquer(strs, 0, len(strs) - 1)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Common prefix exists
    print("Test Case 1: Common prefix exists")
    strs = ["flower", "flow", "flight"]
    result = solution.longest_common_prefix_vertical(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: No common prefix
    print("Test Case 2: No common prefix")
    strs = ["dog", "racecar", "car"]
    result = solution.longest_common_prefix_vertical(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Empty array
    print("Test Case 3: Empty array")
    strs = []
    result = solution.longest_common_prefix_vertical(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Single string
    print("Test Case 4: Single string")
    strs = ["a"]
    result = solution.longest_common_prefix_vertical(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: All strings same
    print("Test Case 5: All strings same")
    strs = ["abc", "abc", "abc"]
    result = solution.longest_common_prefix_vertical(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    strs = ["flower", "flow", "flight"]
    print(f"Input: {strs}")
    print(f"Vertical method: {solution.longest_common_prefix_vertical(strs)}")
    print(f"Horizontal method: {solution.longest_common_prefix_horizontal(strs)}")
    print(f"Divide and conquer method: {solution.longest_common_prefix_divide(strs)}")

def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    # Find the shortest string
    shortest = min(strs, key=len)
    
    # Check each character position
    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                return shortest[:i]
    
    return shortest

if __name__ == "__main__":
    test_solution()
    
    # Test cases
    test_cases = [
        ["flower", "flow", "flight"],  # Expected: "fl"
        ["dog", "racecar", "car"],     # Expected: ""
        ["interspecies", "interstellar", "interstate"],  # Expected: "inters"
        ["prefix", "preface", "prelude"],  # Expected: "pre"
        ["", "b"],  # Expected: ""
        ["a"],  # Expected: "a"
        ["", ""],  # Expected: ""
    ]
    
    for test in test_cases:
        result = longest_common_prefix(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n")

    # Example usage
    print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""
    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
    print(longest_common_prefix(["python", "pythonic", "pytorch"]))  # Output: "pyt"
    print(longest_common_prefix(["", "b"]))  # Output: ""
    print(longest_common_prefix(["a"]))  # Output: "a"
    print(longest_common_prefix([]))  # Output: ""
    print(longest_common_prefix(["same", "same", "same"]))  # Output: "same" 
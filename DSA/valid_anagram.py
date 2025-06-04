class Solution:
    def is_anagram_sort(self, s: str, t: str) -> bool:
        """
        Sorting solution
        Time Complexity: O(n log n)
        Space Complexity: O(1) or O(n) depending on sorting implementation
        """
        return sorted(s) == sorted(t)

    def is_anagram_counter(self, s: str, t: str) -> bool:
        """
        Counter solution
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed number of characters
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def is_anagram_array(self, s: str, t: str) -> bool:
        """
        Array-based solution
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed size array
        """
        if len(s) != len(t):
            return False
            
        count = [0] * 26  # Assuming only lowercase English letters
        
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        for char in t:
            count[ord(char) - ord('a')] -= 1
            if count[ord(char) - ord('a')] < 0:
                return False
                
        return True

def test_solution():
    solution = Solution()
    
    # Test Case 1: Valid anagram
    print("Test Case 1: Valid anagram")
    s = "anagram"
    t = "nagaram"
    result = solution.is_anagram_sort(s, t)
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Not an anagram
    print("Test Case 2: Not an anagram")
    s = "rat"
    t = "car"
    result = solution.is_anagram_sort(s, t)
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Different lengths
    print("Test Case 3: Different lengths")
    s = "a"
    t = "ab"
    result = solution.is_anagram_sort(s, t)
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Empty strings
    print("Test Case 4: Empty strings")
    s = ""
    t = ""
    result = solution.is_anagram_sort(s, t)
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Same string
    print("Test Case 5: Same string")
    s = "hello"
    t = "hello"
    result = solution.is_anagram_sort(s, t)
    print(f"Input: s = {s}, t = {t}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    s = "anagram"
    t = "nagaram"
    print(f"Input: s = {s}, t = {t}")
    print(f"Sort method: {solution.is_anagram_sort(s, t)}")
    print(f"Counter method: {solution.is_anagram_counter(s, t)}")
    print(f"Array method: {solution.is_anagram_array(s, t)}")

if __name__ == "__main__":
    test_solution() 
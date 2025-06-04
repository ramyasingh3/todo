from collections import defaultdict
from typing import List, Dict

class Solution:
    def group_anagrams_sort(self, strs: List[str]) -> List[List[str]]:
        """
        Sorting solution with O(n * k log k) time complexity.
        Groups strings by their sorted characters.
        n is the number of strings, k is the maximum length of a string.
        """
        groups: Dict[str, List[str]] = defaultdict(list)
        
        for s in strs:
            # Sort characters to create key
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())

    def group_anagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Character counting solution with O(n * k) time complexity.
        Uses character counts as keys.
        n is the number of strings, k is the maximum length of a string.
        """
        groups: Dict[tuple, List[str]] = defaultdict(list)
        
        for s in strs:
            # Create count array for each character
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert count array to tuple for hashable key
            key = tuple(count)
            groups[key].append(s)
        
        return list(groups.values())

    def group_anagrams_prime(self, strs: List[str]) -> List[List[str]]:
        """
        Prime number solution with O(n * k) time complexity.
        Uses product of prime numbers as key.
        n is the number of strings, k is the maximum length of a string.
        """
        # First 26 prime numbers for a-z
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        groups: Dict[int, List[str]] = defaultdict(list)
        
        for s in strs:
            # Calculate product of primes
            key = 1
            for char in s:
                key *= primes[ord(char) - ord('a')]
            groups[key].append(s)
        
        return list(groups.values())

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Test Case 1:")
    print(f"Input: {strs1}")
    print(f"Sort: {solution.group_anagrams_sort(strs1)}")
    print(f"Count: {solution.group_anagrams_count(strs1)}")
    print(f"Prime: {solution.group_anagrams_prime(strs1)}")
    print()
    
    # Test Case 2: Empty strings
    strs2 = [""]
    print("Test Case 2:")
    print(f"Input: {strs2}")
    print(f"Sort: {solution.group_anagrams_sort(strs2)}")
    print(f"Count: {solution.group_anagrams_count(strs2)}")
    print(f"Prime: {solution.group_anagrams_prime(strs2)}")
    print()
    
    # Test Case 3: Single character strings
    strs3 = ["a", "b", "a"]
    print("Test Case 3:")
    print(f"Input: {strs3}")
    print(f"Sort: {solution.group_anagrams_sort(strs3)}")
    print(f"Count: {solution.group_anagrams_count(strs3)}")
    print(f"Prime: {solution.group_anagrams_prime(strs3)}")
    print()
    
    # Test Case 4: No anagrams
    strs4 = ["dog", "cat", "pig"]
    print("Test Case 4:")
    print(f"Input: {strs4}")
    print(f"Sort: {solution.group_anagrams_sort(strs4)}")
    print(f"Count: {solution.group_anagrams_count(strs4)}")
    print(f"Prime: {solution.group_anagrams_prime(strs4)}")
    print()
    
    # Test Case 5: Multiple groups
    strs5 = ["abc", "bca", "xyz", "zyx", "def"]
    print("Test Case 5:")
    print(f"Input: {strs5}")
    print(f"Sort: {solution.group_anagrams_sort(strs5)}")
    print(f"Count: {solution.group_anagrams_count(strs5)}")
    print(f"Prime: {solution.group_anagrams_prime(strs5)}")

if __name__ == "__main__":
    test_solution() 
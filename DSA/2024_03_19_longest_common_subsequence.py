# 11_longest_common_subsequence.py

def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))  # Output: 3
    print(longest_common_subsequence("abc", "abc"))  # Output: 3
    print(longest_common_subsequence("abc", "def"))  # Output: 0
    print(longest_common_subsequence("", ""))  # Output: 0
    print(longest_common_subsequence("a", "a"))  # Output: 1
    print(longest_common_subsequence("abcde", "ace"))  # Output: 3
    print(longest_common_subsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))  # Output: 4
    print(longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy"))  # Output: 2 
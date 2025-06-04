from collections import Counter

def sum_of_unique(nums: list[int]) -> int:
    freq = Counter(nums)
    return sum(num for num, count in freq.items() if count == 1)

# Example usage
if __name__ == "__main__":
    print(sum_of_unique([1, 2, 3, 2]))  # Output: 4
    print(sum_of_unique([1, 1, 1, 1]))  # Output: 0

"""
Coin Change

Problem:
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money. Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount 3 cannot be made up using only coins of denomination 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins are needed to make up amount 0.

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount) for the dp array
"""

def coin_change(coins: list[int], amount: int) -> int:
    # Initialize dp array with amount + 1 (which is greater than any possible answer)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # For each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:  # Only consider coins that are less than or equal to current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return -1 if amount cannot be made up
    return dp[amount] if dp[amount] <= amount else -1

# Test cases
def test_coin_change():
    # Test case 1: Basic case
    assert coin_change([1, 2, 5], 11) == 3
    
    # Test case 2: Impossible amount
    assert coin_change([2], 3) == -1
    
    # Test case 3: Zero amount
    assert coin_change([1], 0) == 0
    
    # Test case 4: Single coin type
    assert coin_change([1], 5) == 5
    
    # Test case 5: Multiple coin types
    assert coin_change([1, 3, 4], 6) == 2
    
    # Test case 6: Large amount
    assert coin_change([1, 2, 5], 100) == 20
    
    # Test case 7: Empty coins array
    assert coin_change([], 5) == -1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_coin_change() 
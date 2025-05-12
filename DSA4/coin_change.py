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

def coinChange(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the given amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make up
        
    Returns:
        Minimum number of coins needed, or -1 if impossible
    """
    if amount == 0:
        return 0
        
    # dp[i] represents the minimum number of coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1

def coinChangeWays(coins: list[int], amount: int) -> int:
    """
    Find the number of different ways to make up the given amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make up
        
    Returns:
        Number of different combinations to make up the amount
    """
    if amount == 0:
        return 1
        
    # dp[i] represents the number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            
    return dp[amount]

def getCoinCombinations(coins: list[int], amount: int) -> list[list[int]]:
    """
    Get all possible combinations of coins that sum up to the given amount.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make up
        
    Returns:
        List of all possible coin combinations
    """
    def backtrack(remaining: int, start: int, current: list[int], result: list[list[int]]):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
            
        for i in range(start, len(coins)):
            current.append(coins[i])
            backtrack(remaining - coins[i], i, current, result)
            current.pop()
            
    result = []
    backtrack(amount, 0, [], result)
    return result

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

    # Example usage
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Minimum coins needed: {coinChange(coins1, amount1)}")  # Expected: 3 (5 + 5 + 1)
    print(f"Number of ways: {coinChangeWays(coins1, amount1)}")  # Expected: 11
    print("All combinations:")
    for combo in getCoinCombinations(coins1, amount1):
        print(f"- {combo}")
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"\nInput: coins = {coins2}, amount = {amount2}")
    print(f"Minimum coins needed: {coinChange(coins2, amount2)}")  # Expected: -1 (impossible)
    print(f"Number of ways: {coinChangeWays(coins2, amount2)}")  # Expected: 0
    print("All combinations:")
    for combo in getCoinCombinations(coins2, amount2):
        print(f"- {combo}")
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"\nInput: coins = {coins3}, amount = {amount3}")
    print(f"Minimum coins needed: {coinChange(coins3, amount3)}")  # Expected: 0
    print(f"Number of ways: {coinChangeWays(coins3, amount3)}")  # Expected: 1
    print("All combinations:")
    for combo in getCoinCombinations(coins3, amount3):
        print(f"- {combo}")
    
    # Test case 4
    coins4 = [1, 2, 3]
    amount4 = 4
    print(f"\nInput: coins = {coins4}, amount = {amount4}")
    print(f"Minimum coins needed: {coinChange(coins4, amount4)}")  # Expected: 2 (2 + 2)
    print(f"Number of ways: {coinChangeWays(coins4, amount4)}")  # Expected: 4
    print("All combinations:")
    for combo in getCoinCombinations(coins4, amount4):
        print(f"- {combo}") 
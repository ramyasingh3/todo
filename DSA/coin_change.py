def coin_change(coins, amount):
    """
    Find the fewest number of coins needed to make up the given amount.
    
    Args:
        coins (List[int]): List of coin denominations
        amount (int): Target amount
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
    """
    # Initialize DP array with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
def test_coin_change():
    # Example 1
    coins1 = [1, 2, 5]
    amount1 = 11
    assert coin_change(coins1, amount1) == 3
    
    # Example 2
    coins2 = [2]
    amount2 = 3
    assert coin_change(coins2, amount2) == -1
    
    # Example 3
    coins3 = [1]
    amount3 = 0
    assert coin_change(coins3, amount3) == 0
    
    # Additional test cases
    coins4 = [1, 3, 4, 5]
    amount4 = 7
    assert coin_change(coins4, amount4) == 2
    
    coins5 = [2, 5, 10, 20]
    amount5 = 16
    assert coin_change(coins5, amount5) == 4
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_coin_change() 
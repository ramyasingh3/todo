def coin_change_ii(coins: list[int], amount: int) -> int:
    """
    Find the number of combinations that make up the given amount using the given coins.
    Each coin can be used unlimited number of times.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make
        
    Returns:
        Number of combinations that make up the amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: one way to make amount 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

# Example usage
if __name__ == "__main__":
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 5
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {coin_change_ii(coins1, amount1)}")  # Expected: 4
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"\nInput: coins = {coins2}, amount = {amount2}")
    print(f"Output: {coin_change_ii(coins2, amount2)}")  # Expected: 0
    
    # Test case 3
    coins3 = [1, 2, 3]
    amount3 = 4
    print(f"\nInput: coins = {coins3}, amount = {amount3}")
    print(f"Output: {coin_change_ii(coins3, amount3)}")  # Expected: 4 
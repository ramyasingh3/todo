def coin_change(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the given amount.
    Each coin can be used unlimited number of times.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make
        
    Returns:
        Minimum number of coins needed, or -1 if impossible
    """
    # Initialize dp array with amount + 1 (impossible value)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Fill dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return -1 if amount cannot be made up
    return dp[amount] if dp[amount] <= amount else -1

# Example usage
if __name__ == "__main__":
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {coin_change(coins1, amount1)}")  # Expected: 3 (5 + 5 + 1)
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"\nInput: coins = {coins2}, amount = {amount2}")
    print(f"Output: {coin_change(coins2, amount2)}")  # Expected: -1
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"\nInput: coins = {coins3}, amount = {amount3}")
    print(f"Output: {coin_change(coins3, amount3)}")  # Expected: 0 
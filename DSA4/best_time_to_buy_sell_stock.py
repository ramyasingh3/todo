def maxProfit(prices: list[int]) -> int:
    """
    Find the maximum profit you can achieve by buying and selling a stock.
    You can only hold at most one share of the stock at any time.
    You can buy it then immediately sell it on the same day.
    
    Args:
        prices: List of integers representing the stock prices on each day
        
    Returns:
        Maximum profit that can be achieved
    """
    if not prices:
        return 0
        
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Calculate profit if we sell at current price
        profit = price - min_price
        # Update maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit

# Example usage
if __name__ == "__main__":
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices1}")
    print(f"Output: {maxProfit(prices1)}")  # Expected: 5 (buy at 1, sell at 6)
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"\nInput: {prices2}")
    print(f"Output: {maxProfit(prices2)}")  # Expected: 0 (no profit possible)
    
    # Test case 3
    prices3 = [1, 2, 3, 4, 5]
    print(f"\nInput: {prices3}")
    print(f"Output: {maxProfit(prices3)}")  # Expected: 4 (buy at 1, sell at 5)
    
    # Test case 4
    prices4 = [2, 4, 1]
    print(f"\nInput: {prices4}")
    print(f"Output: {maxProfit(prices4)}")  # Expected: 2 (buy at 2, sell at 4) 
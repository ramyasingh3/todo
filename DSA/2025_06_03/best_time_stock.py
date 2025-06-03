from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit from buying and selling stock.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit possible
        
    Example:
        >>> max_profit([7, 1, 5, 3, 6, 4])
        5
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

def max_profit_multiple_transactions(prices: List[int]) -> int:
    """
    Find the maximum profit from buying and selling stock with multiple transactions.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit possible with multiple transactions
    """
    if not prices:
        return 0
        
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Test case 1:")
    print(f"Input: prices = {prices1}")
    print(f"Single transaction: {max_profit(prices1)}")
    print(f"Multiple transactions: {max_profit_multiple_transactions(prices1)}")
    
    # Test case 2: No profit possible
    prices2 = [7, 6, 4, 3, 1]
    print("\nTest case 2:")
    print(f"Input: prices = {prices2}")
    print(f"Single transaction: {max_profit(prices2)}")
    print(f"Multiple transactions: {max_profit_multiple_transactions(prices2)}")
    
    # Test case 3: Single price
    prices3 = [1]
    print("\nTest case 3:")
    print(f"Input: prices = {prices3}")
    print(f"Single transaction: {max_profit(prices3)}")
    print(f"Multiple transactions: {max_profit_multiple_transactions(prices3)}")
    
    # Test case 4: Empty list
    prices4 = []
    print("\nTest case 4:")
    print(f"Input: prices = {prices4}")
    print(f"Single transaction: {max_profit(prices4)}")
    print(f"Multiple transactions: {max_profit_multiple_transactions(prices4)}")
    
    # Test case 5: Multiple peaks
    prices5 = [3, 2, 6, 5, 0, 3]
    print("\nTest case 5:")
    print(f"Input: prices = {prices5}")
    print(f"Single transaction: {max_profit(prices5)}")
    print(f"Multiple transactions: {max_profit_multiple_transactions(prices5)}") 
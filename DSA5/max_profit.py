def max_profit(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing 
    a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

# Test cases
if __name__ == "__main__":
    # Test 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices1}")
    print(f"Output: {max_profit(prices1)}")  # Expected: 5
    
    # Test 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"\nInput: {prices2}")
    print(f"Output: {max_profit(prices2)}")  # Expected: 0
    
    # Test 3
    prices3 = [2, 4, 1]
    print(f"\nInput: {prices3}")
    print(f"Output: {max_profit(prices3)}")  # Expected: 2 
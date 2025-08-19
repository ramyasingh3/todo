def max_profit(prices):
    """
    Find maximum profit from buying and selling stock once.
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

# Test
if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5

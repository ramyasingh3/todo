# Max Profit Implementation
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices)) 
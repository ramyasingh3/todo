# Coin Change

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Examples

### Example 1:
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

### Example 2:
```
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount 3 cannot be made up using only coins of denomination 2.
```

### Example 3:
```
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins are needed to make up amount 0.
```

## Solution Approach

The solution uses dynamic programming with the following steps:

1. Create a dp array where dp[i] represents the minimum number of coins needed for amount i
2. Initialize dp[0] = 0 (base case) and all other values with amount + 1 (infinity)
3. For each amount from 1 to target:
   - Try each coin denomination
   - If the coin can be used (coin <= current amount):
     - Update dp[i] = min(dp[i], dp[i - coin] + 1)
4. Return dp[amount] if it's less than or equal to amount, else -1

The key insight is that we can build the solution by considering:
- For each amount, we can use any coin that's less than or equal to that amount
- We keep track of the minimum number of coins needed for each amount
- We can reuse coins (unbounded knapsack)

## Time and Space Complexity

- **Time Complexity**: O(amount * len(coins))
  - We process each amount once
  - For each amount, we try each coin
  - amount is the target amount
  - len(coins) is the number of different coin denominations

- **Space Complexity**: O(amount)
  - We use a dp array of size amount + 1
  - This is the space needed to store all intermediate results

## Edge Cases

1. Zero amount
2. Empty coins array
3. Single coin type
4. Impossible amount
5. Large amount
6. Multiple coin types
7. Coins with value 1

## Implementation Notes

- The solution uses a 1D array for dynamic programming
- The solution handles edge cases correctly
- The solution works with any positive integer values
- The solution efficiently computes the minimum number of coins
- The solution can be modified to return the actual coin combination

## Alternative Approaches

1. **Recursive with Memoization**:
   - Use recursion to try all possible combinations
   - Memoize results to avoid recomputation
   - Time Complexity: O(amount * len(coins))
   - Space Complexity: O(amount)
   - More intuitive but less efficient

2. **BFS Approach**:
   - Use BFS to find the shortest path to amount
   - Each node represents a current amount
   - Time Complexity: O(amount * len(coins))
   - Space Complexity: O(amount)
   - Good for finding shortest path

3. **Greedy Approach**:
   - Sort coins in descending order
   - Use largest coins first
   - Time Complexity: O(n log n)
   - Space Complexity: O(1)
   - Works only for certain coin denominations

## Common Applications
- Vending machines
- Cash registers
- Banking systems
- Payment processing
- Currency exchange
- Financial planning
- Budget allocation
- Resource optimization 
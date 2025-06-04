# Coin Change

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

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
Explanation: It's impossible to make 3 with only coin of denomination 2
```

### Example 3:
```
Input: coins = [1], amount = 0
Output: 0
```

## Approach
The solution uses dynamic programming to solve this problem efficiently. Here's how it works:

1. Create a DP array `dp` where `dp[i]` represents the minimum number of coins needed to make amount `i`
2. Initialize `dp[0] = 0` (0 coins needed to make amount 0)
3. For each amount from 1 to the target amount:
   - For each coin denomination:
     - If the coin value is less than or equal to the current amount
     - Update `dp[i]` to be the minimum of its current value and `dp[i - coin] + 1`
4. Return `dp[amount]` if it's not infinity, otherwise return -1

## Time Complexity
- O(n * m), where n is the amount and m is the number of coin denominations
- We iterate through each amount and for each amount, we check all coin denominations

## Space Complexity
- O(n), where n is the amount
- We maintain a DP array of size amount + 1

## Solution Code
The solution is implemented in `coin_change.py`. 
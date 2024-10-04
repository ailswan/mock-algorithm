from typing import List
 
#714. Best Time to Buy and Sell Stock with Transaction Fee
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
 

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
# buy 1; sell 7 => ((7 - 1) - 3) => 3
# buy 5; sell 10 => ((10 - 5) - 3) => 2

# buy 1; sell 10 => ((10 - 1) - 3) => 6
 

# Constraints:

# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104

class Solution:
    def bestTimeForStock(self, prices: List[int], fee: int) -> int:
        # dp, 2D
        # we buy the first stock
        # if we have stock on hand, 2 choices:
            # sell the stcok, or continue
        # if no stock on hand, 2 choices:
            # buy the stock or continue
        # our dp table is the length of prices
        # for each cell in dp, we can check against all previous prices to see if there was a potential buy (less the fee)
            # sell or hold or buy
            
            # sell => dp[i] = prices[i] - min(prices[0:i]) - fee
            # hold => dp[i] = dp[i - 1]
            # buy => dp[i] = price[i]
            # dp[i] = max(price[i], )

            # cash = 0
            # if stock_on_hand:
                # hold[i] = max(cash[i - 1] - price[i], hold[i - 1])
                # cash[0] = 0
                # cash[i] = max(cash[i - 1], cash[i - 1] + prices[i] - fee)                           0 ~ cash[i - 1] = 100
            # return cash[-1]
        # return the max of the dp table
        ans = 0
        # dp = [[0] * len(prices) for _ in len(prices)]


        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):


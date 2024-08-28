from typing import List

# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

class Solution:
    def getProfit(self, prices: List[int])-> int:
        #[7,1,5,3,6,4]
        # \    /\
        #  \/\/
        # 0 1 2 3 4 5
        # 5   1   6
        # only buy once and sell once
        # seperate to daily profit  get max daily profit window
        # lowest_i tracking the lowest price
        # if it is up profit += daily profit  1 2  4 5   1 + 1 + 4   cur price - lowest price
        # if it is down update max profit and reset the cur lowest_i
        lowest_i = 0
        res = 0
         #[7,1,5,3,6,4] 6
        for i in range(1, len(prices)):  #1 - 5   i = 5 lowest_i = 1
            if prices[i] < prices[lowest_i]:#  4 <  1
                lowest_i = i # lowest_i = 1
            if prices[i] > prices[i - 1]:# 4 > 6
                res = max(res, prices[i] - prices[lowest_i])# res = 0 4  4 5
        return res # 5
    # time complexity O(n)
    # space complexity O(1)
            


        

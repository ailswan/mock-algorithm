from typing import List
# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

class Solution:
    def sqrt(self, x: int) -> int:
        # brute force -> iterate through all integers and see if the squared value is less than the input
        # if the value is greater than input x, return the previous integer
        # binary search...

        # input: x = 8
        if x == 0:
            return 0

        left, right = 0, x      # l = 0, r = 8

        while left <= right:
            mid = left + (right - left) // 2        #mid = 2 + ((3 - 0) // 2) -> 2
            if mid * mid == x:                      # 1 * 1 -> 1 == 8? False
                return mid
            if mid * mid < x:                     # 1 < 8? False
                left = mid + 1                         # left = 2
            else:
                right = mid - 1                     # right = 3


        return right#left

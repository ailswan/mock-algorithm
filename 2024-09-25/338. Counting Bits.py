from typing import List

# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 6 --> 110
# 7 --> 111
# 8 --> 1000
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp and bit manipulation
        # 2 choices for dp:
            # either choose 1
            # or choose 0
    
        # find the number of places for (n + 1) --> ceil((n + 1) / 2)
        # we know for i = 0 --> 0
        # we know i = 1 --> 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
    
    0(0)        1(1)        2(10)         3(11)
    0            1            1             2
    0(0) 1(1)  2(10)  3(11) 4(100) 5(101)  6(110)  7(111)   8(1000)
    0     1     1       2      1      2       2      3          1


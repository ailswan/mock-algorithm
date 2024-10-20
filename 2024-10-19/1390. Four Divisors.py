from typing import List

# 1390. Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
# If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.


# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^5
from collections import defaultdict
class Solution:
    def fourDivisorsSum(self, nums: List[int]) -> int:
        # help give the number of and sum of divisors
        # cache {num: sum of divisors(== 4)}
        # Input: nums = [21,4,7]
        # Output: 32
        def help(num):
            s_divisors = 0
            ct = 0
            for i in range(1, num + 1):# 21  #4 # 7 
                if num % i == 0:
                    ct += 1
                    s_divisors += i
            return (ct, s_divisors) # 4, 32 # 3 7 # 2 , 8
        
        cache = defaultdict(int) #{}
        res = 0
        for n in nums:# 7
            if n in cache:
                res += cache[n]
                break
            ct, s_divisors = help(n) # 4, 32  # 3, 7 # 2,8
            print(ct, s_divisors)
            if ct == 4:
                cache[n] = s_divisors #{21: 32}
                res += s_divisors# 32 
        return res # 32
    # time complexity O(n * m) n is the len of nums , m is the largest number
    # space complexity O(n) 


solution = Solution()
nums= [21, 4, 7]
print(solution.fourDivisorsSum(nums))
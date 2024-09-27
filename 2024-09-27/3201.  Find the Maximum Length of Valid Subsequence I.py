from typing import List

#  3201. Find the Maximum Length of Valid Subsequence I

# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 4

# Explanation:

# The longest valid subsequence is [1, 2, 3, 4].

# Example 2:

# Input: nums = [1,2,1,1,2,1,2]

# Output: 6

# Explanation:

# The longest valid subsequence is [1, 2, 1, 2, 1, 2].

# Example 3:

# Input: nums = [1,3]

# Output: 2

# Explanation:

# The longest valid subsequence is [1, 3].

 

# Constraints:

# 2 <= nums.length <= 2 * 10^5
# 1 <= nums[i] <= 10^7
class Solution:
    def LongestValid(self, nums: List[int]) -> int:
        #nums = [1,2,3,4]   4   
        #subsequence  two neighbour digit sum are all even(must be all even or odd numbers) or odd(odd, even appeared one by one)
        # dp1 1,2,3,4        dp2  2 2 2 2     3 3 3 3
        #     1 0 1 0             0 0 0 0     1 1 1 1 
        #         i
        # i == even  dp1[i] = dp1[i - 1] + 1 if i - 1 == odd else 1
        #            dp2[i] = dp2[i - 1] + 1 if i - 1 == even else 1
        # i == odd   dp1[i] = dp1[i - 1] + 1 if i - 1 == even else 1
        #            dp2[i] = dp2[i - 1] + 1 if i - 1 == odd else 1

        # dp1 odd number
        # dp2 even numebr
        # i == odd   dp1[i] = max(dp2) + 1   
        # i == even  dp2[i] = max(dp1) + 1  
        max (ct_odd, ct_even, dp1[-1], dp2[-1])
 

        #max(max(dp1), max(dp2)) 
        #   [1,2,1,1,2,1,2]    
        #dp1 1 0 3 3 0 5 6       
        #dp2 0 2 0 0 4 0 0    
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        ct_odd, ct_even = 0, 0
        if nums[0] % 2:
            dp1[0] = 1
            ct_odd = 1
        else:
            dp2[0] = 1
            ct_even = 1
   
        for i in range(1, n):
            if nums[i] % 2:#odd
                ct_odd += 1
                dp1[i] = max(dp2) + 1
            else:
                dp2[i] = max(dp1) + 1
                ct_even += 1
        return max(ct_odd, ct_even, dp1[-1], dp2[-1])
            


        n = len(nums)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1,n):
            if nums[i] % 2 == 0:# even
                if nums[i - 1] % 2: # ood
                    dp1[i] = dp1[i - 1] + 1
                else: #i - 1 even
                    dp2[i] = dp2[i - 1] + 1
            else:# odd
                if nums[i - 1] % 2 == 0: # even
                    dp1[i] = dp1[i - 1] + 1
                else: # i - 1 odd
                    dp2[i] = dp2[i - 1] + 1
        return max(max(dp1), max(dp2))
    
    # time complexity O(n)
    # space complexity O(n)


# input => [1,2,1,1,2,1,2]
# output => 6



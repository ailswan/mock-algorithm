from typing import List

#  410. Split Array Largest Sum

# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.



# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= k <= min(50, nums.length)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> List[List[int]]:
        # we are to return k subarrays, so there must be k - 1 split locations
        # brute force -> try splitting at every index, see if the subarray sum is smallest
        # for a single split location, we iterate through the array and calculate the left sum and right sum
            # compare the larger sum with a largest_so_far to see if the split causes a minimized largest sum
        # if k is nums.length => return the largest element
        # dp table of length nums.length + 1
            # cells will be split index, there must be k splits
            # return the min of the last row
        # for the dp, we have 2 choices:
            # 1) we split at the index
            # 2_ don't split at the index

#dp
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        
        return f[n][m]
 

#binary search
# The approach uses a greedy algorithm to simulate the process of dividing the array.
# We traverse the array from the beginning to the end, maintaining a variable sum to represent the sum of the current subarray and a variable cnt to represent the number of subarrays that have been split so far (including the current subarray).

# Each time adding the current element to sum causes sum to exceed x (a given threshold), we consider the current element as the start of a new subarray and increment cnt by 1.

# After finishing the traversal, we check whether cnt does not exceed m (the allowed number of subarrays).

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

 
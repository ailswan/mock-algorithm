from typing import List
 
#1043. Partition Array for Maximum Sum
# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
# After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:

# Input: arr = [1,4 | 1,5,7 | 6,1,9 | 9,3], k = 4
# 10 + 28 + 27 + 18 = 
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length

class Solution:
    def partitionArr(self, arr: List[int], k: int) -> int:
        # iterate through the array, choose partition to be 2 ~ k
        # find the largest element for each potential partition
        # keep track of the max of the subarray value, after attempting all k partitions, update answer and partition pointer
        # dp, bottom-up
        # 2 choices:
            # set the partition
            # don't set partition
        #
        n = len(arr)
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            maxValue = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                d[i] = max(d[i], d[j] + maxValue * (i - j))
                if j > 0:
                    maxValue = max(maxValue, arr[j - 1])
        return d[n] 



        # Input: arr = [1,4 | 1,5,7 | 6,1,9 | 9,3], k = 4
        left = 0
        ans = 0

        if k == 1:
            return sum(arr)

        while left < len(arr):
            local_total = 0
            partition_index = left
            for i in range(2, k + 1):
                max_num = max(arr[left: left + i + 1])
                if max_num * i > local_total:
                    partition_index = left + i
                    local_total = max_num * i
            ans += local_total
            left += partition_index
        return ans
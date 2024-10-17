from typing import List

# 995. Minimum Number of K Consecutive Bit Flips

# You are given a binary array nums and an integer k.

# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [0,1,0], k = 1
# Output: 2
# Explanation: Flip nums[0], then flip nums[2].
# Example 2:

# Input: nums = [1,1,0], k = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
# Example 3:

# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
# Explanation: 
# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= k <= nums.length

# edge cases
# nums = [0, 1, 1], k = 3; output = -1
# nums = [1, 0, 1], k = 2; output = -1
# nums = [1, 0, 1, 0], k = 2; output 2
    # [1, 1, 0, 0] -> [1, 1, 1, 1]

class Solution:
    def kBitFlips(self, nums: List[int], k: int) -> int:
        # sliding window
        # check every subarray of length k, starting from 0
        # if subarray starts with 0, flip this subarray

        # Input: nums = [0,0,0,1,0,1,1,0], k = 3
        i = 0
        ans = 0
        n = len(nums)   # 8

        while i < n - k:        # i = 4; 5 < 5?
            should_flip = False
            for j in range(i, i + k + 1):       # j = 4; 4 ~ 8
                if nums[i] == 1:
                    continue
                if j == i and nums[j] != 0:
                    should_flip = True
                    nums[j] ^= 1          # nums = [1, 1, 1, 1, 1, 0, 0, 0]  <-- # nums = [1, 1, 1, 1, 0, 1, 1, 0]
                    # print("nums[j]: ", nums[j])
                elif should_flip:                                   # ^
                    nums[j] ^= 1
            if should_flip:
                ans += 1                        # ans = 2
            should_flip = False
            i += 1                              # i = 5
            print("nums: ", nums)


        for j in range(i, i + k):
            should_flip = False
            if j == i and nums[j] != 0:
                nums[j] ^= 1
                should_flip = False
            elif should_flip:
                nums[j] ^= 1
        if should_flip:
            ans += 1
        
        if 0 in nums:
            ans = -1
        return ans

class Solution:
    def kBitFlips(self, nums: List[int], k: int) -> int:       
        n = len(nums)
        flip_count = 0  # This will store the total number of flips
        ans = 0  # This stores the result (minimum number of flips)
        flipped = [0] * n  # To keep track of flips applied to each index

        for i in range(n):
            # If we are past the window of size k, revert the effect of the earlier flip
            if i >= k:
                flip_count ^= flipped[i - k]

            # If the current bit (after all previous flips) is 0, we need to flip
            if nums[i] == flip_count:  
                # If we don't have enough bits to flip a full window of size k, return -1
                if i + k > n:
                    return -1

                # Perform the flip by marking it in the `flipped` array
                flip_count ^= 1
                flipped[i] = 1
                ans += 1

        return ans
    
import collections
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = collections.deque()
        res = 0
        for i in range(n):
            if q and i >= q[0] + k:
                q.popleft()
            if len(q) % 2 == nums[i]:
                if i + k > n:
                    return - 1
                q.append(i)
                res += 1
        return res
    

test = Solution()
test.kBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3)
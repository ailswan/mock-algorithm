from typing import List

# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

class Solution:
    def rotateArray(self, nums: List[int], k: int) -> List[int]:
        # [1,2,3,4,5,6,7]  [5,6,7,1,2,3,4]
        #  5 6 74  4   1 2 3     
        #              i      j   
        
        #  5 6 7 1 2 3 5 4 4 5
        #  1 2 3  n = 3 k = 4    1
        #  1 2 3 4  n = 4 k = 2
        #  2 3 4 1
        #      ji     

     
        n = len(nums)
        k %= n
        i, j = 0, n - k
        while i < n - 1: # 7  i = 3  j = 7 0
            if i < k:
                nums[i], nums[j] = nums[j], nums[i] # 5 6 7 4 1 2 3
            else:
                
                j = n - k
                nums[i], nums[j] = nums[j], nums[i] 
            i += 1
            j += 1

# [5,6,7,1,3,4,2]
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        #1,2,3,4,5,6,7
        #1,6,7,1,2,3,4
        #      n     c  
        #p = 6
        #      count = 3
        #nums = [-1,-100,3,99], k = 2
        #     a b c d e f g    n % k == 0
        #            3  -1
        #            c
        # p = 3
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


           
         
        

from typing import List

# 11. Container with most water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

class Solution:
    def mostWater(self, height: List[int]) -> int:
        #height = [1,8,6,2,5,4,8,3,7]
        # 1,8,6,2,5,4,8,3,7
        # 0 1 2 3 4 5 6 7 8
        #   lr
        # res track most water
        # curr water 
        l, r = 0, len(height) - 1 # 0 , 8
        res = 0
        while l < r: # 1 < 1
            cur = (r - l) * min(height[l], height[r]) # 1 * 6  cur = 6
            res = max(cur, res) # res = 49
            if height[l] >= height[r]: # 8 >= 6?
                r -= 1 # r = 1
            else:
                l += 1 # l = 1
        return res
    # time complexity O(n)
    # space complexity O(1)


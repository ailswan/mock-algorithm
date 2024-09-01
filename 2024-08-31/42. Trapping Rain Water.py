from typing import List

# 42. Trapping Rain Water 

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

class Solution:
    def trapRainWater(self, height: List[int]) -> int:
        # left and right pointers to traverse the map
        # count up all the water "blocks" for each height
        # the water is calculated by the max_left or max_right less the current height
        # return total

        # Input: height = [4,2,0,3,2,5]
        
        n = len(height) # 6
        total = 0
        left_max = 0
        right_max = 0
        left, right = 0, len(n) - 1

        # 4   3 6 9  7  8
        #     l         r
        #     *
        while left < right:
            if height[left] < height[right]:            # 2 < 5? T
                left_max = max(left_max, height[left])  # left_max = max(0, 4) -> 4
                total += left_max - height[left]        # total = 4 - 4 -> 0
                left += 1                               # left = 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                right -= 1
        
        return total
# time => O(n) where n is the length of elevation map
# space => O(1)
from typing import List

# 84. Largest Histogram in Rectangle

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


# Example 1:
# https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:
# https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg

# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4

class Solution:
    def largestRectangle(self, heights: List[int]) -> int:
        #l, r
        # high  = min([l, r])
        # 2,1,5,6,2,3
        # 0 1 2 3 4 5
        #      l    r
        #            keep moving the min bar and expand l and r, updating the res
        res = 0
        n = len(heights) # 6
        for m in range(n): # 3
            l = r = m # 2
            while l >= 0 and heights[l] >= heights[m]:
                l -= 1
            while r < n and heights[r] >= heights[m]:
                r += 1
            res = max(res, heights[m] * (r - l - 1)) # res =   10
        return res
    # time complexity O(n ^2)
    # space complexity O(1)

solution = Solution()
h = [2,1,5,6,2,3]
print(solution.largestRectangle(h))
# keep moving r  , l stay in 0
# if heights[r] < heights[r + 1] : update res  l * (r - l + 1) . l = r + 1


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        # 2,1,5,6,2,3
        # 0 1 2 3 4 5
        #         i
        # [-1,1,4]
        #  res = 2 * (1 + 1 - 1) 2   (4 - 2 - 1) * 3
         # 2,3,4,5,6,1
         #[-1, 0, 1, 2, 3,4]   5
         # (n - 1) * n
          # 6  time  3 + 3 + 3 + 3 <= 2n
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area


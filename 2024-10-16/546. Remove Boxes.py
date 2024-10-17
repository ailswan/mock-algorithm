from typing import List

# 546. Remove Boxes

# You are given several boxes with different colors represented by different positive numbers.

# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

# Return the maximum points you can get.

# Example 1:

# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# Example 2:

# Input: boxes = [1,1,1]
# Output: 9
# Example 3:

# Input: boxes = [1]
# Output: 1
 

# Constraints:

# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        #[1,3,2,2,2,3,4,3,1] 
        #[1,3,2,3,2,2,4,3,1] 
        # 0 1 2 3 4 5 6 7 8
        #[1,3,3,4,3,4,1] remove 3 1 +  2 * 2 + 2 * 2 + 2 * 2 = 13  remove 4 1 + 3 * 3 + 1 + 2 * 2  = 15
        # each time move, need to keep the longest count has the possibilty to be together
        # {1: 2, 2: 3, 3: 3, 4: 1}
        # counter
        # max value 2  3
        # check if 
        # dp[i] = dp[i - 1], dp[i - k] + k * k       k same elements include i



class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # dp(i, j, k) := max score of boxes[i..j] if k boxes equal to boxes[j]
        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0

            # Check if we can reduce the sub-problem size
            while i < j and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1

            # If we have processed all the boxes, return the score
            if i == j:
                return (k+1)**2

            # Case 1: Remove the last k+1 boxes and recurse on the remaining sub-problem
            ans = (k+1)**2 + dp(i, j-1, 0)

            # Case 2: Merge boxes[j] with some box in the subarray i to j-1 and recurse on the two resulting sub-problems
            for m in range(j-1, i-1, -1):
                if boxes[m] == boxes[j]:
                    ans = max(ans, dp(i, m, k+1) + dp(m+1, j-1, 0))

            return ans

        return dp(0, len(boxes)-1, 0)

# Define the inner dp function that takes in the starting index i, ending index j, and the number of boxes k that are identical to the box at index j.
# The function returns the maximum score that can be achieved for the subarray of boxes starting at index i and ending at index j, 
# given that k boxes are identical to the box at index j.
from typing import List

# 973. K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return 
# the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:
# image URL => https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

# Constraints:

# 1 <= k <= points.length <= 10^4
# -10^4 <= xi, yi <= 10^4

from collections import heapq 
class Solution:
    def kClosestPoints(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Input: points = [[1,3],[-2,2]], k = 1
        # Output: [[-2,2]]

        # Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        # Output: [[3,3],[-2,4]]
        #        * | 
        #          |   *  
        #          |
        #  -----------------
        #          |      * 
        #          |
        # heap store distance   keep the capacity of the maxheap <= k, otherwise would pushpop()
        hq = [] 
        for i, j in points:#[[3,3],[5,-1],[-2,4]]
            distance = i ** 2 + j ** 2 # 20
            if len(hq) < k: # 2 < 2
                heapq.heappush(hq, (-distance, i, j)) #[[-18, 3, 3],[-26, 5,-1]]
            else:
                heapq.heappushpop(hq, (-distance, i, j))#[[-18, 3, 3],[-20,-2,4]]

        res = []
        for d, i, j in hq:#[[-18, 3, 3],[-20,-2,4]]
            res.append([i, j]) 
        return res#[[3, 3],[-2,4]]
    # time complexity O(n * log k)
    # space complexity O(k)
    





        



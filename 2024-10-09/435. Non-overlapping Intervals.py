from typing import List

# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4

class Solution:
    def nonOverlapping(self, intervals: List[List[int]]) -> int:
        # [[1,2],[2,3],[3,4],[1,3]]
        #  ---
        #     ---
        #        ---
        #  ------
        # sort  interval[0] if overlapping: keep the smallest end 
        intervals.sort(key = lambda x: x[0])#[[1,2],[1,3],[2,3],[3,4],]
        n = len(intervals)  # 4
        res = [intervals[0]] #[[1, 2]]
        ct = 0
        for i in range(1, n):# 3
            interval = intervals[i]
            n_s, n_e = interval[0], interval[1] #3, 4
            s, e = res[-1][0], res[-1][1]# 2, 3
            if n_s < e:# 3 < 3
                if n_e < e:# 3 < 2
                    res.pop()
                    res.append(interval)
                ct += 1# ct = 1
            else:
                res.append(interval)# [[1, 2], [2, 3], [3, 4]]
        return ct # 1
    
    #time complexity O(nlogn)
    #space complexity O(n)
                

                


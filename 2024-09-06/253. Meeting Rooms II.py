from typing import List
#  253. Meeting Rooms II


# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

# Example 3:

# Input: intervals = [[7,10],[10,14]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6

class Solution:
    def reequiredRooms(self, times: List[List[int]]) -> int:
        # sort the input based on start times
        # after sorting, we check that the start of the times[i + 1][0] time is larger than the current times[i][1] end time
            # if smaller, we increase meeting room
        
            # ----
            #   ------
            #           ----

        # when a meeting ends, the room is released, so we can keep a list of all rooms in use and their end times
        times.sort(k = lambda x: x[0])
        # rooms_in_use = { times[0][1] }
        # available = 0
        # earliest_end = times[0][1]
        h = [(0, times[0][1])]
            # r1 ----  ----  （1, 4）
            # r2   -----   -----    
            # r3 ---- -----
            # r4   ------    
            #                 
        for i in range(1, len(times)):
            if times[i][0] < h[0][1]:
                heapq.heappush(h, (len(h), times[i][1]))
            
            else:
                heapq.heappushpop(h, (len(h), times[i][1]))

        return len(h)
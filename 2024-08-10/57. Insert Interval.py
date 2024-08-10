from typing import List

#57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# [[1, --2--, 3, --5--], [6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# [[1,2],[4,5],[6,7],[8,10],[12,16]], newInterval = [3, 8]
#[1,10] [12,16]
#---   ----  ---  --- ---
#-----------------

#---      ----  ---  --- ---
#    ---

#---     ----  ---  --- ---
#  -----

#---  ----    ---  --- ---
#       -----

# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

class Solution:
  def insertInterval(self, intervals: List[int], newInterval: List[int]) -> List[int]:
    # iterate through intervals, looking at starti and starti + 1
    # compare starti with newInterval[0], to see if newInterval[0] is between starti and starti + 1
    # look at endi and endi + 1, ensure newInterval[1] is between endi and endi + 1



# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [0,8]
# Output: [[1,2],[3,10],[12,16]]

    mergedInterval = []
    start = newInterval[0][0] 
    end = newInterval[0][1]
    i = 0
     #               4-------8   new I           -----      new I     -----      new I
     #    1-----2  3-----5 6-78--10    [12,16]             ----                     ----
     #    ----------
    while i < len(intervals):
      if intervals[i][1] < newInterval[1]:
        mergedInterval.append(intervals[i])
        i += 1
        continue
      # [3,5]  [4,8]
      elif intervals[i][1] >= newInterval[0]:
        # merge
        start = min(newInterval[0], intervals[i][0])# 1
        end = max(newInterval[1], intervals[i][1])              # [...., [4, 8], ......]
      elif intervals[i][0] > end:
        mergedInterval.append([start,end])
        break
      i += 1

      mergedInterval.extend(intervals[i:])
      return mergedInterval

# time (N)
# space (1)
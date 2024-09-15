from typing import List

# 658. Find K Closest Elements

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
import bisect
from collections import deque
class Solution:
    def findKClosest(self, arr: List[int], k: int, x: int) -> List[int]:
        # Input: arr = [1,2,3,4,5], k = 4, x = 3
        #                   x
        #               2 1 0 1
        #               0 1 2 3
        # Output: [1,2,3,4]
        #binary search to find the closet one index
        # check diff left and right side  , tracking the count <= k
        # Input: arr = [1,2,3,4,5], k = 4, x = -1
        #               0 1 2 3 4
        # Output: [1,2,3,4]

        # Input: arr = [1,2], k = 1, x = 1
        #               0 1
        # Output: [1]

        # Input: arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5
        #               0 1 2 3 4 5 6|7 8 9
        # Output: [3,3,4]
        n = len(arr) # 10
        if n == 0:
            return []
        index = bisect.bisect_left(arr, x) # 7
        #if x exist in the arr bisect_left-> index of x else it works as same as bisect_right
        ct = 1
        l, r = index - 1, index + 1 # 6 ,8
   
        res = deque([arr[index]]) #[7]
        if ct == k:
            return list(res)
        while r - l <= k:#  6 >= 0 and 8 < 10? r - l <= k
            if abs(arr[l] - x) <= abs(arr[r] - x): #  2
                res.appendleft(arr[l]) # 
                l -= 1 #  
            else:
                res.append(arr[r])# [7, 7]
                r += 1 # 9 
            ct += 1 #  2
            if ct == k:
                return list(res)
        while l >= 0:# -1 >= 0
            res.appendleft(arr[l]) #  
            ct += 1 #  
            l -= 1
            if ct == k:
                return list(res) # 
        while r < n:#   1 < 2
            res.append(arr[r])#[1]
            ct += 1 # 4
            r += 1 # 4
            if ct == k:
                return list(res)
        return list(res)
            
    #time complexity O(logn + k) n the length of arr
    #space complexity O(1)
 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        # k = 1 x = 7  [1 3 8 9]
        #               0 1 2 3
        #                (l,r]
        left = bisect_left(arr, x) - 1 #1
        right = left + 1 #2

        # While the window size is less than k
        #while right - left - 1 < k:   #0 < 1                          # this while loop stops when the 2 pointers #have k elements between them
        for _ in range(k):
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]




class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
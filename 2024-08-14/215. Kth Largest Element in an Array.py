from typing import List

# 215. Kth largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap 
        # nlargest
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)
    
    #time complexity O(nlog(n))
    #space complexity O(n)
    
    

    #quick- "select"
    # recursive call to quickselect
    # XXXXXX -----S-W-A-P----- XXXXXXXXX
        #  3,2,  1   5,6,  4
        #        p         
        
        
        
        #left  <  p  < right (each element value in left side is smaller than the value of pivot)
        
        # p = 2
        # nums[p] = 1
        # mid = [1]
        # left_side_of_pivot = []
        # right_side_of_pivot = [3, 2, 5, 6, 4]
        if k <= len(left):
          # we know our ouput is in the left list
        if len(left) + len(mid) < k:
          # we know our output can be in the right list
        # just search the right side
        else:
            #search the left side

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k): # l = [3,2,5,6,4]
            pivot = random.choice(nums)
            left, mid, right = [], [], []  #k = 2
                #  3  2  5  6  4
                #        p
            for num in nums:
                if num > pivot:
                    left.append(num) # l = [6]
                elif num < pivot:
                    right.append(num)#r =[3, 2, 4]
                else:
                    mid.append(num)#m=[1, 5]
            
            if k <= len(left):# 2 <= 1?
                return quick_select(left, k) #(l, 2)
            
            if len(left) + len(mid) < k:# 1 + 2 < 2?
                return quick_select(right, k - len(left) - len(mid))
# if k <= len(right)
# if len(right) + len(mid) < k
# check current mid
            
            return pivot #5
        
        return quick_select(nums, k)
           #time comlexity O(n) averge O(n^2) worst case
           # space comlexity O(n)

class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            k = len(nums) - k 
            def quickSelect(l, r):
                pivot, p = nums[r], l
                for i in range(l, r):
                    if nums[i] <= pivot:
                        nums[p], nums[i] = nums[i], nums[p]
                        p += 1
                nums[p], nums[r] = nums[r], nums[p]

                if p > k:
                    return quickSelect(l, p - 1)
                elif p < k:
                    return quickSelect(p + 1, r)
                else:
                    return nums[p]
            return quickSelect(0, len(nums) - 1)
           #time comlexity O(n) averge O(n^2) worst case
           # space comlexity O(log n)

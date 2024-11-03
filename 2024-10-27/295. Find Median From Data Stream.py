from typing import List

# 295. Find Median from Data Stream

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
 

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

import heapq
class MedianFinder:
    def __init__(self) -> None:
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # if a stream come in [1, 2, 3]
        # left(maxheap)  1            right (minheap)  4  ct_l <= ct_r + 1  heap 
        # num > l[0] and ct_l > ct_r    add num in right  , if ct_l == ct_r : add num in right, else pop min_r to left
        #elif num <= r[0] and ct_l <= ct_r   add num in left, else: add in left  and pop max_l to right
        #left [-1]  right [2]
        if not self.left:
            heapq.heappush(self.left, -num) #[-1]
            return
        if num > -self.left[0]:# 2 > 1
            if len(self.left) > len(self.right):# 1 > 0
                heapq.heappush(self.right, num)# [2] #
            else:
                min_r = heapq.heappushpop(self.right, num)# [3]  2
                heapq.heappush(self.left, -min_r) #[-1, -2]
        else:
            if len(self.left) <= len(self.right):
                heapq.heappush(self.left, -num)
            else:
                max_l = -heapq.heappushpop(self.left, -num)
                heapq.heappush(self.right, max_l)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):# 1  1
            return float(-self.left[0]) #2
        else:
            return (-self.left[0] + self.right[0]) / 2 #(1 + 2) / 2= 1.5
        

medianFinder = MedianFinder()
print(medianFinder.addNum(1));   
print(medianFinder.addNum(2));    
print(medianFinder.findMedian());  
print(medianFinder.addNum(3));     
print(medianFinder.findMedian());  

# time complexity findMedian O(1)  addNum O(log(n/2))
# space complexity O(n)
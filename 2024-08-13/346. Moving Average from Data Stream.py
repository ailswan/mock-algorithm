from typing import List

# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 

# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

 

# Constraints:

# 1 <= size <= 1000
# -10^5 <= val <= 10^5
# At most 104 calls will be made to next.

import collections

class MovingAverage:
    
    def __init__(self, size: int):
        self.capacity = size # 3
        self.window = collections.deque([]) #[]
        self.sum = 0  #0
    #   prefix to track sum we already 
    #   track capacity to if the size is overflow
    def next(self, val: int) -> float: #[[3], [1], [10], [3], [5]]
        # need a  FIFO  queue to track the stream
        # calculate with the prefix sum in window
        if len(self.window) + 1 > self.capacity: # 4 > 3?
            d = self.window.popleft()  #[  10, 3, 5]
            self.sum -= d # 14 - 1 = 13
        self.sum += val # sum = 13 + 5 = 18
        self.window.append(val) #[10, 3, 5]
        return self.sum / len(self.window) # 18 / 3
    
    # n is the number of calls made to "next" and m is the capacity
    #time complexity O(n * m) for stream  O(1) per operation
    #space complexity O(size of window)
 




        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
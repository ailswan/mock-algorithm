from typing import List

# 1539. Kth Missing Positive Number

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
 

# Follow up:

# Could you solve this problem in less than O(n) complexity?

class Solution:
    def missingK(self, arr: List[int], k int) -> int:
        # Input: arr = [2,3,4,7,11], k = 5
        # Output: 9
        # less than O(n) . bianery search
        # 2  3  4  7 11 (1,5,6,  8 , 9 ,10) k = 7  4
        # 0  1  2  3  4
        #       l  lm r
        #if l == 0 : leftnumber = 0
        # find mid    missingLeft = arr[mid] - left number(start from 0) - (mid - l)   should be 4-0 = 4  11 - 7 = 4
        # if missingleft <= k:in the right side k - missingleft
        # if missingleft > k:  left number + k  7 + 2 
        # 2  3  4  7  11  k = 5 (1,   5, 6    8 9)
        # 0  1  2  3   4
        # l        lm   r
        #[4, 7] k = 5  (1, 2, 3    5, 6)
        # [1] k = 1 (2)

        # [1,10,21,22,25] k = 12 (2 3 4 5 6 7 8 9  11 12 13 14)
        #  0 1  2  3  4

        #    lmid r  
        # [8,11,16,20,29,30,32,33,37,39,42,44,46,47,48,50,52,56,60,63,64,65,68,70,72,74,80] k = 45
        #[1, 3] 1   2 
        if not arr:
            return k
        l, r = 0, len(arr) - 1# 0, 4
        res = 0
        if arr[l] > k:
            return k
        # if arr[l] > 1:#
        #     k = k - (arr[l] - 1)    # k = 4
        missing_right = arr[r] - (r + 1)
        if missing_right< k:
            return arr[r] + k - missing_right

        while l < r - 1:# l= 0 r = 1 k =2
            mid = (l + r) // 2  # mid = 3
            miss_ln = arr[mid] - (mid + 1) # 7 - 4 = 3
            if miss_ln < k: # 3 < 5?
                l = mid # l =  3
            else:
                r = mid
        # l r
        last_missing = arr[l]  - (l + 1)# 7 - 4 = 3
        if last_missing < k :    # 3 < 5
            res = arr[l] + (k - last_missing) #   7 + 2
        return res # 9
    #time complexity O(log n)
    #space complexity O(1)

        
#[7   10  13] k = 2

#     rl
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1  
        while left <= right:                    
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k
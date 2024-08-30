from typing import List
#1868. Product of Two Run-Length Encoded Arrays

# Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded.
# Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

# For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
# The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

# Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
# Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
# Compress prodNums into a run-length encoded array and return it.
# You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length.
# Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

# Return the product of encoded1 and encoded2.

# Note: Compression should be done such that the run-length encoded array has the minimum possible length.

# Example 1:

# Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
# Output: [[6,6]]
# Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
# prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].
# Example 2:

# Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
# Output: [[2,3],[6,1],[9,2]]
# Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
# prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].
 

# Constraints:

# 1 <= encoded1.length, encoded2.length <= 10^5
# encoded1[i].length == 2
# encoded2[j].length == 2
# 1 <= vali, freqi <= 10^4 for each encoded1[i].
# 1 <= valj, freqj <= 10^4 for each encoded2[j].
# The full arrays that encoded1 and encoded2 represent are the same length.
import collections
class Solution:
    def encode(self, e1: List[List[int]], e2: List[List[int]]) -> List[List[int]]:
        # Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
        nums1 = self.expand(e1)
        nums2 = self.expand(e2)

        product = self.multiply(nums1, nums2)

        return self.compress(product)
        
        # Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
        # Compress prodNums into a run-length encoded array and return it.


    
    def expand(self, e: List[List[int]]) -> List[int]:
        # TODO: expand the encoded lists
        nums = []
        for group in e:
            for element, freq in group:
                numbers = [element] * freq
                nums.expand(numbers)
        return nums

    def multiply(self, n1: List[int], n2: List[int]) -> List[int]:
        # TODO: perform element-by-element multiplication for prodNums
        ans = []

        for i in range(len(n1)):
            ans.append(n1[i] * n2[i])

        return ans

    def compress(self, nums: List[int]) -> List[List[int]]:
        # TODO: turn numbers into compressed form
        # iterate through nums and check if we have the same number (to be used for compression)
        # when the number is not the same as the previous element, start new grouping
        # input: [2, 2, 2, 6, 9, 9, 6, 6, 7]
        #                                 le 
        
        
        
        # input: [2, 2, 2, 6, 9, 9, 6, 6, 6]
        #                           l     e
        ans = []
        left = 0
         #[2, 2, 2, 6, 9, 9, 6]
         #             l 
        for end in range(1, len(nums)):
            if nums[end] != nums[left]:
                ans.append([nums[left], end - left])
                left = end
            
        # if left != len(nums) - 1:       # left = 6; len(nums) - 1 = 8           6 != 8
        #     ans.append([nums[-1], len(nums) - 1 - left])
        
        # if left == len(nums) - 1:
        #     ans.append([nums][-1], 1)
        ans.append([nums[left], len(nums) - left])

        return ans
        
        # # Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
        # prodNums = [2,2,2,6,9,9,6,6], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2],[6,2]].

# time => O(n + m + n + n) -> O(3n + m) -> O(n) where n and m are the length of the decoded inputs
# space => O(m + n) where n and m are the decoded respective inputs length


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        n1, n2 = len(encoded1), len(encoded2)
        p1 = p2 = 0
        remain1 = remain2 = 0
        while p1 < n1 and p2 < n2:
            freq1 = remain1 if remain1 > 0 else encoded1[p1][1]
            freq2 = remain2 if remain2 > 0 else encoded2[p2][1]
            min_freq = min(freq1, freq2)
            mul = encoded1[p1][0] * encoded2[p2][0]
            if res and res[-1][0] == mul:
                res[-1][1] += min_freq
            else:
                res.append([mul, min_freq])
            if freq1 > freq2:
                remain1 = freq1 - freq2
                remain2 = 0
                p2 += 1
            elif freq1 < freq2:
                remain1 = 0
                remain2 = freq2 - freq1
                p1 += 1
            else:
                remain1 = remain2 = 0
                p1 += 1
                p2 += 1
        return res
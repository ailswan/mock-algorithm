from typing import List

# 3095. Shortest Subarray With OR at Least K I
# You are given an array nums of non-negative integers and an integer k.

# An array is called special if the bitwise OR of all of its elements is at least k.

# Return the length of the shortest special non-empty 
# subarray
#  of nums, or return -1 if no special subarray exists.

# Example 1:

# Input: nums = [1,2,3], k = 2

# Output: 1

# Explanation:

# The subarray [3] has OR value of 3. Hence, we return 1.

# Example 2:

# Input: nums = [2,1,8], k = 10

# Output: 3

# Explanation:

# The subarray [2,1,8] has OR value of 11. Hence, we return 3.

# Example 3:

# Input: nums = [1,2], k = 0

# Output: 1

# Explanation:

# The subarray [1] has OR value of 1. Hence, we return 1.


# Constraints:

# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64


class Solution:
	def shortestSubArray(self, nums: List[int], k: int) -> int:
		# prefix accumulate of bitwise OR of vals
		# we compare the bitwise OR of pSum against the bitwise value of k to see if it's GTE to k
		# if greater or equal to k, use a start/end pointer to try and reduce the window size
		# once we realize our OR val is less than k, check against shortest window so far and update

		# {
		#	prefix_total: index
		# }
		# prefix_total - k


		# Input: nums = [1,2,3], k = 2
		#0 0 1   1   k
		#0 1 0   2   
		#0 1 1   3   i
		# 1    2     3   4   5 
		#            left    i
		# OR12: 0  OR2: 1  when i = 3    (OR12)OR3: 0  (OR2)OR3:1  OR3:2   i= 4
		# prefix_total  increasing  >= k    moving index(left)
		prefix_total = 0
		shortest_so_far = 0
		mapping = {}
		start = 0
		bin_k = bin(k)[3:] # 11
        #[1,12,2,5] k = 43
		for i, num in enumerate(nums):
			prefix_total |= num 				# 01 | 10 -> 11							
			mapping[prefix_total] = i
			temp = dict()
			for key, val in mapping.items():
				subTotal |= key
				temp[subTotal] = val
			mapping.update(temp)
			mapping[num] = i
			for key, val in mapping.items():
				if key >= k:
					shortest_so_far = min(shortest_so_far, i - val + 1)
		
		return shortest_so_far if shortest_so_far else -1
    
# time => (N^3) N is length of input, w is length of bitwise values (n * 2^w)
# space => (N^2)                      O(2^w)  w = 8  10

# w is the number of bits required to represent the maximum value of the integers in the list nums using binary representation.
# For example:

# If the integers in nums are between 0 and 255, w would be 8 (since 255 is 11111111 in binary, which is 8 bits).
# If the integers can be as large as 1023, w would be 10 (since 1023 is 1111111111 in binary, which is 10 bits).
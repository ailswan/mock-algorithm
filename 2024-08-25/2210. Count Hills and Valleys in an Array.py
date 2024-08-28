from typing import List

# 2210. Count Hills and Valleys in an Array
# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i].
# Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i].
#  Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

# Return the number of hills and valleys in nums.

 

# Example 1:

# Input: nums = [2,4,1,1,6,5]
# Output: 3
# Explanation:
# At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
# At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
# At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
# At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
# At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
# At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
# There are 3 hills and valleys so we return 3.
# Example 2:

# Input: nums = [6,6,5,5,4,1]
# Output: 0
# Explanation:
# At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
# At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
# At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
# At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
# At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
# At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
# There are 0 hills and valleys so we return 0.
 

# Constraints:

# 3 <= nums.length <= 100
# 1 <= nums[i] <= 100


class Solution:
	def countHillsValleys(self, nums: List[int]) -> int:
		# start and end indices are never hills or valleys
		# keep track of a running total of hills and valleys
		# iterate through the input, from index 1 to len(nums) - 1
			# at each element, check the left and right elements to see if there is a hill or valley, if so, add to answer
			# if not, move on

		
		# Input: nums = [6,  6,  5,  5,  4,  1]
		#				         ^
		#			                 ^
		#				      ^		
		# 1 3 3 1
		#     ^

		# 5 2 2 5
		ans = 0
		n = len(nums) # 4
		
 #[1, 3, 3, 2, 2 ,1 , 4, 5, 2]
 # 1  -1 
 
 #[21,21,21,2,2,2,2,21,21,45]
 

 #[2,4,1,1,6,5]
 #
 #[1,1,1,1,1,1,1,57,57,57,50,50,50,50,22,22,22,86]     
#       -----
#      /     |------        |
#     / 1      1    |-------|
#----/                      1


# / 1
#/
 
   #  ---
 #  j/    \ k      /\   j < i  < k
 #  /      \      /  \
 # /         \---/    \
 #  i-1   i i + 1

		left, right = 0, 0
		for i in range(1, n - 1):		# n = 5 i = 4 i = 1 ~ 4
			if nums[i] == nums[i + 1]:	# 6 == 5?
				continue
			for j in range(i - 1, -1, -1):
				if nums[i] > nums[j]:
					left = 1
					break
				elif nums[i] < nums[j]:
					left = -1
					break
			for k in range(i + 1):
				if nums[k] > nums[i]:
					right = -1
					break
				elif nums[k] < nums[i]:
					right = 1
					break
			if left == -1 and right == 1 or (left == 1 and right == -1):
				ans += 1
			
			left, right = 0, 0
			

		return ans

# time => (n ^ 2)
# space => (1)
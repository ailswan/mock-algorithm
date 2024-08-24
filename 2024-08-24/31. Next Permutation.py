from typing import List

# 31. Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    def findNext(self, nums: List[int]):
        #  1  3  1   2   3  1
        #  1  3  1   3   2  1

        #  1  3  1   4   3  1
        #  1  3  3   4   1  1
        #  1  3  3   1   1  4
        #        i       j
        #  end of last increasing : 3 swap  it with the first one close to it 3
        #  corner case all elements are decreasing
        #  5 3 2 1
        #  1 2 3 5
        #[1,2,3]   132
        #  1 2 3
        #  0 1 2
        #  1  3  1   4   3  1
        #  0  1  2   3   4  5
        #        i       j
        #  1  3  3   1   1  4
        # 1  2  3
        # 0  1  2
        #    i  j
        # 1  3  2
        # 2  3  1
        n = len(nums) # 3
        last_i = float('inf')
        for i in range(n - 2, - 1, - 1):     # i = 2
            if last_i != float('inf'):
                break
            if nums[i] < nums[i + 1]:# 2 < 3
                last_i = i
                for j in range(n - 1, i, -1): #j = 2  range(2, 1, - 1)
                    if nums[j] > nums[i]: # 3 >  2
                        nums[i], nums[j] = nums[j], nums[i] # swap 3  2
                        # reverse the list from nums[i + 1:]
                        l, r = i + 1, n - 1  # 2  2
                        while l < r:
                            nums[l], nums[r] = nums[r], nums[l]
                            l += 1
                            r -= 1
                        break
                      
        if last_i != float('inf'):
            nums[::-1]
        
        n = len(nums) # 3
        last_i = n - 1
        for i in range(n - 2, - 1, - 1):
            if nums[i] < nums[i + 1]:# 2 < 3
                last_i = i
                break
        for j in range(n - 1, last_i, -1):
            if nums[j] > nums[last_i]: # 3 >  2
                nums[last_i], nums[j] = nums[j], nums[last_i]
                break
        
        # [3, 2, 1]
        l = last_i + 1 if last_i != n - 1 else 0  # 0
        r = n - 1 # 2  
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # time complexity O(n)   
        # space complexity O(1)
            


 




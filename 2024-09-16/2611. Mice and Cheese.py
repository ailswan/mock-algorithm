from typing import List

# 2611. Mice and Cheese

# There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

# A point of the cheese with index i (0-indexed) is:

# reward1[i] if the first mouse eats it.
# reward2[i] if the second mouse eats it.
# You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

# Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.


 
# Example 1:

# Input: reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
# Output: 15
# Explanation: In this example, the first mouse eats the 2nd (0-indexed) and the 3rd types of cheese, and the second mouse eats the 0th and the 1st types of cheese.
# The total points are 4 + 4 + 3 + 4 = 15.
# It can be proven that 15 is the maximum total points that the mice can achieve.
# Example 2:

# Input: reward1 = [1,1], reward2 = [1,1], k = 2
# Output: 2
# Explanation: In this example, the first mouse eats the 0th (0-indexed) and 1st types of cheese, and the second mouse does not eat any cheese.
# The total points are 1 + 1 = 2.
# It can be proven that 2 is the maximum total points that the mice can achieve.


# Constraints:

# 1 <= n == reward1.length == reward2.length <= 10^5
# 1 <= reward1[i], reward2[i] <= 1000
# 0 <= k <= n

class Solution:
    def maxReward(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Input: reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
        # Output: 15
        # m1 k         m2   2k >= n:  pick the max point for each type
        #reward1 = [1,1,3,4,1], reward2 = [4,4,1,1,0], k = 2
        # if 2k < n: give up min points , return sum of 2k largest
        # merg two rewards   max  [4,4,3,4,1]
        n = len(reward1)
        merge = [0] * n
        res = 0
        for i in range(n):
            merge[i] = max(reward1[i], reward2[i])
        if 2 * k >= n:
            res = sum(merge)
        else:
            merge.sort(reverse= True)
            for i in range(2 * k):
                res += merge[i]
        return res
    #time complexity O(n)
    #space complexity O(n)








 

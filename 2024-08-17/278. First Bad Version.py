from typing import List

# 278. First Bad Version

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 

# Constraints:
# 1 <= bad <= n <= 2^31 - 1



# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #1 2 3 4 5     4
        #0 1 2 3 4
        #      ^
        # bianry search
        # l r  isBadVersion(mid) is bad : move r = mid else: l = mid
        l, r = 1, n
        while l < r: # 4  5
            mid = l + (r - l) // 2
            if self.isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
    #time complexity O(log*(n))
    #space complexity O(1)

        
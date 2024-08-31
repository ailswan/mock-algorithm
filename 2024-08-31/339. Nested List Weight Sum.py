from typing import List
# 339. Nested List Weight Sum

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

 

# Example 1:
# https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex1.png


# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
# Example 2:
# https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex2.png


# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
# Example 3:

# Input: nestedList = [0]
# Output: 0
 

# Constraints:

# 1 <= nestedList.length <= 50
# The values of the integers in the nested list is in the range [-100, 100].
# The maximum depth of any integer is less than or equal to 50.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # iterate through the input
        # check if the element is an integer or a nestedList
        # if integer, multiply by the depth and add to the total
        # if it's a nestedList, dfs through it
        # return total at the end

        # input: [1,[4,[6]]]
        # output: 27

        total = 0

        def dfs(nList, depth):          # [4, ...], 2               #[6], 3
            nonlocal total
            for ele in nList:               # [6]
                if ele.isInteger():                     # 6.isInteger? T
                    total += ele.getInteger() * depth   # total = 9 + 6 * 3 -> 27
                else:
                    nList = ele.getList()               # nList = [6]
                    dfs(nList, depth + 1)               # dfs([6], 3)
        
        for element in nestedList:          # nestedList [1, ...]
            if element.isInteger():         # nestedList.isInteger? F
                total += element.getInteger()   # total = 1
            else:
                nList = element.getList()   # nList = [4, ....]
                dfs(nList, 2)               # dfs([4, ...], 2)
        
        return total

# [[[[1]]], [6], ...., ...., ....] 4 + 2 + 
# n = 6
# time => O(n) where n is the number of NestedLists
# space => O(n)
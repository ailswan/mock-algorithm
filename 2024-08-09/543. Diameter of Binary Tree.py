from typing import List

# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:

#          1
#        /   \
#       2     3
#      /  \
#     4    5


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def getDiameter(self, root: TreeNode) -> int:
        # caculate each node's longest path , track the max one to update res
        #          1
        #        /   \
        #       2     3
        #      /  \
        #     4    5
        def getDepth(node):# node2 - 2
            if not node:
                return 0
            l = getDepth(root.left)# node2  2

            r = getDepth(root.right)# node3  1
            self.res = max(self.res, l + r)  #path 4 - 2 - 1 -3  length of path = 3
            return max(l ,r) + 1 
        
        return self.res

        # space complexity - O(h)
        # time complexity - O(n)
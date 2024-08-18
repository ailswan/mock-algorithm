from typing import List

# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

# Example 1:

#           3
#         /   \
#        9    20
#            /  \
#           15   7
        

# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftLeavesSum(self, root: Node) -> int:
    #           3
    #         /   \
    #        9    20
    #            /  \
    #           15   7
        #self.res track the sum
        # leftLeavesSum(root.left) + leftLeavesSum(root.right)
        def getLeftLeavesSum(node, isLeft): #9 1   20 0 
            if not node:
                return 0
            if isLeft and not node.left and not node.right:
                return node.val
            return getLeftLeavesSum(node.left, 1) + getLeftLeavesSum(node.right, 0) # 15 + 0
        
        #node3
        return getLeftLeavesSum(root,0) #node 9(9)  node20(15) 
    
    #time complexity O(n)
    #space complexity O(h)



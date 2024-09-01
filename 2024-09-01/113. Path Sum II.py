from typing import List

# 113. Path Sum II

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:

#                       5
#                     /   \
#                    4     8
#                   /     /  \
#                  11    13   4
#                /   \       /  \
#               7     2     5    1


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22


# Example 2:

#                       1
#                     /   \
#                    2     3


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sumPaths(self, root: Node, targetSum: int) -> List[List[int]]:
        #                       5
        #                     /   \
        #                    4     8
        #                   /     /  \
        #                  11    13   4
        #                /   \       /  \
        #               7     2     5    1


        # Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
        # path = [5, 4...] passed down 
        # is Leaf node: check the sum : append to the res
        self.res = []
        def dfs(node, path): # node1 [5, 8, 4, 1]  
            if not node.left and not node.right: #node 1
                if sum(path) == targetSum: #[5, 8, 4, 1]   18
                    self.res.append(path)#[[5, 4, 11,2], [5, 8, 4, 5] ]
                    return
            if node.left:
                dfs(node.left, path + [node.val])  # node4 [5, 8, 4] node5 [5, 8, 4, 5] 
            if node.right:
                dfs(node.right, path + [node.val]) #  node1 [5, 8, 4, 1]   
        
        if not root:
            return 0 == targetSum
        
        dfs(root, [root.val]) # node5 [5]
        return self.res #[[5, 4, 11,2], [5, 8, 4, 5] ]
    # time complexity O(n) n is the number of nodes
    # space complexity O(h)  h can be log n for average cases, worst case would be n

# Time Complexity: O(n)
# Space Complexity:
# Worst case: O(n)
# Average case: O(log n)


        
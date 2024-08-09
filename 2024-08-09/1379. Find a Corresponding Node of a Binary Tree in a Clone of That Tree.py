from typing import List

# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
# Input: tree = [7,4,3,null,null,6,19], cloned = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
#      7                        7
#     / \                      / \
#    4   3 <- target          4   3<-  
#       / \                      / \
#      6   19                   6   19
# Input: tree = [7],cloned =[7], target =  7
# Output: 7

#  7 <- target      7<- 

# Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1],cloned =[8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# Output: 4
#      8                                   8
#       \                                    \
    #     6                                   6
    #       \                                  \
        #      5                                 5
        #       \                                 \
            #      4  <- target                    4 <-
            #       \                               \
                #     3                              3
                #       \                              \
                    #     2                             2
                    #       \                            \
                       #     1                            1
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# The values of the nodes of the tree are unique.
# target node is a node from the original tree and is not null.
 

# Follow up: Could you solve the problem if repeated values on the tree are allowed?

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClonedNode(self, original_root: TreeNode, clone_root: TreeNode, target: int) -> TreeNode:
        
        
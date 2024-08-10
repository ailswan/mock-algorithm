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
#    4   3 <- target          4   3<-  return
#       / \                      / \
#      6   19                   6   19
# Input: tree = [7],cloned =[7], target =  7
# Output: 7

#  7 <- target      7<- return

# Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1],cloned =[8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# Output: 4
#      8                                   8
#       \                                    \
    #     6                                   6
    #       \                                  \
        #     4                                 4
        #       \                                 \
   #  cur  ->      4  <- target                    4 <-return  
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
    def findClonedNode(self, original_root: TreeNode, clone_root: TreeNode, target: TreeNode) -> TreeNode:
        # traverse through the original_root and clone_root using p1 and p2 ptrs
        # compare p1 with target, if a match, return p2
        q1 = deque([original_root])
        q2 = deque([clone_root])
        # p1 = original_root
        # p2 = clone_root

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1 is None or node2 is None:
                return
            else:
                if node1 == target:   
                    return node2
                else:
                    q1.append(original_root.left)
                    q1.append(original_root.right)
                    q2.append(clone_root.left)
                    q2.append(clone_root.right)

        return None
from typing import List

# 111. Minimum Depth of Binary Tree


# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:
#                 3
#               /   \
#              9     20
#                  /    \
#                 15     7

# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:
#    2
    #  \
    #   3
    #     4
    #      5
    #       6
    
     
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000
from collections import deque 
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def miniDepth(self, root: Node) -> int:
        # bfs go through the node
        # check if the node is leave node return the node
        #                 3
        #               /   \
        #              9     20
        #                  /    \
        #                 15     7
        #    2      1
            #  \ 
            #   3     2
            #     4      2^2
            #      5     2^2^2
            #       6

        if not root:
            return 0
        q = deque([(root, 1)]) #q =  [ (node6, 5)]
        while q:
            node, depth = q.popleft()  #  node6  5
            if not node.left and not node.right:
                return depth # 5
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))


    #time complexity O(n) n is the numbers of the nodes
    #space complexity O(2^h) == O(n)

            

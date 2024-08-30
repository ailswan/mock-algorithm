from typing import List

# 270. Closest Binary Search Tree Value

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 
# Example 1:

#               4
#             /   \
#            2      5
#          /   \
#         1     3
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4


# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Node, target: int) -> int: #(3, 3.7)
        #               4
        #             /   \
        #            2      5
        #          /   \
        #         1     3
        # target = 3.714286 t
        # 4
        # t > root.val on the right side or root
        # else left or root
        # r = closestValue(root.right, t)
        # r - t  >  root - t : return root else r
        # if leaf : return leaft node

        # handle the none and leaves
        if not root:
            return None
        if not root.left and not root.right:
            return root.val # 3
        if target > root.val:#  3.7  >   2
            r = self.closestValue(root.right, target)# 3
            if abs(r - target) > abs(root.val - target):# 3 - 3.7 0.7  > 2 - 3.7  
                return root.val
            else:
                return r # 3
        elif target < root.val:# 3.7  <  4
            l = self.closestValue(root.left, target) # l (2, 3.7)   3
            if abs(l - target) > abs(root.val - target):# 3 - 3.7  0.7 > 4 - 3.7 0.3
                return root.val # 4
            else:
                return l 
        else:
            return root.val
    # time complexity O(logn) n is the total number of nodes
    # space complexity O(h) h is the height of the tree






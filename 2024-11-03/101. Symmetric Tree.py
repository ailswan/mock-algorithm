from typing import List

# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:

#           1
#        /  |  \
#       2   |   2
#     /  \  |  /  \
#    3    4 |  4    3
#           |

# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 

# Follow up: Could you solve it both recursively and iteratively?

class Node:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def SymmetricTree(self, root) -> bool:
        #root.left root.right isSymmetric  root.left.left root.right.right
        def isSymmetrics(left, right):
            if not left and not right:
                return True
            if not right or not left:
                return False
            if left.val != right.val:
                return False
            l_is = isSymmetrics(left.left, right.right)
            r_is = isSymmetrics(left.right, right.left)
            return l_is and r_is
        return isSymmetrics(root.left, root.right)
    
    # time complexity O(n) n is the node of tree  
    # space complexity O(h)h of the tree


class Solution:
    def SymmetricTree(self, root) -> bool:
        #[left, right]
        #[left.left, right.right left.right, right.left]


class Solution:
    def isSymmetric(self, root):
        q = [root, root]
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
    
# while q:
#     lvl_length = len(q)
#     for i in range(lvl_length):
#         .....
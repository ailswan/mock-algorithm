from typing import List

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

#        1  <-
#      /   \
#     2     3  <-
#      \     \
#       5     4  <-


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
import collections
class Treenode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right 

class Solution :
    def rightView(self, root: Treenode) -> List[int]:
            #        1  <-
            #      /   \
            #     2     3  <-
            #      \     \
            #       5     4  <-
            # bfs track each level 
            # find the last val in each level 
            # append val in the res 
            res = []
            q = collections.deque([root])
            while q:# [ node5, node4]
                res.append(q[-1].val)#res =[1, 3, 4]
                l = len(q) #2
                for i in range(l): # 2   range(2)
                    cur = q.popleft() # node3
                    if cur.left:# [node3]
                         q.append(cur.left) 
                    if cur.right:
                         q.append(cur.right) #[ node5, node4]
            return res#[1, 3, 4]
        #time complexity O(n)
        #space complexity O(n)
                
                     
 
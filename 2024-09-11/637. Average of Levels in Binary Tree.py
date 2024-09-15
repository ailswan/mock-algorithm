from typing import List

# 637. Average of Levels in Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10^-5 of the actual answer will be accepted.


# Example 1:

#               3
#             /   \
#            9     20
#                /   \
#               15    7

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:

#               3
#             /   \
#            9    20
#          /   \
#         15    7

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
from collections import deque
class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageLevel(self, root: Node) -> List[float]:
#               3
#             /   \
#            9     20
#                /   \
#               15    7
        #bfs 
        #q track the each level values
        # calculate the average in each level
        q = deque([root])
        res = []
        while q:#[node15, node7]
            l = len(q)#2
            level_sum = 0
            for i in range(l): #i = 1 
                cur = q.popleft()# node7
                level_sum += cur.val # 15 + 7 22
                if cur.left:
                    q.append(cur.left)#[]
                if cur.right:
                    q.append(cur.right)#[]
            average = level_sum / l # 22 / 2
            res.append(average) #[3.000, 14.500, 11.000]
        return res#[3.000, 14.500, 11.000]
    # time complexity O(n) n is the total number of node
    # space complexity O(2^h) store node in one level in q. worst case is 2^h. h is the height of tree





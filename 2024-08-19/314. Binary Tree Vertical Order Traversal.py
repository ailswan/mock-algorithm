from typing import List

# 314. Binary Tree Vertical Order Traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:

#         3
#       /   \
#      9     20
#           /   \
#         15     7


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example 2:

#         3
#      /    \
#     9      8
#    /  \   /  \
#   4    0 1    7


# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example 3:

#         3
#      /    \
#     9       8
#   /   \   /   \
#  4     0 1     7
#      /     \
#     5       2
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
import collections
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #         3(0)
        #       /   \
        #     9(-1)  20(1)
        #          /   \
        #        15(0)  7(2)
        # Output: [[9],[3,15],[20],[7]]
        # positon(p) start from 0 . left node  p -= 1  right node p += 1
        # res = {-1:[9], 0:[3, 15],1:[20], 2[7]}
        res = collections.defaultdict(list)
        def dfs(node, p, r):#node7 p = 2
            if node:
                res[p].append((node.val, r)) #res[1].append(20) {0:[3, 15], -1:[9],1:[20], 2:[7]}
                dfs(node.left, p - 1) # 15 0
                dfs(node.right, p + 1)#7  2

        if not root:
            return []

        dfs(root, 0, 0)
        #{0:[3, 15], -1:[9],1:[20], 2:[7]}
        # k in [-1, 0, 1, 2]
        #[[(9,1)],[(3, 0),(15, 2)],[(20, 1)],[(7, 2)]]
        lst = []
        for k in sorted(res.keys()):
            group = res[k]
            group.sort(key = lambda x: x[1])#[(3, 0),(15, 2)]
            lst.append([v for v, k in group]) #3 15
        return lst

        # return [res[k].sort(lambda x: x[1]) for k in sorted(res.keys())]
    
	# hint: use minimum_column, max_column to decrease time complexity
    #time complexity O(nlogn)
    #space complexity O(n)
        

#         3
#      /    \
#     9       8
#   /   \   /   \
#  4     0 1     7
#      /     \
#     5       2
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]     
# [3, 0 1] [3, 1, 0]       

        
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret
 
from typing import List

# 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Example 1:

#             1
#           /   \
#          2     3
#           \
#            5

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]


# Example 2:

# Input: root = [1]
# Output: ["1"]


# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def getAllPaths(self, root: Node) -> List[str]:
        # res
        # 1->  1->2  1->3
        # node.val + '->' + getAllPaths(node.left)         getAllPaths(node.right)
        #             1
        #           /   \
        #          2     3
        #           \
        #            5
        def dfs(node, path):# node2 "1"  #node3, "1" # node5 "1 -> 2"
            if len(path) == 0:
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)# node2 "1 -> 2"  #node3, "1 -> 3" # node5 "1 -> 2 -> 5"
            if not node.left and not node.right:# node5 "1 -> 2 -> 5"
                self.res.append(path) #["1 -> 3", "1 -> 2 -> 5"]
            if node.left:
                dfs(node.left, path)# dfs(node2, "1")
            if node.right:# dfs(node3, "1") # node2 "1 -> 2"
                dfs(node.right, path)
        dfs(root, "")
        return self.res
# time complexity o(n)
# space complexity o(n)


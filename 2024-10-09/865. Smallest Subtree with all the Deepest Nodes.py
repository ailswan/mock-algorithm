from typing import List 

# #865. Smallest Subtree with all the Deepest Nodes
# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

#  Example 1:
#           3
#         /   \
#         5   1
#      /   |  |  \
#     6   2   0    8
#        / \       / \
#       7   4     9   10

# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
# Example 2:

# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
# Example 3:

# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

# Constraints:

# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
 
class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestSubTree(self, root: Node) -> Node:
        # DFS recursive to find the deepest leaves
        # keep track of the level, looking for the deepest
        # once we find the leaves, mark the parent node as the potential smallest
        ans = None
        deepest = (None, 0) # (node, lvl)

        if root is None:
            return None

        def dfs(node, level):
            nonlocal deepest
            if node is None:
                return level + 1
            
            left = dfs(node.left, level)
            right = dfs(node.right, level)

            if level > deepest[1]:
                deepest = (node, level)
            
            return left or right

        dfs(root, 0)
        return ans
    


#           3
#         /   \
#         5   1
#      /   |  |  \
#     6   2   0    8
#        / \       / \
#       7   4     9   10

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return (None, 0)
            l = dfs(root.left)
            r = dfs(root.right)
            depth = max(l[1], r[1]) + 1
            if l[1]  < r[1]:
                return (r[0], depth)
            elif l[1] > r[1]:
                return (l[0], depth)
            return (root, depth)
        return dfs(root)[0]
            
        
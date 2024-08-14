from typing import List

# 1123. Lowest Common Ancestor of Deepest Leaves

# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
 

# Example 1:

#                 3
#               /   \
#              5     1
#            /  \    | \
#           6   2    0  8
#              / \
#             7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

# Example 2:

# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree, and it's the lca of itself.

# Example 3:

# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
 

# Constraints:
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 1000
# The values of the nodes in the tree are unique.

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAncestor(self, root: TreeNode) -> TreeNode:
        #                 3           0     (node2, 3)
        #               /   \
        #              5     1        1    dfs node5,1->return# (node2, 3)            node1  #(node1, 2)
        #            /  \    | \
        #           6   2    0  8     2    node6 return#(node9,3)   dfs(node2,2) = (node2, 3) 
        #          /    / \
        #         9    7   4           3                          node7,3       node4,3
        # res track parent whose children have deepest 
        # dfs(node, depth)     return (lowest ancestor, largest depth)
        def dfs(node, parent, depth):# node9 node6 depth= 3 (node9,3)            none node6 depth3(node6,2)
            if not node: 
                return (parent, depth - 1)
            if not node.left and not node.right:
                return (node, depth)
            left_parent , left_depth= dfs(node.left, node, depth + 1)#(node9,3)   
            right_parent , right_depth= dfs(node.left, node, depth + 1)#(node2, 3) 
            if left_depth < right_depth:#   3  2?
                return (right_parent, right_depth)    # (node5, 3)
            elif left_depth > right_depth:
                return (left_parent, left_depth)#(node9,3)
            else:
                return (parent, right_depth) # (node5, 3)
        
        parent, depth = dfs(root, None, 0) # (node5, 3)
        return parent
    #time complexity o(n)
    #space complexity o(h)


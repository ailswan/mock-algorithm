from typing import List

# 1650 Lowest Common Ancestor of a Binary Tree III

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

# Example 1:

#         3
#       /  \
#      5    1
#     / \   / \
#    6  2  0   8
#      / \
#     7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q exist in the tree.
class Node:
    def __init__(self, val = 0, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestAncestor(self, p: Node, q: Node)-> Node:
        #         3
        #       /  \
        #      5    1
        #     / \   / \
        #    6  2  0   8
        #      / \
        #     7   4
        # p = 5, q = 1   p =6, q = 8
        
        # input: [8], p = 8, q = 8
        def helper(root, node):#        node = 4
            if not root:
                return False
            if root == node:
                return True
            return helper(root.left, node) or helper(root.right, node)# 0   8 
        if p == q:
            return p
        if p.parent == q.parent:# 5 1
            return p.parent# 3
        # if p and q on the left and right side of one roote seperately just return the root
        # p or q is their lowest ancestor 
        if helper(p, q):#6 8  
            return p
        if helper(q, p):#6 8  
            return q
        return self.lowestAncestor(p.parent, q.parent) # 5   1
    # time complexity O(H)  H is the hight of lowest ancestor subtree
    # space complexity O(H)

    





        # dfs find the lower ancestor for p q if it can be find return the lowset ancestor else return root
        # search the left side to find the p or q
        # if find p return True else return False
        # if findp and findq : return root 
        # else continue search the False one(p/q) in the True path

        def helper(root, node):# 8 4
            if not root:
                return False
            if root == node:
                return True
            return helper(root.left) or helper(root.right)# 0   8 

        if not root:  
            return None  
        l = helper(root.left, p) # 6  5  True
        r = helper(root.right, q)# 2  4 False
        if not l and not r:
            return None
        if l and r:
            return root# 3
        if l and not r:
            return self.lowestAncestor(self.left, p, q) # 5    5 4 
        else:
            return self.lowestAncestor(self.right, p, q)

 
        

            

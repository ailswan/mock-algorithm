from typing import List

# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:
#     3
#    / \
#    9  20
#       / \
#       15 7

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def constructTree(self, inorder: List[int], postorder: List[int]) -> Node:
        # traverse through the inputs
        # inorder => left child -> root -> right child
        # postorder => left child -> right child -> root
        # *** for postorder lists and sublists, the last element is ALWAYS the root ***
        # inorder    9,3,15,20,7  l - n - r
        #             split      len(inorder) - 1- split
        # postorder  9,15,7,20,3  l - r - n
        #               |      n   
        #               1   3   [1:4] 4  
        # the very first element in both inputs is the left child
        # when adding a node, make sure the element in both inputs are the same value
        # from the inorder list, node3 is a parent of node9
        # from postorder list, node 15 is in the opposite subtree of node9
        
        def dfs(inorder, postOrder):
            root = Node(postorder[-1])
            
            split = inorder.index(root.val) # split = 1
            
            left_subtree = dfs(inorder[: split], postorder[:split])
            right_subtree = dfs(inorder[split + 1:], postorder[split : len(postorder) - 1])
            #postorder input => 15,7,20

            root.left = left_subtree
            root.right = right_subtree
            return root
        
        return dfs(inorder, postorder)
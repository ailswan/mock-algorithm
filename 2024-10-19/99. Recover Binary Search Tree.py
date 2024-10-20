from typing import List
# 99. Recover Binary Search Tree

# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:
#    1      3
#   /      /
#  3   =>  1
#   \       \
#    2       2

# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:
    #     3         2
    #   /  \       /  \
    #   1   4  => 1    4
    #       /          /
    #      2          3
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

# Constraints:

# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1
 

# Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverBST(self, root: Node) -> Node:
        # left tree has value larger than its parents' values
        # right tree has value smalelr than its parents' values
        # step 1 => DFS through the tree, looking for the mismatched value
        # step 2 => find the node to switch with the invalid node
        

            #     3                                 2
            #   /  \                              /  \
            #   1   4                         => 1    4
            #       /                                /
            #      2                                3
        self.firstNode = None                   # n3
        self.secondNode = None                  # n2
        self.preNode = Node(float("-inf"))      # n1        n3      n2
        
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode #n3
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

 
        # ptr = root
        # swap_ptr = root
        # ptr3 = 

        def dfs(node):
            if node is None:
                return None

            if node.left and node.left.val > node.val:
                firstNode = node.left
            elif node.right and node.right.val < node.val:
                firstNode = node.right
            
            return dfs(node.left) or dfs(node.right)
        dfs(root)

class Solution:
        def recoverTree(self, root: Node) -> None:
            firstNode = None
            secondNode = None
            pre = Node(float("-inf"))

            stack = []
            p = root
            while p or stack:
                while p:
                    stack.append(p)
                    p = p.left
                p = stack.pop()
                
                if not firstNode and pre.val > p.val:
                        firstNode = pre
                if firstNode and pre.val > p.val:
                    #print(firstNode.val,pre.val, p.val)
                    secondNode = p
                pre = p
                p = p.right
            firstNode.val, secondNode.val = secondNode.val, firstNode.val
    
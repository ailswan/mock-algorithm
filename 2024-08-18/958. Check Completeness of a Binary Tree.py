from typing import List

#  Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
    #         1
    #       /    \
    #     2       3
    #   /  \     /
    #  4    5    6

 
# Example 2:


# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#       1
#     /  \
#    2    3
#   / \    \
#  4   5    7
# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000

class Node:
	def __init__(self, val = 0, left = None, right = None) -> None:
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isCompleteBinaryTree(self, root: Node) -> bool:
		# dfs, recursive
		# make sure at each recursive call, if there is a left child, there MUST be a right child; unless it's a leaf, can have left child
		# if a child is a leaf (no left AND no right children), make sure the parent node has both left AND right children; otherwise, parent node MUST have left child (no right child)
	#         1
    #       /    \
    #     2       3
    #   /  \     /
    #  4    5    6

		if root is None:
			return True


		def dfs(node, parent_ptr = None):	#n2 								dfs(n3) -> True
			if node is None:
				return True
			
			if node.left is None and node.right is None:	# n3
				if not parent_ptr.left:
					return False
			
			if node.left and node.right:	#n4.left? n4.right?
				parent_ptr = node	# parent = n2
				return dfs(node.left. parent_ptr) and dfs(node.right, parent_ptr)		#dfs(n4) -> True and dfs(n5)? -> True
			
			if not node.left or not node.right:
				return False
			return True
		
		return dfs(root) # [n1]

# time complexity => (N)
# space => O(height) if balanced or O(N) for unbalanced tree
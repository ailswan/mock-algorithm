from typing import List

# 250. Count Univalue Subtrees
# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

# Example 1:
#         5
#       /  \
#     1      (5)
#    /  \      \
#   (5)  (5)   (5)

# Input: root = [5,1,5,5,5,null,5]
# Output: 4
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [5,5,5,5,5,null,5]
# Output: 6
 

# Constraints:

# The number of the node in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000

class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def univalueSubtrees(self, root: Node) -> int:
        # check the leaves... all leaves are univalue subtrees
        # DFS, recursively check each subtree to see if they contain the same value
        # at each recursive call, there begins a potential new univalue subtree... or it's not a univalue subtree anymore
        # increment ans by 1 when we return with univalue tree

        #         5
        #       /  \
        #     1      (5)
        #    /  \      \
        #   (5)  (5)   (5)

        # ans = 0

        def dfs(node, unival):
            if node is None:
                return 1, unival
            
            count = 0
            count_l, left = dfs(node.left, node.val)
            count_r, right = dfs(node.right, node.val)

            if node.val == unival:
                count = 1 + count_l + count_r
            else:
                count = count_l + count_r
 
            return count, left or right
        
        return dfs(root, root.val)
    

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return True, 0
            if not node.left and not node.right:
                return True, 1
            left_is_unival, left_count = dfs(node.left)
            right_is_unival, right_count = dfs(node.right)
            current_count = left_count + right_count
            if (left_is_unival and right_is_unival and
                (node.left is None or node.left.val == node.val) and
                (node.right is None or node.right.val == node.val)):
                return True, current_count + 1
            return False, current_count

        _, total_count = dfs(root)
        return total_count
    
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                self.ans += 1
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left == right == node.val or (left is None and right == node.val) or (right is None and left == node.val):
                self.ans += 1
                return node.val
            return float('inf')

        dfs(root)
        return self.ans


# time => O(N) where N is the number of nodes
# space => O(h) where h is height of the tree for the recursion stack (for a balanced tree)


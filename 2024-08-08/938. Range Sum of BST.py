# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1
            #         10
            #       /    \
            #     5       15
            #   /   \       \
            #  3     7        18

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32    # 7 + 10 + 15 = 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.



# Example 2
#                     10
#                   /    \
#                 5       15
#               /   \    /  \
#              3     7  13   18
#             /     /
#            1     6

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

class TreeNode:
    def __init__(self, val = 0, left = None, right= None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getRangeSum(self,root: TreeNode, low: int, high: int) -> int:
        # Example 1
            #         10
            #       /    \
            #     5       15
            #   /   \       \
            #  3     7        18

        # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15   
        # Output: 32    # 7 + 10 + 15 = 32
        # res 
        # node.val in the range  10   res += 10
        # if node.val <   just continue check the right
        # if node.val >    just continue check the left 
        # leftRangeSum + rightRangeSum + check root.val?
        res = 0 # global var
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            # if low <= node.val <= high:
            #     res += node.val # res = 10 + 7 + 15  node 10 
            #     dfs(node.right)
            #     dfs(node.left)
            # if node.val < low: # node5
            #     dfs(node.right) # node7
            # if node.val > high: # node15 # None
            #     dfs(node.left) # res += 0
            
            if low <= node.val <= high:
                res += node.val # res += 15
            if node.val <= high: # 15 <= input [7, 15]
                dfs(root.right) # root.right -> 18 (not included in res)
            if node.val >= low:
                dfs(root.left)

        dfs(root)
        return res 
        
 
        

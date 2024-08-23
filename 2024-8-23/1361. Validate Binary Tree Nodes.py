from typing import List
# 1361. Validate Binary Tree Nodes
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

 
# Example 1:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
    #      0       
    #     / \
    #    1   2
    #       /
    #      3
    # Input: n = 4, leftChild = [3,-1,1,-1], rightChild = [-1,-1,0,-1]
     #     2
    #     / \
    #    1   0
    #       /
    #      3

# Example 2:


# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
    #      0
    #     / \
    #    1   2
    #    \  /
    #      3


# Example 3:


# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
    #      0
    #     /
    #    1
    
# Constraints:

# n == leftChild.length == rightChild.length
# 1 <= n <= 104
# -1 <= leftChild[i], rightChild[i] <= n - 1

class Solution:
	def isValid(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		# tree characteristics: can have at most 2 edges, each node cannot be connected to multiple other nodes
		# hashmap to track the position of each node we encounter <node, 2-children[i, j]>
		# cannot be cyclic

		# iterate through the left and right together
		# keep a visited set
		# if cyclic, return False
		# if we visit the entire tree and no cycles, return True
		# visited = set(0)
		    #      0
            #     / \
            #    1   2
            #    \  /
            #      3

		visited = defaultdict(list)

		# visited set => {0, 1, 2, 3}
		#leftChild = [1, -1, 3, -1] rightChild=[-1,-1, -1,-1]
		    #      0      
			#     / 
			#    1    4    2
			#          \  /
			#           3
			#step1  more than 1 root
			#step2  has cycle?
		hasRoot = False
		indegree = [] # how many parents
		for ptr in range(n):
			if leftChild[ptr] != -1:
				indegree[leftChild[ptr]] += 1
			if rightChild[ptr] != -1:
				indegree[rightChild[ptr]] += 1
		#[0, 1, 0, 2, 1]
		root = -1 #0 root == -1
		for i in range(n):			# greedy method to update the root and return False IF a root ALREADY exists
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
		
		def dfs(index):
			if index == -1:
				return True
			if index in visited:
				return False
			visited.add(index)
	
			return dfs(leftChild[index]) and dfs(rightChild[index]) 
		
		return dfs(root) and len(visited) == n
		#root
		#      0
        #     / \
        #    1   2
        #    \  /
        #      3
		
		
					
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
    #      0       
    #     / \
    #    1   2
    #      
    #      3


# visited = {1, 2, 3}

# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
    #      0
    #     / \
    #    1   2
    #    \  /
    #      3

	# visited ={ 1, 2, 3 }

# Input: n = 4, leftChild = [-1,-1,3,-1], rightChild = [-1,3,-1,-1]
# output: False
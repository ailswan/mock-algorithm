from typing import List

# 785. Is Graph Bipartite?
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
# You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. 
# More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.


# Example 1:
    # 0 - 1
    # | \ |
    # 3 - 2

# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:
        # 0 - 1
        # |   |
        # 3 - 2


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

# Constraints:

# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.

class Solution:
	def isGraphBipartite(self, edges: List[List[int]]) -> bool:
		# build adjacency list out of the edges
		# adj = {
		# 	0: [1, 3],
		# 	1: [0, 2],
		#   2: [1, 3]
		# }

		# bfs through the adj list
		# look at the neighbors, see if neighbor belongs in set A or set B
			# put the current node in set A... put all neighbors in set B
		# at a node, if it doesn't belong to set A or set B, check if its neighbors belong to set A or set B.... add node to the other set
			# if neighbors are in both set A and set B, return False
		# add neighbors to the queue
		# keep a visited list of nodes
		# return True at the end
		adj = defaultdict(list)
		n = len(edges)
		setA = set({0})
		setB = set()

		for a, b in edges:
			adj[a].append(b)
			adj[b].append(a)
		
		# bfs traversal through graph
		q = deque([0])
		visited = []
		m = sum([len(v) for v in adj.values()])
		# adj = {
		# 	0: [1, 3],
		# 	1: [0, 2],
		#   2: [1, 3]
		# }
		#visited = [1, 1, 1 ,2 ,0 ]
		# for i in range(n):
		# 0 
		
		while q:
			node = q.popleft()			# 1
			for neighbor in adj[node]:		# [0]
				q.append(neighbor)			# q = [1, 3]		node = 1 neighbor = 2
				if (node in setA and neighbor in setA) or (node in setB and neighbor in setB):		# (False and False) or (True and False)? -> False
					return False
				if n == len(setA) + len(setB):		# 4 == 2 + 2? True -> return True
					return True
				if node in setA:					
					if neighbor not in setB:		 
						setB.add(neighbor)			# setB = {1, 3}
				elif node in setB:					
					if neighbor not in setA:		
						setA.add(neighbor)			# setA = {0, 2}

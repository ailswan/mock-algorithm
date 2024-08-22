from typing import List

# 1443. Minimum Time to Collect All Apples in a Tree

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

 

# Example 1:

#               0
#            /    \
#          1      (2)
#         /  \    /   \
#      (4)   (5)  3     6

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Example 2:

#               0
#            /    \
#          1      (2)
#         /  \    /   \
#        4   (5)  3    6

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
# Example 3:

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0
 

# Constraints:

# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# hasApple.length == n
import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple; List[bool]) -> int:
    #              0
    #            / 2  \ 2
    #          1      (2)
    #       2 /  \2   / 0  \ 0 
    #      (4)   (5)  3     6
    #  start from end  node :  4   5  3  6   hasApple : time += 2  
    #     loop the node above them : has apple  time += 2
    #[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    #               0
    #            /    \
    #          1      (2)
    #         /  \    /   \
    #        4   (5)  3    6
        inbounds = [0] * n #[4 5 3 6 ] [1, 2]
        aboves = collections.defaultdict(list)  # adjacency list => { 0: [1, 2], 1: [4, 5], 2: [3, 6], 3: [2], 4: [2], 5: [1], 6: [2] }
        #         0
        #       /   \
        #      2     3
        #     /
        #   (1)
        #[[0,2],        [0,3],          [1,2]]
        #         0
        #       /   \
        #      3     4
        #           /
        #          2  
        #        /
        #       (1)
        #[0,3],[0,4],[1,2], [2, 4]] 
        for a, b in edges:
            inbounds[a] += 1  
            inbounds[b] += 1 # [2, 1, 2, 1, 2]
            aboves[b].append(a)
            aboves[a].append(b)#{3: [0], 0: [3, 4], 4: [0, 2], 2: [1, 4], 1: [2]}
        time = 0
        apple = hasApple[:]
        #leaves = [ i for i in range(n) if inbounds[i] == 1 and i != 0] #[1, 3]
        zeros = [ i for i in range(n) if inbounds[i] == 1 and i != 0]#[1, 3 ]
        noVisited = [1] * n #1 = available
        while zeros:#[1, 3] [2, 0]
            temp = []
            for z in zeros:#[2]   
                if z == 0:
                    continue
                
                parent = aboves[z][0]# 4      # aboves[2][0] -> 1
                for t in aboves[z]:
                    if noVisited[t]:
                        parent = t
                inbounds[parent] -= 1 # inbound[4] = 1
                print(z)  #2, 3 
                if apple[z]: #2
                    time += 2  # 4
                    print(time) #4
                    print(2, parent) #2
                    apple[parent] = True # 2->True
                if inbounds[parent] == 1 and parent != 0:#0
                    temp += [parent] #[2]
            zeros = temp #[0]
        return time



class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, parent):
            steps = 0
            for child in adj[node]: # 2, 3  #1
                if child != parent: 
                    steps += dfs(child, node) #dfs(2) -> 2 		dfs(3) -> 2 + 2
											  #dfs(1) -> 0 + 2	#dfs(4) -> 0 + 2

											  #dfs(0) -> 8 + 2            
            return steps + 2 if steps or hasApple[node] else 0 #node0  6
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        result = dfs(0, None)        
        return result - 2 if result else 0
        
#n = 4 edges = [[0,2],[0,3],[1,2]] hasapple = [false,true,false,false] expect = 4

#         0	4 + 4								#callstack: dfs(0) --> dfs(2) --> dfs(1)
#       /   \
#      2 2   3 2
#     /       \ 
#   (1)       (4)

#n = 5  edges = [0,3],[0,4],[1,2], [2, 4]] hasApple = [false, true, false, false, false]


#         0
#       /   \
#      3     4
#           /
#          2
#         /
#       (1)

#n = 6  #edges = [[0,1],[0,2],[1,3],[3,4],[4,5]] #hasApple = [false,true,false,false,true,true]
   #       0
   #      
#note: If the input is non-direction edges, it would be better to use DFS to go through all of the nodes. If edges has directions, it would be better to use BFS to go through each level. It also uses DFS. Most of BFS methods can be wrote in DFS also, but some DFS can not work with BFS. 
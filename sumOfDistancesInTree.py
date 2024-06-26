from typing import List
"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.


Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]


Constraints:

    1 <= n <= 3 * 10^4
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    The given input represents a valid tree.
"""
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Initialize the result array
        res = [0] * n
        
        # Initialize the count array
        count = [1] * n
        
        # Initialize the first dfs function
        def dfs1(node, parent):
            for child in adj[node]:
                if child == parent:
                    continue
                dfs1(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]
        
        # Initialize the second dfs function
        def dfs2(node, parent):
            for child in adj[node]:
                if child == parent:
                    continue
                res[child] = res[node] - count[child] + n - count[child]
                dfs2(child, node)
        
        # Run the dfs functions
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]])) # [8,12,6,10,10,10]
print(Solution().sumOfDistancesInTree(1, [])) # [0]
print(Solution().sumOfDistancesInTree(2, [[1,0]])) # [1,1]
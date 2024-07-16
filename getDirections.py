"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= n
    All the values in the tree are unique.
    1 <= startValue, destValue <= n
    startValue != destValue

Hint 1
The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). The path will travel upwards from node s to the LCA and then downwards from the LCA to node t.

Hint 2
Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?

Hint 3
Remove the longest common prefix of the two path strings to get the path LCA → s, and LCA → t. Each step in the path of LCA → s should be reversed as 'U'.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if dfs(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right, target, path):
                return True
            path.pop()
            return False

        startPath = []
        destPath = []
        dfs(root, startValue, startPath)
        dfs(root, destValue, destPath)
        startPath = ''.join(startPath)
        destPath = ''.join(destPath)
        lcp = 0
        while lcp < len(startPath) and lcp < len(destPath) and startPath[lcp] == destPath[lcp]:
            lcp += 1
        return 'U' * (len(startPath) - lcp) + destPath[lcp:]
    
# Main Call
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

startValue = 3
destValue = 6

solution = Solution()
print(solution.getDirections(root, startValue, destValue))
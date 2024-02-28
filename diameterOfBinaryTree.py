""" 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them. 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root: return 0
        self.max_len = 1
        self._dfs(root)
        return self.max_len - 1
    
    def _dfs(self, node):
        if not node:
            return 0
        
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        
        self.max_len = max(self.max_len, left + right + 1)
        return max(left, right) + 1